"""Reproduce algebraic and numerical checks for a three-state Gibbs transfer matrix.

All calculations are finite checks. The all-parameter conclusions use the proof
in RESULT.md, not numerical extrapolation.
"""
from fractions import Fraction
from math import exp, sqrt


def characteristic(x, s, w):
    return (x - 1) * (x * x - w * x - 1) - s * s


def bisect_root(lo, hi, s, w):
    flo = characteristic(lo, s, w)
    fhi = characteristic(hi, s, w)
    assert flo * fhi < 0, (lo, hi, s, w)
    for _ in range(120):
        mid = (lo + hi) / 2
        fm = characteristic(mid, s, w)
        if mid == lo or mid == hi:
            break
        if fm == 0:
            return mid
        if flo * fm < 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2


def roots(s, w):
    return (bisect_root(1., 3., s, w),
            bisect_root(0., 1., s, w),
            bisect_root(-1., 0., s, w))


def stationary(lam, s, w):
    d = lam - 1
    den = s*s + d*d*(2*lam-w)
    return [s*s/den, lam*d*d/den, (lam-w)*d*d/den]


def transition(lam, s, w):
    d = lam - 1
    return [[1/lam, d/lam, 0.],
            [0., w/lam, (lam-w)/lam],
            [s*s/(lam*d*(lam-w)), 1/(lam*(lam-w)), 0.]]


def test():
    cases = 0
    for s_num in [1, 2, 3, 5, 7, 9]:
        s = Fraction(s_num, 10)
        for w_num in [1, 2, 3, 4, 5, 7, 9]:
            w = Fraction(w_num, 10)
            # Exact finite rational evaluation of p(1+w).
            assert characteristic(1+w, s, w) == w*w-s*s
            # At the crossing the cubic is exactly factorizable.
            if w == s:
                for x in [Fraction(-2), Fraction(-1,4), Fraction(0),
                          Fraction(1), Fraction(5,4), Fraction(3)]:
                    assert characteristic(x, s, w) == (x-1-s)*(x*x-1+s)
            lam, mid, neg = roots(float(s), float(w))
            assert 1<lam<3 and 0<mid<1 and -1<neg<0
            assert abs(lam+mid+neg-(1+float(w)))<1e-11
            if w > s:
                assert mid > -neg
            elif w < s:
                assert mid < -neg
            else:
                assert abs(mid+neg)<1e-11
                assert abs(lam-(1+float(s)))<1e-11
                assert abs(mid-sqrt(1-float(s)))<1e-11
            pi = stationary(lam,float(s),float(w))
            P = transition(lam,float(s),float(w))
            assert abs(sum(pi)-1)<1e-10
            assert all(abs(sum(row)-1)<1e-10 for row in P)
            assert all(abs(sum(pi[i]*P[i][j] for i in range(3))-pi[j])<1e-10 for j in range(3))
            cases += 1

    # Test the universal crossover of stationary weights and spectral gaps
    # using moderate inverse temperatures to avoid tiny-eigenvalue cancellation.
    windows = 0
    a, b = .2, .2
    r_star = (a+b)/2
    for xi in [-2., -1., 0., 1., 2.]:
        for beta in [15., 25., 35.]:
            s = exp(-beta*r_star)
            w = s*exp(-xi)
            lam, mid, neg = roots(s,w)
            d = (exp(-xi)+sqrt(exp(-2*xi)+8))/4
            limit = 1/(1+2*d*d)
            obs = stationary(lam,s,w)[0]
            # First-order errors scale as s, and are recorded as finite checks.
            assert abs(obs-limit)<2.5*s
            # Exact mode dominance is checked above at rational parameters.
            rho = max(mid,-neg)/lam
            coeff = min(sqrt(exp(-2*xi)+8)/2,
                        (3*exp(-xi)+sqrt(exp(-2*xi)+8))/4)
            assert abs((1-rho)/s-coeff)<12*s
            windows += 1
    print(f'VERIFY_OK rational_parameter_cases={cases} crossover_cases={windows}')

if __name__=='__main__':
    test()
