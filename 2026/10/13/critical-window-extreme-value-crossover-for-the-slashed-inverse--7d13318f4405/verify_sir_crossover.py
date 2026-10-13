"""Numerical cross-checks for the beta-slashed inverse-Rayleigh tail crossover.

Dependencies: Python 3, mpmath, SciPy. Run: python verify_sir_crossover.py
The exact asymptotic conclusions require the analytical proof in RESULT.md;
these finite computations only check formulas and illustrative convergence.
"""
import math
import mpmath as mp
from scipy.integrate import quad

mp.mp.dps = 90


def survival(theta, q, z):
    """Independent-gamma representation of P(X/Y > z)."""
    a = mp.mpf(theta) / mp.mpf(z)**2
    shape = mp.mpf(q) / 2
    return -mp.expm1(-a) + a**shape * mp.gammainc(1 - shape, a, mp.inf)


def stochastic_survival(theta, q, z):
    """Independent conditional integral, via -q log(Y)~Exp(1)."""
    a = theta / (z*z)
    f = lambda t: math.exp(-t) * (-math.expm1(-a * math.exp(2*t/q)))
    return quad(f, 0., 30., epsabs=3e-13, epsrel=3e-13)[0]


def phi(k):
    k = mp.mpf(k)
    return -mp.expm1(-k)/k if k else mp.mpf(1)


def near_critical_first(theta, w, z):
    a = mp.mpf(theta)/mp.mpf(z)**2
    L = mp.log(1/a)
    q = 2 + 2*mp.mpf(w)/L
    return survival(theta, q, z)/(a*L*phi(w))


def extremal_two_term(k, n, x=mp.mpf('1.3')):
    k, n, x = mp.mpf(k), mp.mpf(n), mp.mpf(x)
    N = mp.log(n)
    q = 2 + 2*k/N
    b = mp.sqrt(n*N)
    measured = n*survival(1, q, b*x)
    predicted = (phi(k) + (1+mp.exp(-k)*(mp.log(N)+2*mp.log(x)-mp.euler))/N)/x**2
    return measured, predicted


def main():
    comparisons = 0
    for q in [0.5, 1., 1.7, 2., 2.2, 3., 6.]:
        for z in [2., 10.]:
            actual = float(survival(1, q, z))
            independent = stochastic_survival(1., q, z)
            assert abs(actual - independent) < 1e-11, (q, z, actual, independent)
            comparisons += 1
    print(f'Independent conditional-integration comparisons: {comparisons} PASS')

    for q in [mp.mpf('.5'), 1, mp.mpf('1.8'), 2, mp.mpf('2.2'), 3, 10]:
        z = mp.mpf('1e35')
        a = z**-2
        if q < 2:
            predicted = mp.gamma(1-q/2)*a**(q/2)
        elif q == 2:
            predicted = a*mp.log(1/a)
        else:
            predicted = a*q/(q-2)
        ratio = survival(1, q, z)/predicted
        assert abs(ratio - 1) < mp.mpf('.01'), (q, ratio)
    print('Seven three-regime fixed-parameter tail tests: PASS')

    for k in [-3, -1, 0, 1, 3]:
        errors = [abs(near_critical_first(1, k, mp.mpf('1e'+str(e))) - 1)
                  for e in [6, 12, 24]]
        assert errors[2] < errors[1] < errors[0], (k, errors)
        assert errors[-1] < mp.mpf('.05'), (k, errors)
    print('Five uniform-window first-order tests: PASS')

    for k in [-3, -1, 0, 1, 3]:
        ratios = []
        for e in [6, 12, 30]:
            actual, predicted = extremal_two_term(k, mp.mpf(10)**e)
            ratios.append(abs(actual-predicted)/actual)
        assert ratios[-1] < ratios[1] < ratios[0], (k, ratios)
        assert ratios[-1] < mp.mpf('.02'), (k, ratios)
    print('Five triangular-array two-term extreme-tail tests: PASS')

    for k in [-2, 0, 2]:
        ratio = extremal_two_term(k, mp.mpf('1e150'), x=1)[0]/phi(k)
        assert abs(ratio-1) < mp.mpf('.05'), (k, ratio)
    print('Three Fréchet-crossover limit checks: PASS')
    print('ALL NUMERICAL CHECKS PASS (not a substitute for infinite proofs)')

if __name__ == '__main__':
    main()
