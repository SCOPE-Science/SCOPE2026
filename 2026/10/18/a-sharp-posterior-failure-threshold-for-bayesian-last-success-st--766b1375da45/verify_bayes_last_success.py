"""Finite exact checks for a beta-Bernoulli last-success stopping theorem.

Run with Python 3.10 or later; no third-party packages are required.
The tests are finite consistency checks, not replacements for the proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product


def rising(a, k):
    y = 1
    for j in range(k):
        y *= a + j
    return y


def zero_future(A, B, k):
    return Fraction(rising(B, k), rising(A+B, k))


@lru_cache(maxsize=None)
def continuation(A, B, k):
    """Optimal win chance when only the next k observations remain."""
    if k == 0:
        return Fraction(0)
    after_success = max(zero_future(A+1, B, k-1),
                        continuation(A+1, B, k-1))
    after_failure = continuation(A, B+1, k-1)
    return (A*after_success + B*after_failure)/(A+B)


def brute(A, B, k):
    """Enumerate every deterministic observation-adapted success-only rule."""
    paths = tuple(product((0, 1), repeat=k))
    addresses = []
    for t in range(1, k+1):
        addresses += [w for w in product((0, 1), repeat=t) if w[-1] == 1]
    addresses = {w: i for i, w in enumerate(addresses)}
    weights = [rising(A, sum(w))*rising(B, k-sum(w)) for w in paths]
    best = 0
    for mask in range(1 << len(addresses)):
        winnings = 0
        for w, wt in zip(paths, weights):
            taken = False
            for t, digit in enumerate(w, 1):
                if digit and (mask >> addresses[w[:t]]) & 1:
                    taken = all(v == 0 for v in w[t:])
                    break
            if taken:
                winnings += wt
        best = max(best, winnings)
    return Fraction(best, rising(A+B, k))


def run():
    checks = 0
    for k in range(1, 8):
        C = k*(k-1)+1
        for B in range(1, 25):
            a0 = Fraction(B+k-1, k)
            h = continuation(a0, Fraction(B), k)
            z = zero_future(a0, Fraction(B), k)
            if k == 1 or B >= C:
                assert h == z, (k, B, h, z)
            else:
                assert h > z, (k, B, h, z)
            checks += 1
            for d in (Fraction(1, 4), Fraction(1, 2), Fraction(1)):
                am = a0 - d
                ap = a0 + d
                if am > 0 and B >= C:
                    assert continuation(am, Fraction(B), k) <= zero_future(am, Fraction(B), k)
                    checks += 1
                assert continuation(ap, Fraction(B), k) > zero_future(ap, Fraction(B), k)
                checks += 1
        for B in (Fraction(1, 2), Fraction(3, 2), Fraction(11, 2), Fraction(19, 2)):
            for A in (Fraction(1, 3), Fraction(2, 3), Fraction(7, 4), Fraction(9, 2)):
                m = continuation(A, B, k)/zero_future(A, B, k)
                assert continuation(A+Fraction(1, 5), B, k)/zero_future(A+Fraction(1, 5), B, k) > m
                assert continuation(A, B+Fraction(1, 5), k)/zero_future(A, B+Fraction(1, 5), k) < m
                checks += 2
    for B in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3), Fraction(5), Fraction(10)):
        for A in (Fraction(1, 4), Fraction(2, 3), Fraction(1), Fraction(7, 5), Fraction(5, 2), Fraction(7)):
            k = 2
            expected = (A*(A+B+1) <= B*(B+1) and
                        2*A*B <= B*(B+1))
            actual = zero_future(A, B, k) >= continuation(A, B, k)
            assert expected == actual, (A, B)
            checks += 1
    for k in (1, 2, 3):
        for A, B in ((1, 1), (2, 3), (3, 2)):
            assert brute(A, B, k) == continuation(Fraction(A), Fraction(B), k)
            checks += 1
    # Full policy enumeration at k=4 is an independent 2^15-strategy check.
    assert brute(2, 5, 4) == continuation(Fraction(2), Fraction(5), 4)
    checks += 1
    print(f"PASS: {checks} exact finite assertions, including exhaustive stopping-policy checks")


if __name__ == '__main__':
    run()
