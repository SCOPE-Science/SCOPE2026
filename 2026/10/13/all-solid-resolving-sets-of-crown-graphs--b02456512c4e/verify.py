from itertools import combinations
from collections import deque, Counter


def crown_graph(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def all_distances(adj):
    D=[]
    for s in range(len(adj)):
        d=[10**9]*len(adj); d[s]=0
        q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]==10**9:
                    d[v]=d[u]+1; q.append(v)
        D.append(d)
    return D


def is_solid(D, mask):
    # Characterization for 1-solid resolving sets: every ordered x != y
    # has a landmark closer to x than to y.
    N=len(D)
    S=[s for s in range(N) if (mask>>s)&1]
    for x in range(N):
        for y in range(N):
            if x==y: continue
            if not any(D[s][x] < D[s][y] for s in S):
                return False
    return True


def predicted(n, mask):
    N=2*n
    T={v for v in range(N) if not ((mask>>v)&1)}
    A=set(range(n)); B=set(range(n,2*n))
    if T <= A or T <= B:
        return True
    return any(T <= {i,n+i} for i in range(n))


def expected_counts(n):
    # F(z)=2 z^n(1+z)^n-z^(2n)+n z^(2n-2)
    c=Counter()
    from math import comb
    for j in range(n+1):
        c[n+j]+=2*comb(n,j)
    c[2*n]-=1
    c[2*n-2]+=n
    return c

subset_trials=0
basis_total=0
for n in range(3,10):
    adj=crown_graph(n); D=all_distances(adj); N=2*n
    counts=Counter()
    for mask in range(1<<N):
        subset_trials += 1
        actual=is_solid(D,mask)
        pred=predicted(n,mask)
        assert actual==pred,(n,mask,actual,pred)
        if actual:
            counts[mask.bit_count()]+=1
    assert counts==expected_counts(n),(n,counts,expected_counts(n))
    assert min(counts)==n
    assert counts[n]==2
    # Check exact bases are the two bipartition classes.
    A=sum(1<<i for i in range(n))
    B=sum(1<<(n+i) for i in range(n))
    bases={m for m in range(1<<N) if m.bit_count()==n and is_solid(D,m)}
    assert bases=={A,B},(n,bases)
    basis_total += len(bases)

print('VERIFY_OK')
print('parameters_n_checked =', list(range(3,10)))
print('subset_trials =', subset_trials)
print('minimum_bases_checked =', basis_total)
print('all solid-resolving sets matched the complement classification')
print('all coefficient distributions matched 2 z^n(1+z)^n-z^(2n)+n z^(2n-2)')
print('all solid-metric dimensions matched n')
print('all minimum bases were exactly the two bipartition classes')
