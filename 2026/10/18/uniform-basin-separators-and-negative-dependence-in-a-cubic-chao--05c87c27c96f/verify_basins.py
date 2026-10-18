"""Exact finite-depth identities for complementary cubic skew-product maps.

This checker tests algebraic martingale and covariance identities at finite
word lengths. It does not certify almost-sure or infinite-time assertions.
Run: python verify_basins.py
"""
from fractions import Fraction as Q
from itertools import product


def a(beta, x):
    return x * (1 - x) * (x - beta)


def f(beta, sign, x):
    return x + sign * a(beta, x)


def ensemble(beta, u, v, depth):
    su = sv = suu = svv = suv = sq = Q(0)
    for signs in product((-1, 1), repeat=depth):
        x, y = u, v
        for sign in signs:
            x, y = f(beta, sign, x), f(beta, sign, y)
        assert Q(0) < x < beta < y < 1
        su += x
        sv += y
        suu += x*x
        svv += y*y
        suv += x*y
        sq += a(beta, x)*a(beta, y)
    denom = 1 << depth
    return tuple(z/denom for z in (su,sv,suu,svv,suv,sq))


def run():
    checks = 0
    for beta in (Q(1,3), Q(1,2), Q(2,3)):
        u, v = beta/2, (beta+1)/2
        prev = None
        running = Q(0)
        for n in range(5):
            values = ensemble(beta,u,v,n)
            mu,mv,su2,sv2,cross,q = values
            assert mu == u and mv == v
            assert q < 0
            if prev is not None:
                # Martingale product identity, exact at finite depth.
                assert cross - prev[4] == prev[5]
                # Conditional variance increments are squared fiber kicks.
                kicku=ensemble_squares(beta,u,n-1)
                kickv=ensemble_squares(beta,v,n-1)
                assert su2-prev[2] == kicku
                assert sv2-prev[3] == kickv
                checks+=3
            assert cross <= u*v
            prev=values
            checks+=4
        # Strict covariation is visible already at depth one.
        assert ensemble(beta,u,v,1)[4] - u*v == a(beta,u)*a(beta,v)
        checks+=1
    beta=Q(1,2)
    u,v=Q(1,4),Q(3,4)
    assert a(beta,u)*a(beta,v) == -Q(9,4096)
    assert Q(1,4) + a(beta,u)*a(beta,v)/(beta*(1-beta)) == Q(247,1024)
    checks+=2
    print('PASS: '+str(checks)+' exact finite-depth rational identity checks;')
    print('uniform-marginal and negative-dependence limits rely on analytical proof.')


def ensemble_squares(beta,x,depth):
    out=Q(0)
    for signs in product((-1,1), repeat=depth):
        z=x
        for sign in signs:
            z=f(beta,sign,z)
        out+=a(beta,z)**2
    return out/Q(2)**depth


if __name__=='__main__':
    run()
