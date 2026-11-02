#!/usr/bin/env python3
"""Independent finite checks of the complete symmetric-evolution idempotent count.
Run: python verify.py  (standard Python 3 + sympy)
"""
from itertools import combinations
from fractions import Fraction
from math import comb, sqrt
import cmath
import sympy as sp

def formula(n, r):
    if abs(r-n)<1e-8:
        return 2**(n-1)+1-(comb(n,n//2)//2 if n%2==0 else 0)
    for k in range(1,(n-1)//2+1):
        if abs(r*r-4*k*(n-k))<1e-8:
            return 2**n-comb(n,k)
    return 2**n

def enumerate_and_check(n, r):
    a=r/(r+n); b=1/(r+n)
    candidates={(0j,)*n, (1+0j,)*n}
    for k in range(1,n):
        delta=r*r-4*k*(n-k)
        if abs(delta)<1e-8: delta=0j
        for t in ((r+cmath.sqrt(delta))/(2*k),(r-cmath.sqrt(delta))/(2*k)):
            if abs(t-1)<1e-9: continue
            assert abs(1+t)>1e-9
            v=1/(a*(1+t)); u=t*v
            for subset in combinations(range(n),k):
                indices=set(subset)
                candidates.add(tuple(u if i in indices else v for i in range(n)))
    # Numeric fingerprints do not replace the proof; the count is corroborative.
    distinct={tuple((round(z.real,9),round(z.imag,9)) for z in x) for x in candidates}
    for x in candidates:
        S=sum(z*z for z in x)
        assert all(abs(z-a*z*z-b*S)<1e-7 for z in x), (n,r,x)
    expected=formula(n,r)
    assert len(distinct)==expected, (n,r,len(distinct),expected)
    return len(distinct)

def exact_r_equals_n(n):
    a=Fraction(1,2); b=Fraction(1,2*n)
    out={(Fraction(0),)*n,(Fraction(1),)*n}
    for k in range(1,n):
        if 2*k==n: continue
        u=Fraction(2*(n-k),n); v=Fraction(2*k,n)
        for sub in combinations(range(n),k):
            inds=set(sub)
            out.add(tuple(u if i in inds else v for i in range(n)))
    assert len(out)==formula(n,n),(n,len(out),formula(n,n))
    for x in out:
        S=sum(z*z for z in x)
        assert all(z==a*z*z+b*S for z in x)
    return len(out)

def groebner_test():
    x,y,z=sp.symbols('x y z'); sq=x*x+y*y+z*z
    for r in (sp.Integer(1),sp.Integer(3)):
        a=r/(r+3); b=1/(r+3)
        g=sp.groebner([w-a*w*w-b*sq for w in (x,y,z)],x,y,z,order='lex')
        pol=sp.factor(g.polys[-1].as_expr())
        expected=z*(z-1)*(z*z-5*z+8)*(z*z-3*z+4) if r==1 else z*(z-1)**3*(3*z-4)*(3*z-2)/9
        assert sp.simplify(pol-expected)==0,(r,pol)

def main():
    exact_cases=0
    for n in range(3,12):
        exact_r_equals_n(n); exact_cases+=1
    numeric_cases=0
    for n in range(3,9):
        ratios=[complex(1),complex(n),complex(1,1)]
        for k in range(1,(n-1)//2+1):
            ratios.extend((complex(2*sqrt(k*(n-k))),complex(-2*sqrt(k*(n-k)))))
        for r in ratios:
            enumerate_and_check(n,r);numeric_cases+=1
    groebner_test()
    print('VERIFY_OK exact_r_equals_n_cases=',exact_cases,'numeric_parameter_cases=',numeric_cases,'groebner_cases=2')
    for n in range(3,9):
        print('n=',n,'generic=',2**n,'at_r_n=',formula(n,n),
              'minimal_other=',min(formula(n,2*sqrt(k*(n-k))) for k in range(1,(n-1)//2+1)))
if __name__=='__main__': main()
