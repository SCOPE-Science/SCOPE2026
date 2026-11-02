"""Finite cross-checks for logarithmic Orlicz sequence gauges.

Python standard library only. Infinite statements require the analytic proof.
"""
from math import exp, log, isclose


def F(t, alpha):
    return 0.0 if t == 0.0 else t * log(exp(alpha) + 1.0/t)**alpha


def root_for_level(y, alpha):
    lo, hi = 0.0, 1.0
    while F(hi, alpha) < y:
        hi *= 2.0
    for _ in range(100):
        mid = (lo + hi)/2
        if F(mid, alpha) < y:
            lo = mid
        else:
            hi = mid
    return (lo + hi)/2


def main():
    tests = 0
    for alpha in [0.25, 0.5, 1.0, 2.0, 3.0, 5.0]:
        a = root_for_level(1.0, alpha)
        assert isclose(F(a, alpha), 1.0, rel_tol=1e-13)
        tests += 1
        for t in [0.00001, 0.001, 0.1, 0.5, 1.0, 3.0, 20.0]:
            ell = log(exp(alpha) + 1/t)
            deriv2 = alpha*ell**(alpha-2)*(alpha-1-ell)/(t*(1+exp(alpha)*t)**2)
            assert deriv2 < 0
            assert F(2*t, alpha) <= 2*F(t, alpha)*(1+1e-13)
            assert F(1.5*t, alpha) > F(t, alpha)
            tests += 3
        for n in [2, 3, 5, 10, 100, 1000, 10000]:
            x = root_for_level(1.0/n, alpha)
            assert isclose(n*F(x, alpha), 1.0, rel_tol=1e-13)
            tests += 1
            for k in [2, 5, 10, 17]:
                m = min(n,100)
                weights = [(i+1)**k for i in range(m)]
                total = float(sum(weights))
                weights = [w/total for w in weights]
                H = log(m)
                for j in range(1,10):
                    u = j/4
                    tail = sum(w for w in weights if log(1/w)>H+u)
                    assert tail <= exp(-u)+1e-13
                    tests += 1
    print('PASS:', tests, 'finite checks')

if __name__ == '__main__':
    main()
