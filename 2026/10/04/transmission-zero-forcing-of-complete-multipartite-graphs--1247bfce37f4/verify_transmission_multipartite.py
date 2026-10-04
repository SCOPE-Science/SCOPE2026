from fractions import Fraction
from itertools import combinations


def parts_of_n(n, lo=1):
    if n == 0:
        yield ()
        return
    for first in range(lo, n+1):
        for rest in parts_of_n(n-first, first):
            yield (first,) + rest


def graph_from_parts(parts):
    labels=[]
    for i,s in enumerate(parts): labels += [i]*s
    n=len(labels)
    nbr=[set() for _ in range(n)]
    for u in range(n):
        for v in range(u+1,n):
            if labels[u]!=labels[v]:
                nbr[u].add(v); nbr[v].add(u)
    return labels,nbr


def succeeds(parts, init, alpha, beta):
    labels,nbr=graph_from_parts(parts)
    n=len(labels)
    filled=set(init)
    weights=[Fraction(1) if v in filled else Fraction(0) for v in range(n)]
    used=set()
    if len(filled)==n: return True
    for _ in range(n+2):
        white=set(range(n))-filled
        sends=[]
        for u in sorted(filled-used):
            w=nbr[u] & white
            if len(w)==1:
                sends.append((u,next(iter(w))))
        if not sends: return False
        inc=[Fraction(0) for _ in range(n)]
        for u,v in sends:
            used.add(u)
            inc[v]+=alpha*weights[u]
        newly=set()
        for v in white:
            weights[v]+=inc[v]
            if weights[v] >= beta:
                newly.add(v)
        if not newly:
            return False
        filled |= newly
        if len(filled)==n: return True
    raise AssertionError('round bound')


def brute_z(parts, alpha, beta):
    n=sum(parts)
    vs=range(n)
    for k in range(n+1):
        for S in combinations(vs,k):
            if succeeds(parts,S,alpha,beta):
                return k
    raise AssertionError


def tau(N,s,a):
    return min((s-1)*a, (N-s-1)*a + (s-1)*a*a)


def formula(parts,a,b):
    N=sum(parts)
    if all(s==1 for s in parts):
        return N-1 if b <= (N-1)*a else N
    T=max(tau(N,s,a) for s in parts if s>=2)
    Delta=N-min(parts)
    if b <= T: return N-2
    if b <= Delta*a: return N-1
    return N


def source_biclique(m,n,a,b):
    assert 2<=m<=n
    if b <= (m-1)*a:
        return m+n-2
    if b <= (n-1)*a and b <= (m-1)*a+(n-1)*a*a:
        return m+n-2
    if b <= n*a:
        return m+n-1
    return m+n


def source_star(N,a,b):
    if b <= (N-2)*a*a: return N-2
    if b <= (N-1)*a: return N-1
    return N

vals=[Fraction(1,4),Fraction(1,3),Fraction(1,2),Fraction(2,3),Fraction(3,4),Fraction(1)]
types=cases=0
for N in range(2,9):
    for parts in parts_of_n(N):
        if len(parts)<2: continue
        types += 1
        for a in vals:
            for b in vals:
                got=brute_z(parts,a,b)
                exp=formula(parts,a,b)
                assert got==exp,(parts,a,b,got,exp)
                cases += 1
# Specialization checks against the source formulas.
spec=0
for N in range(3,13):
    for a in vals:
        for b in vals:
            assert formula((1,N-1),a,b)==source_star(N,a,b)
            spec += 1
for m in range(2,8):
    for n in range(m,9):
        for a in vals:
            for b in vals:
                assert formula((m,n),a,b)==source_biclique(m,n,a,b)
                spec += 1
print(f'ALL CHECKS PASSED; multipartite_types={types}; exhaustive_parameter_cases={cases}; source_specializations={spec}; max_order=8')
