from fractions import Fraction as F
from math import floor


def moments(dist):
    s = sum(dist.values(), F(0))
    assert s == 1
    mean = sum(F(j) * p for j, p in dist.items())
    second = sum(F(j*j) * p for j, p in dist.items())
    return mean, second


def lower_second(a):
    q = a.numerator // a.denominator
    d = a - q
    return a*a + d*(1-d)


def endpoint_dist(a):
    q = a.numerator // a.denominator
    d = a - q
    if d == 0:
        return {q: F(1)}
    return {q: 1-d, q+1: d}


def high_dist(a, M):
    assert F(M) > a and a > 1
    p = (a-1) / (M-1)
    return {1: 1-p, M: p}


def mix(d0, d1, lam):
    out = {}
    for j in set(d0) | set(d1):
        out[j] = (1-lam)*d0.get(j, F(0)) + lam*d1.get(j, F(0))
    return {j:p for j,p in out.items() if p}


def R(q, theta, z):
    # q-th power of the explicit extremal pgf h_theta(t), with z=t^q.
    return theta**q * z / (1 - (1-theta**q)*z)

# Exact lower-bound and equality checks on many rational means.
for den in range(1, 16):
    for num in range(den, 8*den + 1):
        a = F(num, den)
        d = endpoint_dist(a)
        mean, second = moments(d)
        assert mean == a
        assert second == lower_second(a)
        q = floor(a)
        for j in range(1, 25):
            assert (j-q)*(j-q-1) >= 0

# Exact full-range interpolation at representative noninteger and integer means.
for a in [F(3,2), F(2), F(5,2), F(11,3), F(5)]:
    low = endpoint_dist(a)
    _, s0 = moments(low)
    for M in [max(floor(a)+2, 5), max(floor(a)+7, 11), max(floor(a)+20, 29)]:
        hi = high_dist(a, M)
        m1, s1 = moments(hi)
        assert m1 == a and s1 > s0
        # Any convex interpolation preserves the mean and interpolates second moments.
        for lam in [F(0), F(1,7), F(1,2), F(6,7), F(1)]:
            dm = mix(low, hi, lam)
            mm, ss = moments(dm)
            assert mm == a
            assert ss == (1-lam)*s0 + lam*s1

# Exact composition identity for integer-extremal families in the transformed variable z=t^q.
for q in range(1, 8):
    for a_theta, b_theta, z in [
        (F(1,2), F(2,3), F(1,5)),
        (F(3,5), F(4,7), F(2,9)),
        (F(5,8), F(7,9), F(3,11)),
    ]:
        left = R(q, a_theta, R(q, b_theta, z))
        right = R(q, a_theta*b_theta, z)
        assert left == right

# Source geometric-dual example: if J is geometric on positive integers with parameter alpha,
# then E[J]=1/alpha and E[J^2]/E[J]=2/alpha-1.
for alpha in [F(1,2), F(2,3), F(3,4), F(4,5)]:
    mean = 1/alpha
    second = (2-alpha)/(alpha*alpha)
    assert second/mean == 2/alpha - 1

print('VERIFY_OK')
