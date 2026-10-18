"""Standalone reproducibility checks for the hyperdegree group-opinion map.

Python 3 standard library only. Finite tests supplement, not replace, the proof.
"""
from fractions import Fraction as Q
from random import Random
from math import tanh, cosh


def det3(a):
    return (a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
            - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
            + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0]))


def gram(degrees, weights, slopes):
    kb = sum(w * k for w, (k, q) in zip(weights, degrees))
    qb = sum(w * q for w, (k, q) in zip(weights, degrees))
    A = sum(w * (k / kb)**2 * s for w, (k, q), s in zip(weights, degrees, slopes))
    B = sum(w * (k / kb) * (q / qb) * s for w, (k, q), s in zip(weights, degrees, slopes))
    C = sum(w * (q / qb)**2 * s for w, (k, q), s in zip(weights, degrees, slopes))
    return A, B, C


def check_exact():
    rng = Random(240813336)
    trials = 0
    for _ in range(1200):
        count = rng.randrange(1, 8)
        degrees = [(Q(rng.randrange(0, 9)), Q(rng.randrange(0, 9))) for _ in range(count)]
        if not sum(k for k, q in degrees) or not sum(q for k, q in degrees):
            continue
        weights_raw = [rng.randrange(1, 8) for _ in degrees]
        weights = [Q(w, sum(weights_raw)) for w in weights_raw]
        slopes = [Q(rng.randrange(1, 30), rng.randrange(1, 12)) for _ in degrees]
        A, B, C = gram(degrees, weights, slopes)
        assert A >= 0 and C >= 0 and A*C - B*B >= 0
        a = Q(rng.randrange(0, 6), rng.randrange(1, 9))
        b = -Q(rng.randrange(0, 8), rng.randrange(1, 9))
        E = Q(rng.randrange(0, 12), rng.randrange(1, 8))
        H = Q(rng.randrange(0, 12), rng.randrange(1, 8))
        J = [[a*A, Q(0), b*B], [a*B, Q(0), b*C], [Q(0), E, H]]
        for s in (Q(1, 100), Q(1), Q(7, 3)):
            Jshift = [[J[i][j] + (s if i == j else 0) for j in range(3)] for i in range(3)]
            exact = det3(Jshift)
            expected = s*(s+a*A)*(s+H) + E*(-b)*(s*C + a*(A*C-B*B))
            assert exact == expected and exact > 0
        # The period-two secant algebra: U differences cannot oppose Y differences.
        K = (-b)*(C - a*B*B/(1+a*A))
        assert K >= 0 and 1+H+E*K > 0
        trials += 1
    return trials


def f(x, m):
    return (1+tanh(m*(x-0.5)))/2


def derivative(x, m):
    return m/(2*cosh(m*(x-0.5))**2)


def low_fixed(m):
    # For m>2, f(x)-x>0 at x=0 and <0 immediately left of 1/2.
    left, right = 0.0, 0.5-1e-6
    assert f(left,m) > left and f(right,m) < right
    for _ in range(120):
        mid = (left+right)/2
        if f(mid,m) > mid:
            left = mid
        else:
            right = mid
    return (left+right)/2


def check_two_cycles():
    tests = 0
    for m in (2.01, 2.1, 2.5, 3.0, 4.0, 6.0, 10.0, 20.0):
        lo = low_fixed(m)
        hi = 1-lo
        rho = derivative(lo,m)
        assert lo < 0.5 < hi and 0 < rho < 1
        assert abs(f(lo,m)-lo) < 1e-12
        assert abs(f(hi,m)-hi) < 1e-12
        point_a = (lo, lo, hi)
        point_b = (hi, hi, lo)
        def update(state):
            V,U,Y = state
            return (f(Y,m), f(Y,m), f(U,m))
        assert max(abs(v-w) for v,w in zip(update(point_a),point_b)) < 1e-12
        assert max(abs(v-w) for v,w in zip(update(point_b),point_a)) < 1e-12
        # The two-step Floquet multipliers are 0, rho**2, rho**2.
        assert rho*rho < 1
        for perturb in ((0.0001,0,0),(0,0.0001,0),(0,0,0.0001)):
            x=tuple(v+e for v,e in zip(point_a, perturb))
            # Regression: two-step distances contract after finite iterations.
            for _ in range(400):
                x=update(update(x))
            # Bistability means large perturbations may escape to a fixed point;
            # the chosen perturbations are local and small.
            assert max(abs(v-w) for v,w in zip(x,point_a)) < 0.001
            tests += 1
    return tests


if __name__ == '__main__':
    n = check_exact()
    m = check_two_cycles()
    print(f'PASS: {n} exact-rational Gram/secant/spectral trials; {m} 2-cycle perturbation trials.')
    print('These finite checks are not a proof for arbitrary degree distributions.')
