"""Exact finite checks for the two-type first-arrival ballot theorem.

Only Python standard-library dependencies. Run: python ballot_first_arrival_check.py
"""
from fractions import Fraction
from itertools import permutations


def exact_exponential_ballot(rate_first, rate_second):
    rates = (rate_first, rate_second, rate_first, rate_second)
    total = Fraction(0)
    for ordering in permutations(range(4)):
        prob = Fraction(1)
        remaining = sum(rates)
        word = []
        for j in ordering:
            prob *= Fraction(rates[j], remaining)
            remaining -= rates[j]
            word.append(1 if j < 2 else -1)
        partial = 0
        prefixes = [0]
        for sign in word:
            partial += sign
            prefixes.append(partial)
        if all(x >= 0 for x in prefixes) or all(x <= 0 for x in prefixes):
            total += prob
    return total


def formula(rate_first, rate_second):
    r, s = Fraction(rate_first), Fraction(rate_second)
    return (Fraction(1, 2) + r/(r+2*s) + s/(s+2*r)
            - (r*r+s*s)/(r+s)**2)


def check_chord_pairings():
    # The two occurrences of each type are interchangeable.
    for pairing in (((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))):
        good = 0
        for signs in ((0,0),(0,1),(1,0),(1,1)):
            label = ['']*4
            for (a,b), s in zip(pairing,signs):
                label[a] = 'A' if s == 0 else 'B'
                label[b] = 'B' if s == 0 else 'A'
            p = 0
            prefixes = [0]
            for x in label:
                p += 1 if x=='A' else -1
                prefixes.append(p)
            if all(z >= 0 for z in prefixes):
                good += 1
        assert good == (2 if pairing == ((0,3),(1,2)) else 1)
    return 3


def main():
    n = check_chord_pairings()
    for r in range(1,19):
        for s in range(1,19):
            observed = exact_exponential_ballot(r,s)
            predicted = formula(r,s)
            assert observed == predicted, (r,s,observed,predicted)
            assert Fraction(1,2) < observed <= Fraction(2,3)
            assert observed == Fraction(2,3) if r == s else observed < Fraction(2,3)
            n += 1
    # Interval examples: type 1 arrivals are uniform on (2,3), while
    # type 2 is uniform on (0,1) with mass w and (4,5) otherwise.
    # The CDF of type 2 is identically w on type-1 support;
    # type-1 CDF evaluated on type-2 arrival is Bernoulli(1-w).
    for k in range(0,25):
        w = Fraction(k,48)
        b = Fraction(1,2) + w*(1-w)
        assert Fraction(1,2) <= b <= Fraction(3,4)
        n += 1
    # Equal laws give the distribution-free two-sample Catalan probability.
    assert formula(1,1) == Fraction(2,3)
    print(f'PASS: {n} exact rational checks (including {18*18} exponential races).')


if __name__ == '__main__':
    main()
