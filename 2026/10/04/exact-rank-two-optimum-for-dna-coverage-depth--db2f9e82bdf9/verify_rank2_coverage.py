#!/usr/bin/env python3
from fractions import Fraction


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def expectation(ms):
    n = sum(ms)
    if sum(m > 0 for m in ms) < 2:
        return None
    return Fraction(1, 1) + sum(Fraction(m, n - m) for m in ms if m)


def optimum_formula(q, n):
    Q = q + 1
    a, r = divmod(n, Q)
    return (Fraction(1, 1)
            + (Q - r) * Fraction(a, n - a)
            + r * Fraction(a + 1, n - a - 1))


def main():
    for q in range(2, 7):
        Q = q + 1
        for n in range(2, 11):
            vals = []
            for ms in compositions(n, Q):
                e = expectation(ms)
                if e is not None:
                    vals.append((e, ms))
            observed = min(e for e, _ in vals)
            predicted = optimum_formula(q, n)
            assert observed == predicted, (q, n, observed, predicted)
            a, r = divmod(n, Q)
            target = sorted([a + 1] * r + [a] * (Q - r))
            minimizers = [ms for e, ms in vals if e == observed]
            assert minimizers
            assert all(sorted(ms) == target for ms in minimizers), (q, n)
            if n <= Q:
                assert predicted == Fraction(1, 1) + Fraction(n, n - 1)
    for n in range(3, 20):
        for y in range(0, n - 2):
            for x in range(y + 2, n):
                f = lambda t: Fraction(t, n - t)
                assert f(x) + f(y) > f(x - 1) + f(y + 1)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
