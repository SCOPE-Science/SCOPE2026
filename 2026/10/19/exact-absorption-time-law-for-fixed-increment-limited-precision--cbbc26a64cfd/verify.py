"""Exact-arithmetic checks for the fixed-increment truncated stochastic-rounding absorption theorem.

Only Python's standard library is required. This is a finite stress test, not an
infinite proof. The analytic proof is in RESULT.md.
"""
from fractions import Fraction
from math import floor


def power_two(k):
    return Fraction(2**k) if k >= 0 else Fraction(1, 2**(-k))


def spacing(p, k):
    return power_two(k - p + 1)


def binade(x):
    assert x > 0
    k = x.numerator.bit_length() - x.denominator.bit_length()
    if x < power_two(k):
        k -= 1
    elif x >= power_two(k + 1):
        k += 1
    assert power_two(k) <= x < power_two(k + 1)
    return k


def guard_truncate(x, p, r):
    k = binade(x)
    h = spacing(p + r, k)
    return (x // h) * h


def transition_prob(s, a, p, r):
    k = binade(s)
    d = spacing(p, k)
    assert 0 < a < d
    # s is an exact p-number. Guard truncation is toward zero.
    rounded_guard = guard_truncate(s + a, p, r)
    q = (rounded_guard - s) / d
    assert 0 <= q < 1
    return q


def parameters(E, p, r, a):
    assert p >= 2 and r >= 1
    u0 = spacing(p, E)
    v0 = spacing(p + r, E)
    assert v0 <= a < u0
    L = E
    while spacing(p + r, L) <= a:
        L += 1
    N = 2**(p - 1)
    qq = []
    for k in range(E, L):
        h = spacing(p + r, k)
        t = int(a // h)
        assert 1 <= t < 2**r
        qq.append(Fraction(t, 2**r))
    return L, N, qq


def check():
    steps = 0
    for E in range(-3, 4):
        for p in range(3, 8):
            for r in range(1, 5):
                u0 = spacing(p, E)
                v0 = spacing(p + r, E)
                for m in range(1, 2**r):
                    a = m * v0
                    assert a < u0
                    L, N, qq = parameters(E, p, r, a)
                    # Verify each state independently from the exact
                    # floating grid and the p+r truncation rule.
                    pos = power_two(E)
                    qs = []
                    for k in range(E, L):
                        assert pos == power_two(k)
                        for j in range(N):
                            assert pos == power_two(k) + j*spacing(p, k)
                            q = transition_prob(pos, a, p, r)
                            assert q == qq[k-E], (E,p,r,m,k,j,q,qq[k-E])
                            qs.append(q)
                            pos += spacing(p, k)
                            steps += 1
                    assert pos == power_two(L)
                    assert transition_prob(pos, a, p, r) == 0
                    # Backward state-by-state Bellman equations for the
                    # exact first two moments of absorption time.
                    mean = Fraction(0)
                    var = Fraction(0)
                    for q in reversed(qs):
                        mean += 1/q
                        var += (1-q)/(q*q)
                    predicted_mean = N*sum((1/q for q in qq), Fraction(0))
                    predicted_var = N*sum(((1-q)/(q*q) for q in qq), Fraction(0))
                    assert mean == predicted_mean
                    assert var == predicted_var
                    # At each intermediate grid state exact SR has
                    # strictly positive probability to advance.
                    for k in range(E, L+3):
                        assert a/spacing(p, k) > 0
    print('EXACT_CHECKS_PASSED', steps)
    print('EXAMPLE:', end=' ')
    E,p,r = 0,5,3
    a = spacing(p+r, E)
    L,N,qq = parameters(E,p,r,a)
    mean = N*sum((1/q for q in qq), Fraction(0))
    var = N*sum(((1-q)/(q*q) for q in qq), Fraction(0))
    print(f'E={E}, p={p}, r={r}, a={a}, absorbing_power={L}, expected_steps={mean}, variance={var}')

if __name__ == '__main__':
    check()
