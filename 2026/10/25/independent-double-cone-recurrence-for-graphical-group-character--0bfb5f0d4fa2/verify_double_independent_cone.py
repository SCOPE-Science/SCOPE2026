#!/usr/bin/env python3
"""Finite-field verification of a rank distribution under independent double coning.
All calculations are literal mod-prime linear algebra, independent of the proof's block decomposition.
"""
from collections import Counter
from itertools import product


def rank_modp(mat, p):
    a = [[x % p for x in row] for row in mat]
    n = len(a)
    r = 0
    for col in range(n):
        pivot = next((i for i in range(r, n) if a[i][col] % p), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(u * inv) % p for u in a[r]]
        for j in range(r+1, n):
            c = a[j][col]
            if c:
                a[j] = [(a[j][k] - c*a[r][k]) % p for k in range(n)]
        r += 1
    return r


def spectrum(n, edges, p):
    out = Counter()
    for values in product(range(p), repeat=len(edges)):
        a = [[0]*n for _ in range(n)]
        for (i,j), t in zip(edges, values):
            a[i][j] = t
            a[j][i] = -t
        rank = rank_modp(a, p)
        assert rank % 2 == 0
        out[rank//2] += 1
    return dict(out)


def double_cone(n, edges):
    return n+2, sorted(edges + [(i,n) for i in range(n)] + [(i,n+1) for i in range(n)])


def proposed(n, base, q):
    out=Counter()
    for r,num in base.items():
        d=n-2*r
        assert d>=0
        count0 = 1 if r==0 else q**(2*r)+(q**(2*r)-1)*q**(2*r-1)
        totalp=q**(4*r)
        rank1=(q+1)*(q**d-1)
        rank2=(q**d-1)*(q**d-q)
        out[r] += num*count0
        out[r+1] += num*(totalp-count0+totalp*rank1)
        out[r+2] += num*totalp*rank2
    return {r:c for r,c in out.items() if c}


def check_one(n, edges, p):
    base=spectrum(n,edges,p)
    nn, ee=double_cone(n,edges)
    got=spectrum(nn,ee,p)
    want=proposed(n,base,p)
    assert got==want,(n,edges,p,base,got,want)
    assert sum(got.values())==p**len(ee)
    assert sum(got[r]*p**(nn-2*r)*p**(2*r) for r in got)==p**(nn+len(ee))
    return {'graph_vertices':n,'graph_edges':len(edges),'q':p,'extended_edges':len(ee),'spectrum':dict(sorted(got.items()))}


def rank_count(a,b,r,q):
    if r<0 or r>min(a,b):return 0
    # Number of rank-r matrices: Gaussian binomial times full-rank rows.
    numerator=1
    denominator=1
    for j in range(r):
        numerator *= (q**a-q**j)*(q**b-q**j)
        denominator *= (q**r-q**j)
    assert numerator%denominator==0
    return numerator//denominator


def check_tripartite(a,b,q):
    n=a+b
    edges=[(i,a+j) for i in range(a) for j in range(b)]
    observed=spectrum(n,edges,q)
    predicted={r:rank_count(a,b,r,q) for r in range(min(a,b)+1) if rank_count(a,b,r,q)}
    assert observed==predicted,(a,b,q,observed,predicted)
    return check_one(n,edges,q)

if __name__=='__main__':
    cases=[]
    for p in (2,3,5):
        cases.append(check_one(2,[(0,1)],p))
    for p in (2,3):
        cases.append(check_tripartite(1,2,p))
    cases.append(check_tripartite(2,2,2))
    cases.append(check_one(3,[],3))
    cases.append(check_one(1,[],5))
    for c in cases:
        print('PASS',c)
    print('VERIFY_OK_DOUBLE_CONE',len(cases),'full edge assignment configurations')
