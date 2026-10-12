"""Exact combinatorial checks for local charts of staircase Ferrers toric varieties.

Run with Python 3.10 or later: python ferrers_local_checker.py
No external packages required. This checks finite cases; the general theorem is symbolic.
"""
from collections import Counter
from itertools import combinations, combinations_with_replacement
from math import comb


def catalan(t):
    return comb(2*t,t)//(t+1)


def narayana(t):
    if not t: return [1]
    return [comb(t,k)*comb(t,k+1)//t for k in range(t)]


def chart(m,i,j):
    assert 1 <= i <= m and 1 <= j <= m+1-i
    # coordinates of the ambient monomial torus: a_p (p != i), b_q (q != j)
    dims = [('a',p) for p in range(1,m+1) if p!=i] + [('b',q) for q in range(1,m+1) if q!=j]
    def monomial(coords):
        C=Counter(coords)
        return tuple(C.get(x,0) for x in dims)
    full = {
        monomial(([('a',p)] if p!=i else []) + ([('b',q)] if q!=j else []))
        for p in range(1,m+1) for q in range(1,m+2-p) if (p,q)!=(i,j)
    }
    H,L=m+1-j,m+1-i
    sw={monomial([('b',q)]) for q in range(1,j)} | {
        monomial([('a',p),('b',q)])
        for p in range(H+1,m+1) for q in range(1,m+2-p)}
    ne={monomial([('a',p)]) for p in range(1,i)} | {
        monomial([('a',p),('b',q)])
        for q in range(L+1,m+1) for p in range(1,m+2-q)}
    sm={monomial([('a',p)]) for p in range(i+1,H+1)} | {
        monomial([('b',q)]) for q in range(j+1,L+1)}
    factors=sw|ne|sm
    assert len(factors)==len(sw)+len(ne)+len(sm)
    assert factors <= full
    for f in full:
        if f in factors: continue
        assert any(tuple(x+y for x,y in zip(a,b))==f for a in factors for b in factors)
    # One set of disjoint coordinate blocks per factor.
    supports=[{k for g in S for k,v in enumerate(g) if v} for S in [sw,ne,sm]]
    assert all(not(a&b) for a,b in combinations(supports,2))
    tangent = len(factors)
    expected = 2*m-2+comb(i-1,2)+comb(j-1,2)
    assert tangent==expected,(m,i,j,tangent,expected)
    assert len(sw)==(j-1)+(j-1)*j//2
    assert len(ne)==(i-1)+(i-1)*i//2
    assert len(sm)==2*(m+1-i-j)
    # Independently compute the rank of the Jacobian linear terms
    # from every admissible Ferrers 2-by-2 minor.
    all_edges={(p,q) for p in range(1,m+1) for q in range(1,m+2-p)}
    derivatives=set()
    for p,r in combinations(range(1,m+1),2):
        for q,s in combinations(range(1,m+1),2):
            if {(p,q),(p,s),(r,q),(r,s)}<=all_edges:
                for pair in [((p,q),(r,s)),((p,s),(r,q))]:
                    if (i,j) in pair:
                        derivatives.add(next(x for x in pair if x!=(i,j)))
    jac_tangent=len(all_edges)-1-len(derivatives)
    assert tangent==jac_tangent,(m,i,j,tangent,jac_tangent)
    return tangent


def ferrers_hilbert(t,d):
    # Deduplicate degree-d monomials in the edge semigroup for C_t.
    # Rows are a dummy row and t genuine rows; columns are 1..t.
    if t==0: return 1 if d==0 else 0
    edges=[(0,q) for q in range(t)] + [
        (p,q) for p in range(1,t+1) for q in range(t+1-p)]
    K=set()
    for multiset in combinations_with_replacement(edges,d):
        rows=Counter(p for p,q in multiset)
        cols=Counter(q for p,q in multiset)
        K.add(tuple(rows.get(p,0) for p in range(t+1))+
              tuple(cols.get(q,0) for q in range(t)))
    return len(K)


def expected_hilbert(t,d):
    D=2*t
    N=narayana(t)
    if t==0:return 1 if d==0 else 0
    return sum(v*comb(D+d-k-1,D-1) for k,v in enumerate(N) if d>=k)

count=0
for m in range(2,12):
    for i in range(1,m+1):
        for j in range(1,m+2-i):
            chart(m,i,j)
            count+=1
    if m>=3:
        assert sum(chart(m,i,j)==2*m-2 for i in range(1,m+1)
                   for j in range(1,m+2-i))==4
for t in range(1,7):
    h=narayana(t)
    assert sum(h)==catalan(t)
    for d in range(4 if t<6 else 3):
        got=ferrers_hilbert(t,d)
        want=expected_hilbert(t,d)
        assert got==want,(t,d,got,want)
print('PASS: exact chart semigroup factorization, tangent counts and Jacobian ranks')
print('  charts tested:',count, '(2 <= m <= 11)')
print('PASS: smooth torus-fixed points = four for 3 <= m <= 11')
print('PASS: Narayana-series coefficients via independent monomial enumeration (1 <= t <= 6)')
for m in range(3,9):
    vals=[catalan(i-1)*catalan(j-1) for i in range(1,m+1) for j in range(1,m+2-i)]
    print('m=%d: points=%d, extreme multiplicity=%d, max multiplicity=%d, maximal tangent excess=%d'%
          (m,len(vals),catalan(m-1),max(vals),comb(m-1,2)))
