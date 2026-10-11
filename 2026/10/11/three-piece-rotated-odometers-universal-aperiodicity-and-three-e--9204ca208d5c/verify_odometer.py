"""Exact cell-graph verification for three-piece rotated odometers.

The proof of aperiodicity uses a renormalization argument in the accompanying text;
this checker verifies all finite graph identities on which that argument rests.
No finite orbit search is used as a substitute for the infinite argument.
"""
from fractions import Fraction
from itertools import permutations

# One-line notation for permutations of {0,1,2}.
EXPECTED = {
    (0, 1, 2): ((0, 1, 2), (4, 4, 4)),
    (0, 2, 1): ((1, 2, 0), (2, 2, 8)),
    (1, 0, 2): ((1, 2, 0), (2, 2, 8)),
    (1, 2, 0): ((1, 2, 0), (4, 4, 4)),
    (2, 0, 1): ((2, 0, 1), (10, 1, 1)),
    (2, 1, 0): ((2, 0, 1), (10, 1, 1)),
}


def adic(x):
    assert Fraction(0) <= x < 1
    n = 1
    while x >= 1 - Fraction(1, 2**n):
        n += 1
    return x - 1 + Fraction(3, 2**n)


def full_map(x, pi):
    i = int(3*x)
    return adic(x + Fraction(pi[i]-i, 3))


def finite_transition(j, pi):
    """One step on the 1/12-grid before entering the high-branch gate."""
    permuted = 4*pi[j//4] + j%4
    if permuted >= 9:
        return None, permuted-9
    if permuted < 6:
        return permuted+6, None
    return permuted-3, None


def trace(j, pi):
    cells = []
    while True:
        assert j not in cells, 'closed finite cell loop outside high gate'
        cells.append(j)
        to_cell, terminal = finite_transition(j, pi)
        if terminal is not None:
            return cells, terminal
        j = to_cell


def verify():
    assert len(EXPECTED) == 6
    for pi in permutations((0,1,2)):
        traces = [trace(i, pi) for i in range(3)]
        renormalized = tuple(last for cells,last in traces)
        heights = tuple(len(cells) for cells,last in traces)
        assert (renormalized, heights) == EXPECTED[pi]
        assert sorted(cell for cells,last in traces for cell in cells) == list(range(12))
        assert set(renormalized) == {0,1,2}
        for j, (cells, last) in enumerate(traces):
            for offset in (Fraction(1,120), Fraction(1,72), Fraction(1,60)):
                x = Fraction(j,12) + offset
                y = x
                for cell in cells:
                    assert int(12*y) == cell
                    y = full_map(y, pi)
                assert 0 < y < Fraction(1,4)
                w = Fraction(last, 12) + offset
                assert y == adic(4*w)/4
                # First-return image is the scaled rotated odometer.
                pi1 = renormalized
                rhs = adic(4*(x + Fraction(pi1[j]-j,12)))/4
                assert y == rhs
        print('pi=', pi, '  renormalized=', renormalized,
              '  return_heights=', heights)
    # Contrasting two-piece example (not asserted for q=3):
    for x in (Fraction(1,2), Fraction(5,8), Fraction(7,8)):
        rotated = x - Fraction(1,2)
        assert adic(rotated) == x
    print('EXACT_CELL_GRAPH_OK')


if __name__ == '__main__':
    verify()
