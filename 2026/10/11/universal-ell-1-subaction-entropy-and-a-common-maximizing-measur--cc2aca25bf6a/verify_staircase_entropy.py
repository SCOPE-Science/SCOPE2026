"""Finite checks for staircase restriction of planar additive square systems.

This is an illustration, not a proof for arbitrary uniquely extendable subshifts.
"""
from itertools import product, combinations


def configurations(q, width, height):
    """Every q-ary rectangle satisfying the alternating-square relation."""
    for row in product(range(q), repeat=width):
        for column_tail in product(range(q), repeat=height-1):
            column = (0,) + column_tail
            yield tuple((row[x] + column[y]) % q
                        for y in range(height) for x in range(width))


def staircase(width, height, step_positions):
    """An east/north monotone path between opposite corners."""
    east_indices = set(step_positions)
    x = y = 0
    result = [(x, y)]
    for j in range(width + height - 2):
        if j in east_indices:
            x += 1
        else:
            y += 1
        result.append((x, y))
    assert (x, y) == (width - 1, height - 1)
    return result


def test_staircases(q, max_side):
    verified = 0
    for width in range(1, max_side+1):
        for height in range(1, max_side+1):
            rects = tuple(configurations(q, width, height))
            expected = q ** (width + height - 1)
            assert len(rects) == len(set(rects)) == expected
            all_indices = range(width + height - 2)
            for east_indices in combinations(all_indices, width-1):
                path = staircase(width, height, east_indices)
                idx = [y*width + x for x, y in path]
                restrictions = {tuple(rect[i] for i in idx) for rect in rects}
                assert len(restrictions) == expected, (q, width, height, east_indices)
                verified += 1
    return verified


def test_projection_distinction():
    for n in range(1, 6):
        width = height = n+1
        rects = tuple(configurations(2, width, height))
        straight_diagonal = {tuple(rect[k*width+k] for k in range(width))
                             for rect in rects}
        stair = staircase(width, height, range(n))
        indices = [y*width+x for x,y in stair]
        zigzag_observations = {tuple(rect[i] for i in indices) for rect in rects}
        assert len(straight_diagonal) == 2 ** (n+1)
        assert len(zigzag_observations) == 2 ** (2*n+1)
    return 5


def main():
    tests = test_staircases(2, 5) + test_staircases(3, 4)
    tests += test_projection_distinction()
    print(f"PASS: {tests} exact finite restrictions/counting identities")
    print("Scope: additive square systems over F_2 and F_3, finite rectangles;")
    print("the universal infinite-volume entropy theorem is proved analytically.")

if __name__ == '__main__':
    main()
