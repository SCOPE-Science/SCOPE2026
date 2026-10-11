"""Independent finite checks for the star order-cone face law.

Requires only the Python standard library. Run: python verify.py
Numerical tests are illustrations, not proofs of the asymptotic theorem.
"""
import math
import random

SQRT2 = math.sqrt(2.0)
SQRT2PI = math.sqrt(2.0 * math.pi)


def phi(u):
    return math.exp(-u * u / 2.0) / SQRT2PI


def tail(u):
    return 0.5 * math.erfc(u / SQRT2)


def g(u):
    return phi(u) - u * tail(u)


def u_scale(m):
    lo, hi = 0.0, math.sqrt(4.0 * math.log(m + 3.0) + 10.0)
    for _ in range(95):
        mid = (lo + hi) / 2.0
        if m * g(mid) > mid:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def project_sorted(root, leaves):
    a = sorted(leaves)
    s = 0.0
    n = len(a)
    for k in range(n + 1):
        t = (root + s) / (k + 1)
        if (k == 0 or a[k - 1] <= t + 1e-12) and (k == n or t <= a[k] + 1e-12):
            return k, t
        if k < n:
            s += a[k]
    raise ArithmeticError('no pooled-set solution')


def project_bisect(root, leaves):
    lo = min([root] + leaves) - 1.0
    hi = max([root] + leaves) + 1.0
    for _ in range(75):
        t = (lo + hi) / 2.0
        f = t + sum(max(t - x, 0.0) for x in leaves)
        if f < root:
            lo = t
        else:
            hi = t
    t = (lo + hi) / 2.0
    return sum(x < t for x in leaves), t


def test():
    rng = random.Random(271828)
    checks = 0
    # Algebraically independent algorithms: sorting/prefix averages vs scalar KKT bisection.
    for m in range(1, 12):
        for _ in range(250):
            root = rng.gauss(0.0, 1.0)
            leaves = [rng.gauss(0.0, 1.0) for j in range(m)]
            k1, t1 = project_sorted(root, leaves)
            k2, t2 = project_bisect(root, leaves)
            assert k1 == k2 and abs(t1 - t2) < 2e-10
            assert abs(t1 - root + sum(max(t1 - g, 0) for g in leaves)) < 1e-10
            assert k1 == sum(g < t1 for g in leaves)
            checks += 3

    # Compare Gaussian face frequencies with independent conic-angle calculation for m=2.
    freq = [0, 0, 0]
    squarenorm_sum = 0.0
    r = 110000
    for _ in range(r):
        root, a, b = [rng.gauss(0.0, 1.0) for j in range(3)]
        k, t = project_sorted(root, [a, b])
        freq[k] += 1
        squarenorm_sum += t*t + max(a,t)**2 + max(b,t)**2
    expected = [1/3, 1/2, 1/6]
    for observed, target in zip(freq, expected):
        assert abs(observed/r-target) < 0.012
        checks += 1
    # E face dimension = E squared norm of Gaussian projection = 13/6.
    assert abs(squarenorm_sum/r - 13/6) < 0.065
    checks += 1
    # Exposed full-dimensional face: root is smallest of all Gaussian coordinates.
    for m in [1, 2, 3, 5, 9]:
        matches = sum(
            project_sorted((draw := [rng.gauss(0, 1) for j in range(m + 1)])[0],draw[1:])[0] == 0
            for _ in range(24000)
        )
        assert abs(matches/24000 - 1/(m+1)) < 0.016
        checks += 1

    scales = []
    for m in [100, 1000, 10000, 100000]:
        u = u_scale(m)
        assert abs(m*g(u)-u) < 1e-7
        scales.append((m, round(u*u,6),round(2*math.log(m),6),round(m*tail(u)/(u*u),6)))
        checks += 2

    print('VERIFY_OK checks=', checks)
    print('m=2 frequencies K=0,1,2:', [round(v/r,6) for v in freq])
    print('scale diagnostics (m,u^2,2log(m),m Phi(-u)/u^2):', scales)


if __name__ == '__main__':
    test()
