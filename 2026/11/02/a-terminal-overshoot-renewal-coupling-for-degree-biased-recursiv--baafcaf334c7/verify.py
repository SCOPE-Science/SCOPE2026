"""Exact finite consistency checks for the stated renewal coupling.

Finite arithmetic verifies the decrement kernel and the coupling's local
transition identity. Infinite limits are proved in RESULT.md, not here.
"""
from fractions import Fraction as F
from functools import lru_cache


@lru_cache(None)
def harmonic(n):
    if n == 0:
        return F(0)
    return harmonic(n - 1) + F(1, n)


def jump(k):
    assert k >= 2
    return harmonic(k - 1) / (k * (k + 1))


def tail(m):
    if m <= 2:
        return F(1)
    return (harmonic(m - 1) + 1) / m


def kill(m):
    assert m >= 2
    return harmonic(m - 1) / (m - 1)


def cut(m, k):
    assert 2 <= k <= m
    return kill(m) if k == m else F(m, m - 1) * jump(k)


@lru_cache(None)
def cutting_distribution(m):
    if m <= 1:
        return {0: F(1)}
    out = {1: kill(m)}
    for k in range(2, m):
        p = cut(m, k)
        if m - k <= 1:
            out[1] = out.get(1, F(0)) + p
        else:
            for t, x in cutting_distribution(m - k).items():
                out[t + 1] = out.get(t + 1, F(0)) + p * x
    return out


@lru_cache(None)
def passage_distribution(b):
    # The first arrival of a renewal sum at or above the positive boundary b.
    assert b >= 1
    out = {1: tail(b)}
    for k in range(2, b):
        p = jump(k)
        if b - k <= 1:
            out[1] += p
        else:
            for t, x in passage_distribution(b - k).items():
                out[t + 1] = out.get(t + 1, F(0)) + p * x
    return out


def run():
    assertions = 0
    for m in range(2, 180):
        assert sum((jump(k) for k in range(2, m)), F(0)) + tail(m) == 1
        assertions += 1
        assert sum((cut(m, k) for k in range(2, m + 1)), F(0)) == 1
        assertions += 1
        q_over = tail(m)
        b = kill(m)
        assert 0 <= b <= q_over
        assertions += 1
        assert (1 - b / q_over) == (m - 1 - harmonic(m - 1)) / ((m - 1) * (harmonic(m - 1) + 1))
        assertions += 1
        if m >= 3:
            assert sum((jump(k) / (1 - q_over) for k in range(2, m)), F(0)) == 1
            assertions += 1
            for k in range(2, m):
                mixture = jump(k) + (q_over - b) * jump(k) / (1 - q_over)
                assert mixture == cut(m, k)
                assertions += 1

    for n in range(2, 28):
        a = cutting_distribution(n)
        b = passage_distribution(n - 1)
        assert sum(a.values()) == 1 and sum(b.values()) == 1
        assertions += 2
        assert all(x >= 0 for x in a.values()) and all(x >= 0 for x in b.values())
        assertions += 2
        for t in range(0, n + 1):
            # Stochastic domination required by the terminal-overshoot coupling:
            # cutting count is at least renewal first passage.
            assert sum((v for j, v in a.items() if j <= t), F(0)) <= sum(
                (v for j, v in b.items() if j <= t), F(0)
            )
            assertions += 1

    # Independent renewal-mass recursion and residual-size identity.
    u = [F(0)] * 60
    u[0] = F(1)
    for r in range(1, len(u)):
        u[r] = sum((jump(k) * u[r - k] for k in range(2, r + 1)), F(0))
        assert F(0) <= u[r] <= 1
        assertions += 1
    for n in range(2, 59):
        # Last position before crossing n-1 is n-m, and next jump >=m-1.
        total = sum((u[n - m] * tail(m - 1) for m in range(2, n + 1)), F(0))
        assert total == 1
        assertions += 1

    print('PASS: exact rational identities and probability laws')
    print('Assertion count:', assertions)
    print('Cutting states: 2..27; coupling transition sizes: 2..179')
    for n in (4, 8, 12, 20, 27):
        kd = cutting_distribution(n)
        td = passage_distribution(n - 1)
        tv = sum((abs(kd.get(t, 0) - td.get(t, 0)) for t in set(kd) | set(td)), F(0)) / 2
        print('n=%d total_variation=%.8f' % (n, float(tv)))


if __name__ == '__main__':
    run()
