"""Independent exact-arithmetic finite checks for the finite-population gap-product theorem.

These checks test the identities and sample cases; the theorem for all k and real gaps
is established by the accompanying mathematical proof, not by enumeration.
"""
from fractions import Fraction
from itertools import combinations, product
from math import prod


def direct(gaps):
    k = len(gaps)
    positions = [Fraction(0)]
    for gap in gaps:
        positions.append(positions[-1] + gap)
    numer = Fraction(0)
    denom = Fraction(0)
    for chosen in combinations(range(k + 1), k):
        weight = prod(positions[chosen[j + 1]] - positions[chosen[j]]
                      for j in range(k - 1))
        omitted = next(i for i in range(k + 1) if i not in chosen)
        cost = min(abs(positions[omitted] - positions[j]) for j in chosen)
        numer += weight * cost
        denom += weight
    return numer / denom


def formula(gaps):
    k = len(gaps)
    numer = k + 1 + sum(min(gaps[i], gaps[i+1]) / max(gaps[i], gaps[i+1])
                        for i in range(k - 1))
    return numer / (2 * sum(Fraction(1, 1) / g for g in gaps))


def optimality_condition(gaps):
    m = min(gaps)
    return (gaps[0] == m and gaps[-1] == m
            and all(gaps[i] == m or gaps[i + 1] == m
                    for i in range(len(gaps) - 1)))


def main():
    count = 0
    for k in range(2, 7):
        for ints in product(range(1, 5), repeat=k):
            gaps = tuple(Fraction(t) for t in ints)
            expected = direct(gaps)
            closed = formula(gaps)
            opt = min(gaps)
            assert expected == closed, (k, ints, expected, closed)
            assert expected >= opt, (k, ints)
            assert 2 * expected < (2*k - 1) * opt, (k, ints)
            assert (expected == opt) == optimality_condition(gaps), (k, ints)
            count += 4
        for T in [2, 5, 20, 100]:
            gaps = (Fraction(1),) + (Fraction(T),) * (k - 1)
            got = formula(gaps) / min(gaps)
            exact = Fraction((2*k - 1)*T + 1, 2*(T + k - 1))
            assert got == exact, (k, T, got, exact)
            count += 1
    print(f'PASS: {count} exact-rational assertions; k=2..6, integer gaps 1..4; sharp families T=2,5,20,100.')

if __name__ == '__main__':
    main()
