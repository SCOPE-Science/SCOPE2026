"""Exact rational finite-word checks for a triangular Bernoulli cocycle.
The infinite assertions in the accompanying proof are not replaced by enumeration.
"""
from fractions import Fraction
from itertools import product


def prod_matrices(signs, lam, mu):
    a, b, c, d = (Fraction(1), Fraction(0), Fraction(0), Fraction(1))
    for sign in signs:
        a, b, c, d = (lam*a, lam*b, sign*a + mu*c, sign*b + mu*d)
    return a, b, c, d


def partial_cantor(signs, rho):
    return sum((Fraction(sign)*rho**j for j, sign in enumerate(reversed(signs))), Fraction(0))


def check():
    checked = 0
    for lam, mu in ((Fraction(2), Fraction(1,2)), (Fraction(3), Fraction(1)),
                    (Fraction(5), Fraction(2))):
        rho = mu / lam
        assert 0 < rho < Fraction(1,2)
        c = Fraction(1,2)
        assert 0 < c < lam*(1-rho)
        for n in range(1, 9):
            for signs in product((-1, 1), repeat=n):
                a, b, low, d = prod_matrices(signs, lam, mu)
                s = partial_cantor(signs, rho)
                assert (a,b,low,d)==(lam**n,0,lam**(n-1)*s,mu**n)
                for t in (Fraction(1), Fraction(2), Fraction(3)):
                    x = c*rho**(t*n)
                    px, py = a*x+b, low*x+d
                    r = c*rho**((t-1)*n)
                    assert (px*px+py*py)/mu**(2*n) == r*r+(1+r*s/lam)**2
                    checked += 1
    # For rho<1/2 the positive and negative first-cylinder intervals are disjoint.
    for rho in (Fraction(1,4),Fraction(1,3),Fraction(2,5)):
        r = 1/(1-rho)
        assert -1+rho*r < 1-rho*r
        assert 1-rho*r > 0
    print('EXACT_PRODUCTS_AND_SEPARATION_OK', checked)

if __name__ == '__main__':
    check()
