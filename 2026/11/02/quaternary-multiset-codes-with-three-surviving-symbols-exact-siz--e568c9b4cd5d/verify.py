"""Exact verification of four-symbol multiset codes with three retained tokens.

Run with Python 3 standard library. All candidate multiplicity vectors are
listed in lexicographic order and each complete code is counted only once.
"""
from itertools import combinations, permutations, product
from collections import Counter, defaultdict
from math import comb

EXPECTED = {
    5: (6, 288, 14),
    6: (5, 708, 46),
    7: (5, 16, 2),
    8: (5, 1, 1),
}

def vectors(n, q=4):
    if q == 1:
        yield (n,)
        return
    for a in range(n + 1):
        for b in vectors(n - a, q - 1):
            yield (a,) + b

def intersection(x, y):
    return sum(min(a, b) for a, b in zip(x, y))

def compatible(x, y):
    return intersection(x, y) <= 2

def code_valid(code):
    return all(compatible(x, y) for x, y in combinations(code, 2))

def all_maxima_graph(n, size):
    words = list(vectors(n))
    masks = []
    for i, x in enumerate(words):
        mask = 0
        for j in range(i + 1, len(words)):
            if compatible(x, words[j]):
                mask |= 1 << j
        masks.append(mask)
    results = []
    def extend(selected, choices):
        need = size - len(selected)
        if need == 0:
            results.append(frozenset(words[i] for i in selected))
            return
        while choices.bit_count() >= need:
            singleton = choices & -choices
            i = singleton.bit_length() - 1
            choices ^= singleton
            extend(selected + (i,), choices & masks[i])
    extend((), (1 << len(words)) - 1)
    assert len(results) == len(set(results))
    return results

def count_by_heavy_and_exception(n):
    words = list(vectors(n))
    exceptional = [x for x in words if max(x) <= 2]
    exception_sets = ([e for e in combinations(exceptional, 2) if compatible(*e)]
                      if n == 5 else [(e,) for e in exceptional])
    heavy_by_symbol = [[x for x in words if x[a] >= 3 and
                        sum(y >= 3 for y in x) == 1] for a in range(4)]
    count = 0
    kinds = Counter()
    for e in exception_sets:
        pools = [[x for x in heavy_by_symbol[a] if all(compatible(x, z) for z in e)]
                 for a in range(4)]
        for four in product(*pools):
            if code_valid(four):
                count += 1
                kinds[tuple(sorted((tuple(sorted(x, reverse=True)) for x in e)))] += 1
    return count, kinds

def cycle_type(perm):
    visited = set()
    sizes = []
    for j in range(4):
        if j not in visited:
            cur, count = j, 0
            while cur not in visited:
                visited.add(cur)
                cur = perm[cur]
                count += 1
            sizes.append(count)
    return tuple(sorted(sizes, reverse=True))

def permute_code(code, perm):
    return frozenset(tuple(x[i] for i in perm) for x in code)

def check_three_shadows(n):
    words = list(vectors(n))
    three = list(vectors(3))
    shadows = [frozenset(r for r in three if all(r[i] <= x[i] for i in range(4)))
               for x in words]
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            assert (not (shadows[i] & shadows[j])) == compatible(words[i], words[j])


def main():
    group = list(permutations(range(4)))
    for n, (optimum, expected_count, expected_orbits) in EXPECTED.items():
        assert len(list(vectors(n))) == comb(n + 3, 3)
        check_three_shadows(n)
        maxima = all_maxima_graph(n, optimum)
        assert len(maxima) == expected_count
        assert all(len(c) == optimum and code_valid(c) for c in maxima)
        direct_count, kinds = count_by_heavy_and_exception(n)
        assert direct_count == expected_count
        fixed = defaultdict(list)
        for p in group:
            f = sum(permute_code(c, p) == c for c in maxima)
            fixed[cycle_type(p)].append(f)
        assert all(len(set(fs)) == 1 for fs in fixed.values())
        total_fixed = sum(sum(fs) for fs in fixed.values())
        assert total_fixed % 24 == 0
        orbit_count = total_fixed // 24
        assert orbit_count == expected_orbits
        if n == 5:
            assert kinds == {((2, 2, 1, 0), (2, 2, 1, 0)): 288}
        if n == 6:
            assert kinds == {((2, 2, 2, 0),): 576, ((2, 2, 1, 1),): 132}
        print('length=', n, 'max_code_size=', optimum,
              'labeled_optima=', expected_count, 'permutation_orbits=', orbit_count,
              'fixed_by_cycle=', sorted((str(k), len(fs), fs[0]) for k, fs in fixed.items()))
    for n in range(9, 18):
        # Every word has a coordinate at least 3, so the heavy-coordinate
        # injection yields a four-codeword upper bound. Constant vectors attain it.
        assert all(max(x) >= 3 for x in vectors(n))
        constants = [tuple(n if j == i else 0 for j in range(4)) for i in range(4)]
        assert code_valid(constants)
    print('QUATERNARY_THREE_SURVIVOR_VERIFICATION_OK')

if __name__ == '__main__':
    main()
