#!/usr/bin/env python3
"""Independent finite arithmetic checks for a double-star dual numerical-radius formula.

No finite test proves the theorem for all parameters. The accompanying proof does.
"""
from fractions import Fraction
import math


def closed_value(p, q, beta):
    threshold = (p*q)**0.25
    if beta <= threshold:
        return 2*(math.sqrt(p)+math.sqrt(q))
    return 2*math.sqrt(p+q+beta*beta+p*q/(beta*beta))


def witness(p, q, beta):
    if beta <= (p*q)**0.25:
        return 2/math.sqrt(p), 2/math.sqrt(q), 0.0
    z = (beta**4-p*q)/(beta**2*(beta**2+p))
    assert 0 < z < 1
    st = math.sqrt(z)
    ct = math.sqrt(1-z)
    den = math.sqrt(q+beta*beta*z)
    cp = math.sqrt(q)/den
    sp = beta*st/den
    return 2*ct/math.sqrt(p), 2*cp/math.sqrt(q), 2*st*sp


def singular_norm(u, v, c):
    trace = u*u+v*v+c*c
    discr = max(0., trace*trace-4*u*u*v*v)
    return math.sqrt((trace+math.sqrt(discr))/2)


def grid_lower(p,q,beta,denominator=70):
    best=0.
    for iu in range(denominator+1):
        u=2*iu/denominator
        for iv in range(denominator+1):
            v=2*iv/denominator
            c=math.sqrt(max(0.,(4-u*u)*(4-v*v)))/2
            best=max(best,math.sqrt(p)*u+math.sqrt(q)*v+beta*c)
    return best


def main():
    checked=0
    assert (Fraction(4)-1)*(Fraction(4)-1) == 4*Fraction(3,2)**2
    assert Fraction(1)+Fraction(1)+2*Fraction(3,2)==5
    checked += 2
    for p in range(1,11):
        for q in range(1,11):
            for beta in [0, 0.25, 0.5, 1, 2, 3, 4, 7, 11,
                         (p*q)**0.25, (p*q)**0.25*(1+1.e-4)]:
                x, y, c = witness(p,q,beta)
                assert min(x,y,c) >= -1.e-12
                u,v=math.sqrt(p)*x,math.sqrt(q)*y
                singular=singular_norm(u,v,c)
                # Constraints can be strictly feasible when beta=0, but the
                # chosen witness is always on the norm-one boundary.
                assert math.isclose(singular,2,rel_tol=2.e-10,abs_tol=2.e-10), (p,q,beta,singular)
                obj=p*x+q*y+beta*c
                expected=closed_value(p,q,beta)
                assert math.isclose(obj,expected,rel_tol=2.e-10,abs_tol=2.e-10), (p,q,beta,obj,expected)
                checked += 2
    for p in range(1,12):
        for q in range(1,12):
            for beta in (2, 3, 4, 5, 7, 11):
                if beta**4 <= p*q:
                    continue
                z=(Fraction(beta)**4-p*q)/(Fraction(beta)**2*(Fraction(beta)**2+p))
                assert 0 < z < 1
                assert Fraction(beta)**4*(1-z) == p*(q+Fraction(beta)**2*z)
                checked+=2
    for p,q,beta in [(1,1,2),(2,3,1),(2,3,2),(3,7,3),(9,16,3),
                     (1,9,1),(4,4,3),(5,8,5),(2,16,1)]:
        approximate=grid_lower(p,q,beta)
        exact=closed_value(p,q,beta)
        assert approximate<=exact+1.e-8
        assert exact-approximate<0.08, (p,q,beta,exact-approximate)
        checked+=2
    print('VERIFY_OK checks=%d exact_rational_identity=True numeric_witnesses=True grid_comparisons=True' % checked)

if __name__=='__main__':
    main()
