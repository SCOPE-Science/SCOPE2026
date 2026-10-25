"""Numerical consistency checks for the angular competing-termination theorem.

The proof is analytic; these finite checks do not certify its universal quantifiers.
Requires Python 3 standard library only. Run: python3 checker.py
"""
import math


def H(z, u):
    return 0.5*z*(math.tanh(z) - u*math.tanh(u*z)) - 1.0 + math.cosh(u*z)/math.cosh(z)


def threshold(z):
    lo, hi = 0.0, 0.99
    assert H(z, lo) > 0 and H(z, hi) < 0
    for _ in range(65):
        mid = (lo + hi)/2.0
        if H(z, mid) > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2.0


def conditional_times(z, u):
    # Set L=D=1, hence kappa=z*z.
    kappa = z*z
    F = math.cosh(u*z)/math.cosh(z)
    dF = F*z*(u*math.tanh(u*z)-math.tanh(z))/(2*kappa)
    return 1/kappa + dF/(1-F), -dF/F


def main():
    assert abs(1/math.sqrt(5)-0.4472135954999579) < 1e-14
    for z in (0.5, 1, 3, 10, 30):
        u = threshold(z)
        assert 0 < u < 1
        assert H(z, max(0.0, u-0.05)) > 0
        assert H(z, min(0.999999, u+0.05)) < 0
        kill, esc = conditional_times(z, u)
        assert abs(kill-esc) < 2e-11 * max(1.0, abs(kill), abs(esc))
        print('z=', z, 'threshold=', format(u, '.15g'), 'layer=', format(z*(1-u), '.15g'))
    weak = threshold(0.05)
    c = 8*math.sqrt(5)/1875
    assert abs(weak-(1/math.sqrt(5)+c*0.05**2)) < 5e-7
    w_star = 1.5936242600400401
    assert abs(30*(1-threshold(30))-w_star) < 1e-9
    assert abs(w_star-2*(1-math.exp(-w_star))) < 1e-14
    # Independent weak-killing moment threshold: CV^2 equals one.
    u = 1/math.sqrt(5)
    cv2 = 2*(1+u*u)/(3*(1-u*u))
    assert abs(cv2-1) < 1e-14
    print('All finite consistency checks passed; universal theorem uses analytic proof.')


if __name__ == '__main__':
    main()
