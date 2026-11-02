"""Exact small-instance checks for the PAV exchange-locality boundary.
Run with Python 3.10+ and no third-party dependencies.
"""
from fractions import Fraction
from itertools import product


def harmonic(k):
    return sum((Fraction(1, t) for t in range(1, k+1)), Fraction(0))


def allocations(m, k):
    if m == 1:
        yield (k,)
        return
    for x in range(k+1):
        for rest in allocations(m-1, k-x):
            yield (x,) + rest


def pav(seats, counts):
    return sum((multiplicity * harmonic(sum(seats[j] for j in range(len(seats)) if mask & (1 << j)))
                for mask, multiplicity in enumerate(counts) if multiplicity), Fraction(0))


def is_local(seats, counts):
    score = pav(seats, counts)
    for i, x in enumerate(seats):
        if not x:
            continue
        for j in range(len(seats)):
            if j == i:
                continue
            nxt = list(seats)
            nxt[i] -= 1
            nxt[j] += 1
            if pav(nxt, counts) > score:
                return False
    return True


def test_three_party():
    checked = 0
    for num_parties in range(1, 4):
        for counts_bits in product((0, 1), repeat=(1 << num_parties) - 1):
            counts = (0,) + counts_bits
            for k in range(1, 7):
                cases = list(allocations(num_parties, k))
                values = [pav(z, counts) for z in cases]
                optimum = max(values)
                for seats, val in zip(cases, values):
                    if is_local(seats, counts):
                        assert val == optimum, (num_parties, counts, k, seats, val, optimum)
                    checked += 1
    return checked


def test_prior_four_party_obstruction():
    # Gölz--Yaghoubizade (2026), Example B.3 (previously published).
    ballots = [{0, 2}, {0, 3}, {1, 2, 3}, {1}]
    counts = [0] * 16
    for ballot in ballots:
        counts[sum(1 << j for j in ballot)] += 1
    x = (0, 0, 1, 1)
    y = (1, 1, 0, 0)
    assert is_local(x, counts)
    assert pav(y, counts) > pav(x, counts)
    assert pav(y, counts) == max(pav(z, counts) for z in allocations(4, 2))
    return pav(x, counts), pav(y, counts)


if __name__ == '__main__':
    checked = test_three_party()
    a, b = test_prior_four_party_obstruction()
    print(f'VERIFY_OK three_party_cases={checked} known_four_party_local={a} global={b}')
