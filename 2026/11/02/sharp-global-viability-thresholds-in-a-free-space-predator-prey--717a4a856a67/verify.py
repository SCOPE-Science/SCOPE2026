#!/usr/bin/env python3
"""Exact-rational boundary-viability checks for a three-species free-space model.

No numerical trajectory is used to certify a global theorem. The mathematical
proof is in RESULT.md; these tests independently evaluate its exact formulas.
"""
from fractions import Fraction as F
from random import Random


def criterion(alpha, beta, eps, gamma, delta, xi, eta):
    d1, d2, d3 = 1-alpha, eps*beta, xi
    a, b = 1-eta, delta-eps*gamma
    if d1 < 0:
        return False
    def pass_edge(d, e):
        # e <= (sqrt(d)+sqrt(d3))^2, compared without a square root
        return e <= d+d3 or (e-d-d3)**2 <= 4*d*d3
    return pass_edge(d1,a) and pass_edge(d2,b)


def boundary_flux(alpha, beta, eps, gamma, delta, xi, eta, p, q, r):
    assert p>=0 and q>=0 and r>=0 and p+q+r==1
    return ((1-alpha)*p + eps*beta*q + xi*r
            + (1-eps)*p*q - (1-eta)*p*r
            - (delta-eps*gamma)*q*r)


def minimizing_edge(d, d3, e):
    if e <= 0:
        return (F(1) if d < d3 else F(0))
    u = (e+d3-d)/(2*e)
    return max(F(0), min(F(1),u))


def worst_point(alpha,beta,eps,gamma,delta,xi,eta):
    if alpha > 1:
        return (F(1),F(0),F(0))
    d1,d2,d3=1-alpha, eps*beta, xi
    u1=minimizing_edge(d1,d3,1-eta)
    u2=minimizing_edge(d2,d3,delta-eps*gamma)
    pts=((u1,F(0),1-u1),(F(0),u2,1-u2))
    return min(pts,key=lambda x:boundary_flux(alpha,beta,eps,gamma,delta,xi,eta,*x))


def run():
    A=(F(1,4), F(1,2), F(3,4),F(1),F(5,4))
    E=(F(1,10),F(1,4),F(1,2),F(1))
    B=(F(1,10),F(1,2),F(1),F(2),F(4))
    rand=Random(920340)
    valid=invalid=grid_checks=0
    for _ in range(5000):
        alpha,beta,eps,gamma,delta,xi,eta=(rand.choice(A),rand.choice(B),rand.choice(E),
            rand.choice(B),rand.choice(B),rand.choice(B),rand.choice(B))
        yes=criterion(alpha,beta,eps,gamma,delta,xi,eta)
        wp=worst_point(alpha,beta,eps,gamma,delta,xi,eta)
        flux=boundary_flux(alpha,beta,eps,gamma,delta,xi,eta,*wp)
        assert (flux >= 0) == yes, (alpha,beta,eps,gamma,delta,xi,eta,wp,flux)
        valid += int(yes); invalid += int(not yes)
        for n in range(11):
            for m in range(11-n):
                p,q,r=F(n,10),F(m,10),F(10-n-m,10)
                f=boundary_flux(alpha,beta,eps,gamma,delta,xi,eta,p,q,r)
                if yes: assert f>=0
                grid_checks+=1
    params= (F(1), F(4,5), F(1,10), F(1), F(139,100), F(21,50), F(1,10))
    assert not criterion(*params)
    assert boundary_flux(*params,F(9,10),F(0),F(1,10))==F(-39,1000)
    # At xi=9/10 the published remaining parameters satisfy both edge tests.
    assert criterion(*(params[:5]+(F(9,10),params[6])))
    assert not criterion(*(params[:5]+(F(899,1000),params[6])))
    print('EXACT_CHECK_OK 5000 parameter tuples,',valid,'inward and',invalid,
          'outward; boundary grid evaluations:',grid_checks)
    print('Source reference outward flux:',F(-39,1000))
    print('Source reference sharp xi cutoff:',F(9,10))

if __name__=='__main__': run()
