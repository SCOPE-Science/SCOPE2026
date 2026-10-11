#!/usr/bin/env python3
"""Finite exact-arithmetic diagnostics for a neutral border-collision first-return law.

This checks representative rational rotations and nonresonant finite orbits;
the Diophantine return-time theorem requires the accompanying proof.
"""
from fractions import Fraction as Q
from math import acos, atan, cos, pi, sin, tan


def step(tau_l, tau_r, state):
    x, y = state
    if x <= 0:
        return (tau_l*x+y+1, Q(0))
    return (tau_r*x+y+1, -x)


def first_return_exact(tau_l, tau_r, x, cap):
    pt = (x, Q(0))
    for t in range(1, cap+1):
        pt = step(tau_l, tau_r, pt)
        if pt[1] == 0:
            return t
    return None


def radial_right_x(tau, x, n):
    """Exact x component after n iterations of the right affine branch."""
    a, b = x, Q(0)
    for _ in range(n):
        a, b = tau*a+b+1, -a
    return a


def predicted_from_circle(tau_float, e, cap):
    phi = acos(tau_float/2)
    alpha = phi / (2*pi)
    width = atan(2*abs(e)*tan(phi/2))/pi
    for k in range(1,cap+1):
        rot = (k*alpha) % 1
        if (e > 0 and rot >= 1-width-1e-12) or (e < 0 and 0 < rot <= width+1e-12):
            return k
    return None


def run():
    count=0
    # Integer trace: exact finite rotation order q, independent of left trace.
    for tau, q in [(-1,3),(0,4),(1,6)]:
        for tl in [Q(-3,2),Q(0),Q(9,4)]:
            for x in [Q(-2),Q(-1,3),Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(2)]:
                x=Q(x)
                observed=first_return_exact(tl,Q(tau),x,q)
                assert observed is not None and 1 <= observed <= q,(tau,x,observed)
                assert (observed == q) if x == Q(1,2) else True
                count+=1
        assert radial_right_x(Q(tau),Q(1,2),q-1)==0
        for n in range(q-1):
            assert radial_right_x(Q(tau),Q(1,2),n)>0
        count+=q
    # The universal switching-tangent ellipse is invariant under the right map.
    def ell(tau, x, y):
        return x*x+tau*x*y+y*y-x+y+Q(1,4)
    for tau0 in [Q(-1), Q(0), Q(1), Q(1,2)]:
        a,b=Q(1,2),Q(0)
        for _ in range(35):
            assert ell(tau0,a,b)==0
            assert a>=0
            a,b=tau0*a+b+1,-a
            count+=1
    # Irrational alpha (Niven's theorem, since cos(phi)=1/4).
    tau=Q(1,2)
    for n in range(1,61):
        actual=float(radial_right_x(tau,Q(1,2),n))
        phi=acos(float(tau)/2)
        expected=(1-cos((n+1)*phi))/(2-float(tau))
        assert abs(actual-expected)<2e-9,(n,actual,expected)
        assert radial_right_x(tau,Q(1,2),n)>0
        count+=1
    for tl in [Q(-4,3),Q(0),Q(7,5)]:
        for e in [Q(1,5),Q(1,10),Q(1,40),Q(1,100),Q(-1,5),Q(-1,10),Q(-1,40),Q(-1,100)]:
            observed=first_return_exact(tl,tau,Q(1,2)+e,3000)
            predicted=predicted_from_circle(float(tau),float(e),3000)
            assert observed is not None and observed==predicted,(tl,e,observed,predicted)
            count+=1
    print('FINITE_DIAGNOSTICS_PASS',count)
    print('Limits: finite tests do not prove irrational recurrence or Diophantine asymptotics.')

if __name__=='__main__':
    run()
