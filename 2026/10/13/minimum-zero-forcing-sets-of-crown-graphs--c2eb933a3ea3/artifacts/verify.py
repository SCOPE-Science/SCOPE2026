from itertools import combinations
from math import comb


def crown_adj(n):
    N=2*n
    adj=[set() for _ in range(N)]
    for i in range(n):
        for j in range(n):
            if i!=j:
                adj[i].add(n+j)
                adj[n+j].add(i)
    return adj


def is_zero_forcing(adj,S):
    blue=set(S)
    while True:
        force=None
        for u in sorted(blue):
            white=adj[u]-blue
            if len(white)==1:
                force=(u,next(iter(white)))
                break
        if force is None:
            return len(blue)==len(adj)
        blue.add(force[1])


def theorem_basis(n,S):
    A=set(range(n)); B=set(range(n,2*n))
    IA={i for i in range(n) if i not in S}
    JB={j for j in range(n) if n+j not in S}
    return len(S)==2*n-4 and len(IA)==2 and len(JB)==2 and IA!=JB

subset_checks=0
basis_checks=0
for n in range(3,10):
    adj=crown_adj(n)
    N=2*n
    z=None; bases=[]
    for k in range(N+1):
        found=[]
        for S in combinations(range(N),k):
            subset_checks+=1
            if is_zero_forcing(adj,S):
                found.append(frozenset(S))
        if found:
            z=k; bases=found; break
    assert z==2*n-4,(n,z)
    expected=comb(n,2)*(comb(n,2)-1)
    assert len(bases)==expected,(n,len(bases),expected)
    for S in combinations(range(N),2*n-4):
        basis_checks+=1
        actual=is_zero_forcing(adj,S)
        predicted=theorem_basis(n,set(S))
        assert actual==predicted,(n,S,actual,predicted)
print(f"VERIFY_OK n_range=3..9 subset_checks={subset_checks} basis_checks={basis_checks} max_order=18")
