#!/usr/bin/env python3
"""Independent finite certificate for a weighted two-deletion shadow converse.

The mathematical reduction from disjoint shadows to the bound is described in
RESULT.md; this program verifies the complete equality-pattern lemma and
cross-checks the alphabet-weight identity by direct enumeration.
"""
from itertools import combinations, product
from collections import defaultdict

WEIGHT = {(0, 0, 0): 22, (0, 0, 1): 5, (0, 1, 0): 3,
          (0, 1, 1): 8, (0, 1, 2): 3}

def canonical(word):
    names = {}
    return tuple(names.setdefault(a, len(names)) for a in word)

def shadow(word):
    return {tuple(word[i] for i in positions)
            for positions in combinations(range(len(word)), 3)}

def shadow_weight(word):
    return sum(WEIGHT[canonical(s)] for s in shadow(word))

def main():
    pats = [x for x in product(range(5), repeat=5) if canonical(x) == x]
    assert len(pats) == 52
    stats = defaultdict(list)
    for word in pats:
        same = word[0] == word[1]
        value = shadow_weight(word)
        stats[(same, len(set(word)))].append(value)
        assert value >= (22 if same else 30), (word, value)
    expected = {
        (True, 1): (1, 22, 22), (True, 2): (7, 27, 43),
        (True, 3): (6, 26, 44), (True, 4): (1, 27, 27),
        (False, 2): (8, 30, 54), (False, 3): (19, 30, 50),
        (False, 4): (9, 30, 37), (False, 5): (1, 30, 30),
    }
    assert set(stats) == set(expected)
    for group, (count, minimum, maximum) in expected.items():
        vals = stats[group]
        assert (len(vals), min(vals), max(vals)) == (count, minimum, maximum)
    assert sum(len(v) for (same, _), v in stats.items() if same) == 15
    assert sum(len(v) for (same, _), v in stats.items() if not same) == 37
    print('Exhaustive canonical five-letter equality patterns: 52; all inequalities PASS')
    print('first-two-equal | distinct-symbols | patterns | min weight | max weight')
    for (same, count), vals in sorted(stats.items(), key=lambda t:(not t[0][0],t[0][1])):
        print(f'{str(same):>15} | {count:>16} | {len(vals):>8} | {min(vals):>10} | {max(vals):>10}')
    assert min(shadow_weight(w) for w in pats if w[0]==w[1]) == 22
    assert min(shadow_weight(w) for w in pats if w[0]!=w[1]) == 30

    # Independent alphabet-by-alphabet checks against actual words, not just types.
    # At q=7 there are 16,807 length-five words and 343 length-three words.
    for q in range(2, 8):
        total = sum(WEIGHT[canonical(word)] for word in product(range(q), repeat=3))
        formula = q * (3*q*q + 7*q + 12)
        assert total == formula, (q, total, formula)
        observed = [10**9, 10**9]
        for word in product(range(q), repeat=5):
            val = shadow_weight(word)
            equal = int(word[0]==word[1])
            observed[equal] = min(observed[equal], val)
            assert val >= (22 if equal else 30)
        required = 22*q + 30*q*(q-1)
        gap = required - total
        assert gap == q*(q-1)*(20-3*q)
        assert (gap > 0) == (q <= 6)
        print(f'q={q}: tested={q**5:>5} length-five words; '
              f'min(equal)={observed[1]}; min(distinct)={observed[0]}; '
              f'available={total}; mandatory={required}; excess={gap}')
    print('The universal capacity inequality excludes q=2,3,4,5,6: PASS')
    print('No claim of existence at q=7 or above is made.')

if __name__ == '__main__':
    main()
