"""Independent mod-two boundary-rank check for the SG(4,2) independence complex."""
from collections import defaultdict
from itertools import combinations


def run():
    universe = set(range(10))
    vertices = [frozenset(c) for c in combinations(range(10), 4)
                if all((x + 1) % 10 not in c for x in c)]
    assert len(vertices) == 25
    # Recursive face expansion by index, independently of the other checker's
    # iterative face generator.
    by_size = defaultdict(list)
    by_size[0].append(0)
    def extend(mask, start):
        for j in range(start, len(vertices)):
            if all(vertices[j] & vertices[i] for i in range(j)
                   if mask >> i & 1):
                y = mask | (1 << j)
                by_size[y.bit_count()].append(y)
                extend(y, j + 1)
    extend(0, 0)
    for arr in by_size.values():
        arr.sort()
        assert len(arr) == len(set(arr))
    assert sum(map(len, by_size.values())) == 19907
    ranks = {}
    for size in range(2, max(by_size) + 1):
        rows = {face: pos for pos, face in enumerate(by_size[size - 1])}
        pivots = {}
        for face in by_size[size]:
            col = 0
            for j in range(25):
                if face >> j & 1:
                    col ^= 1 << rows[face ^ (1 << j)]
            while col:
                i = col.bit_length() - 1
                if i in pivots:
                    col ^= pivots[i]
                else:
                    pivots[i] = col
                    break
        ranks[size] = len(pivots)
    # Unreduced homology, using the zero boundary C0 -> 0.
    betti = {size - 1: len(by_size[size]) - ranks.get(size, 0)
             - ranks.get(size + 1, 0) for size in by_size if size}
    assert {d: b for d, b in betti.items() if b} == {0: 1, 3: 1, 4: 2}
    print('VERIFY_HOMOLOGY_OK faces=19907 betti_mod2={0:1,3:1,4:2}')

if __name__ == '__main__':
    run()
