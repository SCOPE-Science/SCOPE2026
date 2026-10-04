#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter
from random import Random


def image_set(n, f, S):
    return {f[x] for x in S}


def rotate_set(n, S, k):
    return {(x + k) % n for x in S}


def apply_word(n, f, word):
    S = set(range(n))
    for letter, exponent in word:
        if letter == 'a':
            S = rotate_set(n, S, exponent % n)
        elif letter == 'b':
            for _ in range(exponent):
                S = image_set(n, f, S)
        else:
            raise ValueError(letter)
    return S


def defect_one_data(n, f):
    counts = Counter(f)
    image = set(f)
    if len(image) != n - 1:
        return None
    e = next(iter(set(range(n)) - image))
    d = next(y for y, c in counts.items() if c == 2)
    kernel = tuple(x for x in range(n) if f[x] == d)
    assert len(kernel) == 2
    return e, d, kernel


def theorem_predicts_two_b(n, e, d, x, y):
    delta = (y - x) % n
    rho = (d - e) % n
    return delta != rho or (-delta) % n != rho


def explicit_witness(n, f, e, d, kernel, x, y):
    # Try both orientations of the target hole pair.
    rho = (d - e) % n
    for first, second in ((x, y), (y, x)):
        t = (second - first) % n
        if t == rho:
            continue
        # f maps Q\kernel bijectively onto Q\{e,d}.
        desired = (e + t) % n
        candidates = [h for h in range(n) if h not in kernel and f[h] == desired]
        assert len(candidates) == 1
        h = candidates[0]
        k = (h - e) % n
        j = (first - e) % n
        word = [('b', 1), ('a', k), ('b', 1), ('a', j)]
        out = apply_word(n, f, word)
        target = set(range(n)) - {x, y}
        assert out == target, (n, f, e, d, kernel, x, y, word, out, target)
        length = 2 + k + j
        assert length <= 2 * n
        return word, length
    return None


def two_b_reachable_by_enumeration(n, f):
    reachable = set()
    for k in range(n):
        for j in range(n):
            out = apply_word(n, f, [('b', 1), ('a', k), ('b', 1), ('a', j)])
            if len(out) == n - 2:
                holes = tuple(sorted(set(range(n)) - out))
                reachable.add(holes)
    return reachable


def check_map(n, f):
    dat = defect_one_data(n, f)
    assert dat is not None
    e, d, kernel = dat
    actual = two_b_reachable_by_enumeration(n, f)
    for x, y in combinations(range(n), 2):
        predicted = theorem_predicts_two_b(n, e, d, x, y)
        assert ((x, y) in actual) == predicted, (n, f, e, d, x, y, predicted, actual)
        witness = explicit_witness(n, f, e, d, kernel, x, y)
        assert (witness is not None) == predicted
    rho = (d - e) % n
    expected_missing = set()
    if n % 2 == 0 and rho == n // 2:
        expected_missing = {tuple(sorted((x, (x + n // 2) % n))) for x in range(n)}
    all_pairs = set(combinations(range(n), 2))
    assert all_pairs - actual == expected_missing
    return len(actual), len(expected_missing)


def exhaustive(n):
    maps = checked = 0
    min_reach = 10**9
    max_missing = 0
    for f in product(range(n), repeat=n):
        if len(set(f)) != n - 1:
            continue
        maps += 1
        reach, missing = check_map(n, f)
        checked += 1
        min_reach = min(min_reach, reach)
        max_missing = max(max_missing, missing)
    return maps, checked, min_reach, max_missing


def random_defect_one_map(n, rng):
    e = rng.randrange(n)
    d = rng.choice([x for x in range(n) if x != e])
    kernel = rng.sample(range(n), 2)
    rest_states = [x for x in range(n) if x not in kernel]
    rest_images = [x for x in range(n) if x not in (e, d)]
    rng.shuffle(rest_images)
    f = [None] * n
    for x in kernel:
        f[x] = d
    for x, y in zip(rest_states, rest_images):
        f[x] = y
    return tuple(f)


def main():
    print('THEOREM_CHECK two-defect cyclic defect-one reachability')
    print('Exhaustive rank-(n-1) maps:')
    for n in range(3, 8):
        maps, checked, min_reach, max_missing = exhaustive(n)
        print(f'n={n}: maps={maps}, checked={checked}, min_two_b_pairs={min_reach}/{n*(n-1)//2}, max_missing={max_missing}')
    rng = Random(20261001)
    print('Deterministic random checks:')
    for n in range(8, 14):
        cases = 200
        exceptional = 0
        for _ in range(cases):
            f = random_defect_one_map(n, rng)
            e, d, _ = defect_one_data(n, f)
            if n % 2 == 0 and (d - e) % n == n // 2:
                exceptional += 1
            check_map(n, f)
        print(f'n={n}: cases={cases}, antipodal-displacement-cases={exceptional}')
    print('VERIFY_OK')

if __name__ == '__main__':
    main()
