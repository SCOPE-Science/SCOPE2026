"""Exact arithmetic checks for a finite-gap binary carry distribution theorem."""
from fractions import Fraction
from itertools import product
from math import comb


def carry_distribution(t, r):
    """Probabilities for at most r carries, with the infinite bit tail resolved exactly."""
    current = {(0, 0): Fraction(1)}
    for i in range(t.bit_length()):
        new = {}
        bit = (t >> i) & 1
        for (oldcarry, count), probability in current.items():
            for inputbit in (0, 1):
                outgoing = (inputbit + bit + oldcarry) // 2
                nextcount = count + outgoing
                if nextcount <= r:
                    state = (outgoing, nextcount)
                    new[state] = new.get(state, Fraction(0)) + probability / 2
        current = new
    result = [Fraction(0) for _ in range(r + 1)]
    for (carry, count), probability in current.items():
        if carry == 0:
            result[count] += probability
        else:
            for extra in range(r - count + 1):
                result[count + extra] += probability / (2 ** (extra + 1))
    return result


def predicted(r, boundary):
    result = [Fraction(comb(r + k - 1, k), 2 ** (r + k)) for k in range(r + 1)]
    result[r] -= Fraction(boundary, 2 ** (2 * r))
    return result


def check():
    cases = 0
    for r in range(1, 9):
        for variant in range(18):
            gaps = [r + ((variant * (j + 3) + 7 * j + j*j) % 5) for j in range(r - 1)]
            positions = [variant % 3]
            for g in gaps:
                positions.append(positions[-1] + g)
            t = sum(1 << pos for pos in positions)
            assert carry_distribution(t, r) == predicted(r, gaps.count(r)), (r, gaps)
            cases += 1
    # More thorough boundary testing for small ranks.
    for r in range(2, 6):
        for gaps in product(range(r, r + 3), repeat=r - 1):
            positions = [0]
            for g in gaps:
                positions.append(positions[-1] + g)
            t = sum(1 << pos for pos in positions)
            assert carry_distribution(t, r) == predicted(r, gaps.count(r)), (r, gaps)
            cases += 1
    # A distinct finite dyadic check, taking enough low bits for exact density.
    for r, gaps in [(2, (2,)), (2, (3,)), (3, (3,3)), (3, (3,4)), (3, (4,4)), (4, (4,4,4))]:
        positions = [0]
        for g in gaps:
            positions.append(positions[-1] + g)
        t = sum(1 << pos for pos in positions)
        length = positions[-1] + r + 4
        if length > 18:
            continue
        count = sum((n+t).bit_count() >= n.bit_count() for n in range(1 << length))
        assert Fraction(count, 1 << length) == sum(predicted(r, gaps.count(r))), (r, gaps)
    print('VERIFY_OK', cases, 'exact Markov distribution tests; finite dyadic checks passed')


if __name__ == '__main__':
    check()
