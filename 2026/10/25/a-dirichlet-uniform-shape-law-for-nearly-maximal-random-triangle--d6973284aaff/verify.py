#!/usr/bin/env python3
"""Numerical and exact-arithmetic checks for a geometric conditional limit theorem."""
import math, random
from fractions import Fraction as F

# Direct area determinant versus expanded near-corner deficit.
rng=random.Random(942128)
for i in range(20000):
    a,b,c,d,e,f=[rng.random()*0.17 for _ in range(6)]
    det=(1-c-a)*(1-f-b)-(d-b)*(e-a)
    h=1-det
    expanded=a+b+c+f+d*e-a*d-a*f-b*c-b*e-c*f
    assert abs(h-expanded)<1e-12
print('EXACT_GEOMETRIC_DETERMINANT_EXPANSION_OK 20000')

# Four linear defects plus one product: exact integral over [0,eta]^2.
# J(h) = h^5/24 * int_0^1 (1-w)^4[log(eta^2/h)-log(w)]dw
# = h^5/120 * (log(eta^2/h)+H_5); the integral of -log(w)
# is H_5/5. Verify both rational beta integral identities.
I0=sum(F((-1)**k*math.comb(4,k),k+1) for k in range(5))
I1=sum(F((-1)**k*math.comb(4,k),(k+1)**2) for k in range(5))
H5=sum((F(1,k) for k in range(1,6)),F(0))
assert I0==F(1,5) and I1==H5/5
assert F(24,120)==F(1,5)
print('EXACT_PRODUCT_SINGULARITY_BETA_AND_LOG_INTEGRALS_OK')

# Check formula against independent positive-weight Simpson integral.
for h,eta in [(0.0007,0.12),(0.00003,0.19)]:
    N=60000
    step=1/N
    sm=0.
    # midpoint integration of a smooth-ish integrand after w=z^2.
    for k in range(N):
        z=(k+0.5)*step
        w=z*z
        sm += 2*z*(1-w)**4*(math.log(eta*eta/h)-math.log(w))
    sim=h**5/24*sm*step
    exact=h**5/120*(math.log(eta*eta/h)+float(H5))
    assert abs(sim-exact)/exact<1e-6,(sim/exact,h,eta)
print('INDEPENDENT_PRODUCT_INTEGRAL_QUADRATURE_OK')

# Dirichlet(1,...,1) 6-part simplex and independent logarithmic exponent.
# x=(a,b,c,f,ed)/h, sixth coordinate is unused deficit slack.
# For each h the constructed points lie inside the actual near-max event.
for h in (0.002, 0.000005):
    n=110000
    sm=[0.0]*5; sv=0; su=0; independent=0; close=0
    maxdiff=0
    for _ in range(n):
        z=[-math.log(rng.random()) for _ in range(6)]
        total=sum(z)
        t=[k/total for k in z]
        u=rng.random()
        a,b,c,f=[h*x for x in t[:4]]
        e=h**u; d=h**(1-u)*t[4]
        v=d*e
        delta=a+b+c+f+v-a*d-a*f-b*c-b*e-c*f
        assert 0<=delta<h+1e-13
        assert max(a,b,c,d,e,f)<=1
        maxdiff=max(maxdiff,abs(delta/h-sum(t[:5])))
        close += max(a,b,c,d,e,f)<0.2
        for j in range(5): sm[j]+=t[j]
        smU = u
        su += smU
        sv += t[4]
        independent += u*t[4]
    assert all(abs(s/n-1/6)<0.004 for s in sm)
    assert abs(su/n-0.5)<0.004
    assert abs(independent/n -1/12)<0.002
    print('CORNER_SIMPLEX_AND_LOG_EXPONENT_CHECK_OK',h,'fraction_near_corners',round(close/n,5),'max_normalized_correction',round(maxdiff,5))

print('ALL_SQUARE_NEAR_MAXIMUM_SHAPE_CHECKS_OK')
