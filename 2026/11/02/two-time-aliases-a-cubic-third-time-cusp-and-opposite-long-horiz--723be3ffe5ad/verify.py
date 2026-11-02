"""Standalone exact-arithmetic checks for a two-time exponential-affine identification law.
Run: python verify.py
"""
from fractions import Fraction as Q
from math import exp, log, isclose

def mult(m, z, n):
    # For integer n >= 1, this evaluates the scalar map exactly on rational data.
    return m**n*(1-z)**(n-1)*(1+(n-1)*z)

checks=0
for den in range(2, 19):
    for num in range(1, den):
        z=Q(num,den)
        for m in [Q(1,5),Q(1,2),Q(2,3),Q(4,5),Q(1,1),Q(6,5)]:
            d=m*m*z*z
            second=m*m-d
            plus=mult(m,z,3)
            minus=mult(m,-z,3)
            assert mult(m,z,1)==mult(m,-z,1)==m
            assert mult(m,z,2)==mult(m,-z,2)==second
            assert plus-minus == 4*(m*z)**3
            assert plus+minus == 2*(3*m*second-2*m**3)
            assert (plus-3*m*second+2*m**3)**2==4*d**3
            assert (minus-3*m*second+2*m**3)**2==4*d**3
            assert (plus+2*m**3-3*m*second)/(2*m*d) == z
            assert (minus+2*m**3-3*m*second)/(2*m*d) == -z
            for sign in [1,-1]:
                zz=sign*z
                bh=zz/(1-zz)
                q=m*(1-zz)
                for n in range(1,9):
                    assert q**n*(1+n*bh)==mult(m,zz,n)
                    checks+=1
            if m<1 and m*(1+z)>1:
                assert m*(1-z)<1
            checks+=8
# third-horizon rational example gives stable observations and opposite future signs.
m,z=Q(4,5),Q(3,5)
assert mult(m,z,1)==mult(m,-z,1)==Q(4,5)
assert mult(m,z,2)==mult(m,-z,2)==Q(256,625)
assert mult(m,z,3)==Q(2816,15625)
assert mult(m,-z,3)==-Q(4096,15625)
assert m*(1-z)==Q(8,25) and m*(1+z)==Q(32,25)
checks+=6
# Noninteger horizon checks against the *original* real-exponential formula.
for m in [.25,.6,.8,1.1]:
    for z in [.13,.36,.61,.85]:
        for sign in [-1,1]:
            zz=sign*z
            q=m*(1-zz)
            a=log(q)
            b=zz/(1-zz)
            for s in [.07,.3,.5,.97,1.,1.3,2.,2.4,2.9,3.,3.7,7.2]:
                lhs=exp(a*s)*(1+b*s)
                rhs=m**s*(1-zz)**(s-1)*(1+(s-1)*zz)
                assert isclose(lhs,rhs,rel_tol=1e-12,abs_tol=1e-12)
                checks+=1
# A discrete heat semigroup with constant mode: e^{sL} = P + e^{-3 k s}(I-P).
k=.4
for s in [1.,2.,3.,3.25]:
    p=m=4/5
    z=3/5
    e=exp(-3*k*s)
    x=[.2,1.,-1.3]
    avg=sum(x)/3
    evolved=[avg+e*(v-avg) for v in x]
    outplus=[(p**s*(1-z)**(s-1)*(1+(s-1)*z))*v for v in evolved]
    outminus=[(p**s*(1+z)**(s-1)*(1-(s-1)*z))*v for v in evolved]
    if s in (1.,2.):
        assert all(isclose(u,v,rel_tol=1e-12,abs_tol=1e-12) for u,v in zip(outplus,outminus))
    if s==3.:
        assert not isclose(outplus[0],outminus[0])
    checks+=1
print('PASS',checks,'rational/float identities and heat-mode spot checks')
