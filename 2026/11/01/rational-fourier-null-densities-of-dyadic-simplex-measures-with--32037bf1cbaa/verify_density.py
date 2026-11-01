"""Exact checks for the Fourier-null density of dyadic simplex measures.

Only Python's standard library is required.  The infinite probability
calculation is justified separately by the finite-state proof.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import product
from math import comb


def distribution(state):
    """Immediate-hit probability and live even-partition transition mass."""
    state = tuple(sorted(state))
    hit = Fraction(1)
    for s in state:
        hit *= Fraction(comb(s, s // 2), 2**s)
    live = {}
    for choices in product(*(range(0, s + 1, 2) for s in state)):
        if all(a * 2 == s for a, s in zip(choices, state)):
            continue
        weight = Fraction(1)
        for a, s in zip(choices, state):
            weight *= Fraction(comb(s, a), 2**s)
        children = tuple(sorted(y for a, s in zip(choices, state)
                                for y in (a, s - a) if y))
        live[children] = live.get(children, Fraction(0)) + weight
    assert hit + sum(live.values()) <= 1
    return hit, {k: v for k, v in live.items() if v}


@lru_cache(None)
def eventual(state):
    hit, live = distribution(state)
    self_weight = live.pop(state, Fraction(0))
    total = hit + sum(w * eventual(child) for child, w in live.items())
    return total / (1 - self_weight)


def is_zero_at_level(residues, j):
    size = 1 << j
    counts = [0] * size
    for x in residues:
        counts[x % size] += 1
    return all(counts[a] == counts[a + size // 2]
               for a in range(size // 2))


def finite_census(level):
    modulus = 1 << level
    out = [0] * level
    for frequency in product(range(modulus), repeat=7):
        residues = (0,) + frequency
        for j in range(1, level + 1):
            if is_zero_at_level(residues, j):
                out[j - 1] += 1
                break
    return out


def main():
    A, B, D, E = (8,), (2, 6), (2, 2, 4), (2, 2, 2, 2)
    expected = {
        A: (Fraction(35, 128), {A: Fraction(1, 128), B: Fraction(7, 32)}),
        B: (Fraction(5, 32), {B: Fraction(1, 64), D: Fraction(15, 64)}),
        D: (Fraction(3, 32), {D: Fraction(1, 32), E: Fraction(3, 32)}),
        E: (Fraction(1, 16), {E: Fraction(1, 16)}),
    }
    for state, rhs in expected.items():
        assert distribution(state) == rhs, (state, distribution(state))
    assert eventual(E) == Fraction(1, 15)
    assert eventual(D) == Fraction(16, 155)
    assert eventual(B) == Fraction(358, 1953)
    assert eventual(A) == Fraction(11197, 35433)
    assert eventual((2,)) == 1
    assert eventual((4,)) == Fraction(3, 7)
    assert finite_census(1) == [35]
    assert finite_census(2) == [4480, 595]
    states = {A: Fraction(1)}
    first = []
    for level in range(1, 5):
        first.append(sum(p * expected[s][0] for s, p in states.items()))
        nxt = {}
        for s, p in states.items():
            for child, w in expected[s][1].items():
                nxt[child] = nxt.get(child, Fraction(0)) + p * w
        states = nxt
    assert first == [Fraction(35, 128), Fraction(595, 16384),
                     Fraction(11795, 2097152), Fraction(155155, 268435456)]
    assert sum(first[:2]) == Fraction(5075, 16384)
    print('DYADIC_EIGHT_ATOM_NULL_DENSITY_OK',
          'rational=' + str(eventual(A)),
          'L1=35/128 L2=5075/16384')


if __name__ == '__main__':
    main()
