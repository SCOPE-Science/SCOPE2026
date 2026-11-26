"""Finite checks of the fixed-transition mean and matching swap bound."""
from fractions import Fraction
from math import comb


def matching(mask, m):
    older = recent = 0
    for edge in range(m):
        older, recent = recent, max(recent, older + 1) if mask & (1 << edge) else recent
    return recent


def main():
    means = swaps = 0
    for m in range(1, 12):
        values = [matching(mask, m) for mask in range(1 << m)]
        totals = [0] * (m + 1)
        for mask, k in enumerate(values):
            totals[bin(mask).count('1')] += k
            if m <= 8:
                for i in range(m):
                    if not mask & (1 << i):
                        continue
                    for j in range(m):
                        if not mask & (1 << j):
                            assert abs(k - values[mask ^ (1 << i) ^ (1 << j)]) <= 1
                            swaps += 1
        for t, total in enumerate(totals):
            exact = (m + 1 - t) * sum(Fraction(comb(t, r), comb(m, r)) for r in range(1, t + 1, 2))
            assert Fraction(total, comb(m, t)) == exact, (m, t)
            means += 1
    print(f'PASS: {means} exact conditional means and {swaps} ordered swaps')


if __name__ == '__main__':
    main()
