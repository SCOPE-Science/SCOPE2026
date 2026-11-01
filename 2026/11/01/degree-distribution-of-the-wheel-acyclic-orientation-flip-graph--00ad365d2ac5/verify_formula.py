#!/usr/bin/env python3
"""Independent exact-coefficient check of wheel degree polynomial by run compositions.
No directed graph, external libraries, numerical approximations, or prior logs used.
"""
from math import comb
from collections import defaultdict
from fractions import Fraction

def mul(p,q):
    out=defaultdict(int)
    for a,ca in p.items():
        for b,cb in q.items():out[a+b] += ca*cb
    return dict(out)

def path_sources(L):
    return {j:comb(L,2*j-1) for j in range(1,(L+1)//2+1)}

def composition_parts(n,k):
    if k == 1:
        if n>=1:yield (n,)
        return
    for first in range(1,n-k+2):
        for tail in composition_parts(n-first,k-1):
            yield (first,)+tail

def via_runs(m):
    D=defaultdict(Fraction)
    # Nonconstant hub-spoke orientations have an even number k of cyclic runs.
    for k in range(2,m+1,2):
        for comp in composition_parts(m,k):
            poly={0:1}
            for L in comp: poly=mul(poly,path_sources(L))
            for sources, count in poly.items():
                D[m-k+sources] += Fraction(2*m,k)*count
    # Constant spokes: each rim word with q runs of each arrow direction.
    D[m] += 4*m
    D[m+1] += 2*m*(m-3)
    for q in range(2,m//2+1):
        D[m+q] += 4*comb(m,2*q)
    assert all(v.denominator == 1 for v in D.values())
    return {d:int(v) for d,v in D.items() if v}

def coeff_poly(m):
    # Algebraic coefficient theorem with Q(x,z)=1-2x+(1-z)x^2.
    # [x^h]Q(x,z)^(-2j) expanded by the binomial theorem.
    D=defaultdict(Fraction)
    for j in range(1,m//2+1):
        h=m-2*j
        for t in range(h//2+1):
            a=Fraction(m,j)*comb(2*j+h-t-1,h-t)*comb(h-t,t)*2**(h-2*t)
            for q in range(t+1):
                D[m+q] += a*comb(t,q)*(-1)**(t-q)
    D[m] += 4*m
    D[m+1] += 2*m*(m-3)
    for q in range(2,m//2+1):D[m+q] += 4*comb(m,2*q)
    assert all(v.denominator==1 for v in D.values())
    return {d:int(v) for d,v in D.items() if v}

def main():
    for m in range(3,13):
        A=via_runs(m)
        B=coeff_poly(m)
        assert A==B,(m,A,B)
        assert sum(A.values())==3**m-3
        assert sum(d*n for d,n in A.items())==2*m*(5*3**(m-2)-3)
        assert min(A)==m
        assert max(A)==(m if m==3 else m+m//2)
        assert A[max(A)]==(24 if m==3 else (4 if m%2==0 else 4*m))
        simple=4*m+sum(Fraction(m,j)*comb(m+2*j-1,m-2*j) for j in range(1,m//2+1))
        assert A[m]==simple
        lucas=[2,1]
        for i in range(2,2*m+1):lucas.append(lucas[-1]+lucas[-2])
        periodic=(2,1,-1,-2,-1,1)[m%6]
        assert A[m]==lucas[2*m]+4*m-4+periodic
        print('FORMULA_WHEEL_PASS',m,dict(sorted(A.items())))
    print('ALL_FORMULA_WHEEL_CHECKS_PASS')

if __name__=='__main__':main()
