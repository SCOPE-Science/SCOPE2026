"""Exact independent checks for two-leader coherence on Hamming graphs.

Run: python verify.py (requires SymPy). The infinite-dimensional claim
follows from the proof; this program verifies finite exact instances.
"""
from fractions import Fraction
from itertools import product
from math import comb
import sympy as sp


def coefficients(q, d, k):
    out = []
    for j in range(1, d + 1):
        left = comb(d, j) * (q - 1) ** j
        right = sum((-1) ** a * comb(k, a) * comb(d-k, j-a) * (q-1)**(j-a)
                    for a in range(max(0, j-d+k), min(k, j)+1))
        out.append(left-right)
    return out


def predicted_trace(q, d, k):
    n = q ** d
    a = sum((Fraction(comb(d, j)*(q-1)**j, n*q*j) for j in range(1,d+1)), Fraction())
    c = coefficients(q, d, k)
    aa = sum((Fraction(c[j-1],j) for j in range(1,d+1)), Fraction())
    bb = sum((Fraction(c[j-1],j*j) for j in range(1,d+1)), Fraction())
    assert aa > 0
    return 2*n*a-aa/Fraction(2*q)-bb/Fraction(q*aa)


def exact_graph(q,d):
    vertices=list(product(range(q),repeat=d)); n=len(vertices)
    L=sp.zeros(n)
    for i,v in enumerate(vertices):
        L[i,i]=d*(q-1)
        for j in range(i+1,n):
            if sum(x != y for x,y in zip(v,vertices[j]))==1:
                L[i,j]=L[j,i]=-1
    return vertices,L


def verify():
    basic=0
    for q in range(2,9):
        for d in range(2,8):
            vals=[predicted_trace(q,d,k) for k in range(1,d+1)]
            assert all(vals[k]>vals[k+1] for k in range(d-1)),(q,d,vals)
            basic+=d-1
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(4,2),(5,2)]
    inversions=0
    for q,d in cases:
        vs,L=exact_graph(q,d)
        for k in range(1,d+1):
            j=vs.index(tuple([1]*k+[0]*(d-k)))
            keep=[i for i in range(len(vs)) if i not in (0,j)]
            inv=L.extract(keep,keep).inv()
            got=Fraction(sp.trace(inv))
            expected=predicted_trace(q,d,k)
            assert got==expected,(q,d,k,got,expected)
            inversions+=1
        # Count extremizing unordered pairs by distance directly.
        n=len(vs); number=sum(1 for i in range(n) for j in range(i+1,n)
                          if sum(a != b for a,b in zip(vs[i],vs[j]))==d)
        assert number==n*(q-1)**d//2
    print(f'VERIFY_OK rational_strict_comparisons={basic}; grounded_exact_inversions={inversions}; graph_cases={len(cases)}; count_certificates={len(cases)}')

if __name__=='__main__':
    verify()
