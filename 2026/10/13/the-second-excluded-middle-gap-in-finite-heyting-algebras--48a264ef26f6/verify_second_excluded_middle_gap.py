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
        if not ((mask >> x) & 1):
            continue
        for y in range(n):
            if le[x][y] and not ((mask >> y) & 1):
                return False
    return True


def components(le):
    n = len(le)
    seen = [False] * n
    comps = []
    for s in range(n):
        if seen[s]:
            continue
        seen[s] = True
        stack = [s]
        comp = []
        while stack:
            x = stack.pop()
            comp.append(x)
            for y in range(n):
                if y == x:
                    continue
                if (le[x][y] or le[y][x]) and not seen[y]:
                    seen[y] = True
                    stack.append(y)
        comps.append(sorted(comp))
    return comps


def is_chain(comp, le):
    return all(le[x][y] or le[y][x] for x, y in combinations(comp, 2))


checks = 0
total_posets = 0
for n in range(1, 6):
    poset_count = 0
    top_count = 0
    second_count = 0
    full = (1 << n) - 1

    for le in all_posets(n):
        poset_count += 1
        total_posets += 1
        ups = [m for m in range(1 << n) if is_upset(m, le)]
        complemented = [m for m in ups if is_upset(full ^ m, le)]
        comps = components(le)
        ratio = Fraction(len(complemented), len(ups))

        # Center size equals 2^(number of comparability components).
        assert len(complemented) == 2 ** len(comps)
        checks += 1

        nontrivial = [c for c in comps if len(c) > 1]
        top_structure = (
            len(nontrivial) == 1
            and len(nontrivial[0]) == 2
            and is_chain(nontrivial[0], le)
        )
        second_structure = (
            len(nontrivial) == 1
            and len(nontrivial[0]) == 3
            and is_chain(nontrivial[0], le)
        )

        # Recovers the top 2/3 family and then tests the new second gap.
        assert (ratio == Fraction(2, 3)) == top_structure
        checks += 1

        if ratio < 1 and not top_structure:
            assert ratio <= Fraction(1, 2)
        else:
            assert ratio == 1 or top_structure
        checks += 1

        assert (ratio == Fraction(1, 2)) == second_structure
        checks += 1

        top_count += int(top_structure)
        second_count += int(second_structure)

    assert poset_count == EXPECTED_POSETS[n]
    checks += 1
    expected_top = 0 if n == 1 else n * (n - 1)
    assert top_count == expected_top
    checks += 1
    expected_second = 0 if n < 3 else n * (n - 1) * (n - 2)
    assert second_count == expected_second
    checks += 1
    print('n', n, 'posets', poset_count, 'top_cases', top_count, 'second_cases', second_count)

assert total_posets == sum(EXPECTED_POSETS.values())
print('total_posets', total_posets)
print(f'VERIFY_OK {checks} exact assertions')
