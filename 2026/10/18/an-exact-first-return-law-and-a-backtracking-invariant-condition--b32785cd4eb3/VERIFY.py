"""Independent finite-time first-return check for a second-order walk on a regular tree.

Run: python VERIFY.py.  Uses Python's standard library only.
"""
from fractions import Fraction as F
from math import sqrt

def calc(d, back_weight, forward_weight, steps=30):
    q=F(back_weight, back_weight+(d-1)*forward_weight)
    r=F(forward_weight, back_weight+(d-1)*forward_weight)
    # Direct radial Markov walk from first visited neighbor, last edge outward.
    mass={(1, 'out'): F(1)}
    first=[]
    for t in range(1, 2*steps+2):
        nxt={}
        hit=F(0)
        for (k, direction), prob in mass.items():
            toward=q if direction=='out' else r
            away=1-toward
            if k==1:hit+=prob*toward
            else:nxt[(k-1,'in')]=nxt.get((k-1,'in'),F(0))+prob*toward
            nxt[(k+1,'out')]=nxt.get((k+1,'out'),F(0))+prob*away
        if t%2==1:first.append(hit)
        else: assert hit == 0
        mass=nxt
    # Independently derive the series by comparing coefficients of
    # z(1-r)H(z)^2-(1+(q-r)z*z)H(z)+q*z=0.
    coeff=[]
    for n in range(steps+1):
        if n==0: u=q
        else:
            u=(r-q)*coeff[n-1]+(1-r)*sum((coeff[i]*coeff[n-1-i] for i in range(n)),F(0))
        coeff.append(u)
        assert u>=0
        assert first[n] == u, (d,q,r,n,first[n],u)
    h=q/(1-r)
    expected=F(2*(d-1),d-2)
    # Independently calculate conditional first-return expectation by
    # differentiating the algebraic equation at z=1.
    deriv=q*(1+r-q)/((1-r)*(1-r-q))
    assert F(1)+deriv/h == expected
    assert h==F(back_weight,back_weight+(d-2)*forward_weight)
    rho=(1-float(q))/sqrt(d-1)+sqrt(float(q)*(float(q)+d-2)/ (d-1))
    assert 0<rho<1
    return steps+4

checks=0
for d in (3,4,5,7):
    for a,g in ((1,1),(2,1),(1,3),(7,1),(1,7)):
        checks+=calc(d,a,g,steps=32)
print(f'PASS: {checks} checks (finite first-return coefficients, exact identities and exponential rate).')
