"""Independent exhaustive checks for the even-helm minimum zero-forcing census.
Run: python3 check_python.py. This is finite corroboration, not an infinite proof.
"""
from itertools import combinations
from math import comb

def helm(n):
    adj = [0] * (2*n+1)
    def edge(u,v):
        adj[u] |= 1<<v
        adj[v] |= 1<<u
    for i in range(n):
        edge(0,1+i)
        edge(1+i,1+(i+1)%n)
        edge(1+i,1+n+i)
    return adj

def closure(adj,seed):
    target=(1<<len(adj))-1
    current=seed
    while current != target:
        add=0
        for i,neighbor in enumerate(adj):
            if (current>>i)&1:
                rem=neighbor&~current
                if rem and rem & (rem-1) == 0:
                    add |= rem
        if not add:break
        current|=add
    return current==target

def recognized_defects(n,S):
    bits=[int(i in S) for i in range(n)]
    defects=[(i,bits[i]) for i in range(n) if bits[i]==bits[(i+1)%n]]
    if len(defects)<4:return False
    pairs={a:[] for a in (0,1)}
    for t in range(len(defects)):
        i,b=defects[t];j,c=defects[(t+1)%len(defects)]
        if b==c:pairs[b].append((i,j))
    return all(len(pairs[b])==1 and (pairs[b][0][1]-pairs[b][0][0])%n==1 for b in (0,1))

def main():
    for n in range(6,21,2):
        a=helm(n);k=n//2
        states=[]
        for C in combinations(range(n),k):
            leafmask=sum(1 << (1+n+i) for i in C)
            actual=closure(a,leafmask)
            assert actual==recognized_defects(n,set(C)), (n,C)
            if actual:states.append(C)
        expected=6 if n==6 else k*k*2**(k-4)
        assert len(states)==expected,(n,len(states),expected)
        # Any slide from an all-pendant minimum set moves to an internal rim;
        # such a set cannot be a minimum zero forcing set (forcing-chain proof).
        print('n=%d k=%d states=%d expected=%d criterion_ok=yes' % (n,k,len(states),expected))
    # For the small orders, check by all-subset search that no smaller forcing sets exist.
    for n in (6,8,10):
        a=helm(n);k=n//2
        for size in range(k):
            for C in combinations(range(2*n+1),size):
                assert not closure(a,sum(1<<i for i in C)), (n,C)
        print('n=%d no_forcing_set_smaller_than_%d=yes' % (n,k))
    print('PYTHON_VERIFY_OK')
if __name__=='__main__':main()
