"""Independent incidence-multiset count for all six-vertex 3-list assignments.

A color is identified, up to palette renaming, by its nonempty subset of
vertices on whose three-element lists it occurs. The multiplicities of
these 63 possible subsets sum to three at every vertex.
"""
from functools import lru_cache

N = 6
SUPPORTS = tuple(range(1, 1 << N))

@lru_cache(maxsize=None)
def count(i, residual):
    if i == len(SUPPORTS):
        return int(all(x == 0 for x in residual))
    support = SUPPORTS[i]
    vertices = tuple(v for v in range(N) if support & (1 << v))
    max_number = min(residual[v] for v in vertices)
    result = 0
    for copies in range(max_number + 1):
        remaining = list(residual)
        for v in vertices:
            remaining[v] -= copies
        result += count(i + 1, tuple(remaining))
    return result

if __name__ == '__main__':
    total = count(0, (3,) * N)
    assert total == 2_406_208, total
    print('INDEPENDENT_SUPPORT_COUNT_OK', total)
