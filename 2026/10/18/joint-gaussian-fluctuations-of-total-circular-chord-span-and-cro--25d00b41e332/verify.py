"""Standalone exact enumeration and analytic checks for random matching span/crossing theorem.

Run with Python 3 standard library: python verify.py
The checked finite cases are not a substitute for the proof of the limit law.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

@lru_cache(None)
def matchings(vertices):
    if not vertices:
        return ((),)
    a = vertices[0]
    return tuple(((a, b),) + rest
                 for ix, b in enumerate(vertices[1:])
                 for rest in matchings(vertices[1:ix+1] + vertices[ix+2:]))

def length(e, n):
    a, b = e
    gap = b-a-1
    return min(gap, 2*n-2-gap)

def cross(e, f):
    a,b = e
    c,d = f
    return int((a<c<b<d) or (c<a<d<b))

def rational_moments(n):
    ps = matchings(tuple(range(2*n)))
    sums = [0]*5
    for p in ps:
        l = sum(length(e,n) for e in p)
        c = sum(cross(e,f) for i,e in enumerate(p) for f in p[i+1:])
        for i,z in enumerate((l,c,l*l,c*c,l*c)):
            sums[i] += z
    m = len(ps)
    el,ec,el2,ec2,elc=[F(x,m) for x in sums]
    return m,el,ec,el2-el*el,ec2-ec*ec,elc-el*ec

def predicted(n):
    EL=F(n*(n-1)**2,2*n-1)
    EX=F(n*(n-1),6)
    VL=F(2*n*n*(n-1)**2*(n*n-n+1),3*(2*n-3)*(2*n-1)**2)
    VX=F(n*(n-1)*(n+3),45)
    CLX=F(n**3*(n-1)**2,6*(2*n-3)*(2*n-1))
    return (EL,EX,VL,VX,CLX)

def projection_check():
    # Uniform Q on (0, 1/2); density 2. Integrate polynomials exactly.
    def add(a,b):
        return [x+y for x,y in zip(a+[F(0)]*max(0,len(b)-len(a)),b+[F(0)]*max(0,len(a)-len(b)))]
    def mul(a,b):
        c=[F(0)]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):c[i+j]+=x*y
        return c
    def integral(a):
        return sum(F(2)*v*F(1,2)**(k+1)/F(k+1) for k,v in enumerate(a))
    # E[h(A,B) | Q=q] - Eh = 2q-1/2.
    H=[F(-1,2),F(2)]
    # E[c(A,B) | Q=q] - Ec = 2q(1-q)-1/3.
    C=[F(-1,3),F(2),F(-2)]
    assert integral(H)==integral(C)==0
    assert integral(mul(H,H))==F(1,12)
    assert integral(mul(C,C))==F(1,45)
    assert integral(mul(H,C))==F(1,24)
    assert F(1,12)*F(1,45)-F(1,24)**2==F(1,8640)
    assert F(1,45)-F(1,24)**2/F(1,12)==F(1,720)

if __name__=='__main__':
    projection_check()
    total=0
    for n in range(2,8):
        cnt,*obs = rational_moments(n)
        expected=predicted(n)
        for name,observed,formula in zip(('EL','EX','VarL','VarX','CovLX'),obs,expected):
            assert observed==formula, (n,name,observed,formula)
        total += cnt
        print('n=',n,'matchings=',cnt,'finite formula checks=5, PASS')
    assert total==sum(factorial(2*n)//(factorial(n)*2**n) for n in range(2,8))
    print('PROJECTION_INTEGRALS_OK; EXACT_MATCHINGS_CHECKED=',total,'VERIFY_OK')
