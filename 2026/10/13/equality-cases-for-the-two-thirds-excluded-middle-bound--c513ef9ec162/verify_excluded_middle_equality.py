#!/usr/bin/env python3
from itertools import combinations, product
from fractions import Fraction

EXPECTED_POSETS = {1: 1, 2: 3, 3: 19, 4: 219, 5: 4231}


def all_posets(n):
    pairs = list(combinations(range(n), 2))
    for code in product(range(3), repeat=len(pairs)):
        # 0 = incomparable, 1 = i<j, 2 = j<i.
        le = [[False] * n for _ in range(n)]
        for i in range(n):
            le[i][i] = True
        for (i, j), state in zip(pairs, code):
            if state == 1:
                le[i][j] = True
            elif state == 2:
                le[j][i] = True

        transitive = True
        for i in range(n):
            for j in range(n):
                if not le[i][j]:
                    continue
                for k in range(n):
                    if le[j][k] and not le[i][k]:
                        transitive = False
                        break
                if not transitive:
                    break
            if not transitive:
                break
        if transitive:
            yield le


def is_upset(mask, le):
    n = len(le)
    for x in range(n):
        if not (mask >> x) & 1:
            continue
        for y in range(n):
            if le[x][y] and not ((mask >> y) & 1):
                return False
    return True


def comparability_components(le):
    n = len(le)
    seen = [False] * n
    sizes = []
    for s in range(n):
        if seen[s]:
            continue
        seen[s] = True
        stack = [s]
        size = 0
        while stack:
            x = stack.pop()
            size += 1
            for y in range(n):
                if y == x:
                    continue
                comparable = le[x][y] or le[y][x]
                if comparable and not seen[y]:
                    seen[y] = True
                    stack.append(y)
        sizes.append(size)
    return sorted(sizes)


checks = 0
total_posets = 0
for n in range(1, 6):
    poset_count = 0
    equality_count = 0
    full_mask = (1 << n) - 1

    for le in all_posets(n):
        poset_count += 1
        total_posets += 1
        upsets = [m for m in range(1 << n) if is_upset(m, le)]
        complemented = [m for m in upsets if is_upset(full_mask ^ m, le)]

        components = comparability_components(le)
        assert len(complemented) == 2 ** len(components)
        checks += 1

        equality = Fraction(len(complemented), len(upsets)) == Fraction(2, 3)
        expected_structure = n >= 2 and components == [1] * (n - 2) + [2]
        assert equality == expected_structure
        checks += 1

        if equality:
            equality_count += 1

    assert poset_count == EXPECTED_POSETS[n]
    checks += 1
    assert equality_count == (0 if n == 1 else n * (n - 1))
    checks += 1
    print('n', n, 'posets', poset_count, 'equality_cases', equality_count)

assert total_posets == sum(EXPECTED_POSETS.values())
# This final consistency check is deliberately not included in the displayed exact-assertion count.
print('total_posets', total_posets)
print(f'VERIFY_OK {checks} exact assertions')
