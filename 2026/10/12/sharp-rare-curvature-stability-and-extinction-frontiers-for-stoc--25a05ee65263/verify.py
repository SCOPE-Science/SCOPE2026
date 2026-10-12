#!/usr/bin/env python3
"""Independent exact-arithmetic checks for two-curvature Chebyshev descent."""
from fractions import Fraction as Q
from math import comb, cosh, acosh, exp, isclose


def cheb(n, u):
    a, b = Q(1), u
    if n == 0:
        return a
    for _ in range(2, n+1):
        a, b = b, 2*u*b-a
    return b


def recurrence(n, z):
    """Actual undamped first-order RKC stage recursion with z=-alpha*curvature."""
    x0, x1 = Q(1), Q(1)+z/(n*n)
    if n == 1:
        return x1
    for _ in range(2,n+1):
        x0, x1 = x1, (2+2*z/(n*n))*x1-x0
    return x1

checks=0
for s in range(1,13):
    for t in (Q(1,8), Q(1,2), Q(3,4), Q(1), Q(5,4), Q(7,4)):
        for kappa in (Q(3),Q(5,2),Q(7)):
            for curvature in (Q(1),kappa):
                z = -s*s*t*curvature
                assert recurrence(s,z)==cheb(s,Q(1)-t*curvature)
                checks += 1
            a=cheb(s,Q(1)-t)
            b=cheb(s,Q(1)-t*kappa)
            if kappa*t>2:
                assert abs(b)>1
                pstar=(Q(1)-a*a)/(b*b-a*a)
                assert Q(0)<=pstar<Q(1)
                assert (Q(1)-pstar)*a*a+pstar*b*b==1
                checks+=3
            for p in (Q(1,100),Q(1,3),Q(5,6)):
                for n in range(0,8):
                    binomial=sum(Q(comb(n,j)) *p**j*(1-p)**(n-j)*(a**(n-j)*b**j)**2 for j in range(n+1))
                    closed=((1-p)*a*a+p*b*b)**n
                    assert binomial==closed
                    checks+=1
# Exact resonance example: stage 3, lambda_low 1, lambda_high 3, step alpha 9.
s=3; a=cheb(s,Q(0)); b=cheb(s,Q(-2)); p=Q(1,100)
assert a==0 and b==-26
for n in range(1,13):
    assert (p*b)**n==Q(-13,50)**n
    assert (p*b*b)**n==Q(169,25)**n
    checks+=2
# Odd-stage Chebyshev resonance: exact recurrence and exponentially small moment threshold.
for s in range(1,18,2):
    a=cheb(s,Q(0)); b=cheb(s,Q(-2))
    assert a==0 and abs(b)>1
    pstar=Q(1,b*b)
    assert Q(0)<pstar<=Q(1,4)
    asym=4*exp(-2*s*acosh(2))
    if s>=9:
        assert isclose(float(pstar)/asym,1,rel_tol=1e-8)
    checks+=3
print('VERIFY_OK',checks)
