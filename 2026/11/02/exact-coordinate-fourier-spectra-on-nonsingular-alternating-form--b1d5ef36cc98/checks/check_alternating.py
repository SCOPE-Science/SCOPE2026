#!/usr/bin/env python3
"""Exact finite-field checker for the full-rank alternating-form Fourier frame.
Pure Python (standard library); prime-field instances only. The analytic proof
extends to every prime-power field and all even ambient dimensions.
"""
from fractions import Fraction
from itertools import combinations, product
from math import comb


def pfaffian(M, indices, q):
    if not indices:
        return 1
    i = indices[0]
    ans = 0
    for jnum in range(1, len(indices)):
        j = indices[jnum]
        rest = indices[1:jnum] + indices[jnum + 1:]
        ans += (-1)**(jnum + 1) * M[i][j] * pfaffian(M, rest, q)
    return ans % q


def prediction(q,d):
    A, B = q**(d-1)-1, q**(d-3)-1
    a=Fraction(-1,A); b=Fraction(1,A*B)
    return a,b


def run(q,d):
    assert q in (2,3,5,7) and d%2==0 and d>=4
    edges = list(combinations(range(d),2))
    E=len(edges)
    totals=[0]*E
    coincidences=[[0]*E for _ in range(E)]
    zero=[0]*E
    N=0
    for v in product(range(q), repeat=E):
        M=[[0]*d for _ in range(d)]
        for (i,j),x in zip(edges,v):
            M[i][j]=x
            M[j][i]=-x % q
        if pfaffian(M,tuple(range(d)),q)==0:
            continue
        N+=1
        for i,x in enumerate(v):
            if x==0: zero[i]+=1
            for j in range(i):
                if x==v[j]: coincidences[j][i]+=1
    a,b=prediction(q,d)
    for i in range(E):
        mom=Fraction(q*zero[i]-N,(q-1)*N)
        assert mom==a, ('one',q,d,edges[i],mom,a)
        for j in range(i+1,E):
            # Due to scaling invariance, counts of x-y=0 determine Fourier expectation.
            mom=Fraction(q*coincidences[i][j]-N,(q-1)*N)
            t = a if len(set(edges[i])&set(edges[j]))==1 else b
            assert mom==t, ('pair',q,d,edges[i],edges[j],mom,t)
    # Spectrum from incidence spaces of J(d,2).
    lam2=1-2*a+b
    lam1=1+(d-4)*a-(d-3)*b
    lam0=1+2*(d-2)*a+comb(d-2,2)*b
    tr=1+lam0
    det=lam0-E*a*a
    assert det>0 and lam1>0 and lam2>0
    assert tr+(d-1)*lam1+(E-d)*lam2==E+1
    # The sign of the characteristic polynomial at lambda_2 controls
    # whether the exceptional upper eigenvalue has passed it.
    P=(lam2-1)*(lam2-lam0)-E*a*a
    target=Fraction(d-1,2)*((8-d)*(q**(d-3)-1)**2-2*(d-6)*(q**(d-3)-1)-(d-4))
    assert P==target/Fraction((q**(d-1)-1)**2*(q**(d-3)-1)**2)
    assert (P<0)==(d>=8)
    return {'q':q,'d':d,'forms':N,'entries':E,
            'exact_single':str(a),'exact_disjoint':str(b),
            'checked_moments':E+E*(E-1)//2,
            'spectrum_trace':str(tr),'spectrum_det':str(det),
            'lambda2_beats_mu_plus': bool(P>0)}


def main():
    for q,d in [(2,4),(3,4),(5,4),(2,6)]:
        print(run(q,d))
    print('PASS: every enumerated off-diagonal Fourier moment, exact spectral trace/determinant and transition sign')

if __name__=='__main__':
    main()
