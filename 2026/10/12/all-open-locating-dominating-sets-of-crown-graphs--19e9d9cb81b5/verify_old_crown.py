from itertools import combinations

def crown(n):
    # vertices 0..n-1 = a_i, n..2n-1=b_i
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j); adj[n+j].add(i)
    return adj

def is_old(adj,S):
    S=set(S)
    sig=[]
    for v in range(len(adj)):
        t=frozenset(adj[v]&S)
        if not t: return False
        sig.append(t)
    return len(sig)==len(set(sig))

def predicted(n,S):
    S=set(S)
    A=sum(i in S for i in range(n))
    B=sum(n+i in S for i in range(n))
    return A>=n-1 and B>=n-1

def main():
    total=old=mins=0
    coeffs={}
    for n in range(3,9):
        adj=crown(n)
        local=[]
        for r in range(2*n+1):
            c=0
            for S in combinations(range(2*n),r):
                total+=1
                got=is_old(adj,S); want=predicted(n,S)
                if got!=want:
                    raise AssertionError((n,S,got,want))
                if got: c+=1; old+=1
            if c: local.append((r,c)); coeffs[(n,r)]=c
        want=[(2*n-2,n*n),(2*n-1,2*n),(2*n,1)]
        if local!=want:
            raise AssertionError((n,local,want))
        mins += n*n
    print(f'VERIFY_OK n_range=3..8 subsets={total} old_sets={old} minimum_sets={mins} max_order=16')
if __name__=='__main__': main()
