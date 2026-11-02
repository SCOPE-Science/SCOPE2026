#!/usr/bin/env python3
"""Independent base-radix profile traversal with edge-wise welfare and rank counts."""
from collections import defaultdict
from itertools import permutations
from fractions import Fraction

PERMS = tuple(permutations((0, 1, 2)))
RANKS = tuple(tuple(p.index(target) for target in range(3)) for p in PERMS)
OBS = defaultdict(int)
RELATIONS = defaultdict(int)
for index in range(6**6):
    value = index
    digits = []
    for _ in range(6):
        digits.append(value % 6)
        value //= 6
    men = [RANKS[k] for k in digits[:3]]
    women = [RANKS[k] for k in digits[3:]]
    # Scores factor as independent contributions of selected edges.
    gains = [[(3-men[m][w]) * (3-women[w][m]) for w in range(3)] for m in range(3)]
    rankcounts = [[(int(men[m][w] == 0) + int(women[w][m] == 0),
                    int(men[m][w] == 1) + int(women[w][m] == 1),
                    int(men[m][w] == 2) + int(women[w][m] == 2))
                   for w in range(3)] for m in range(3)]
    stable = {}
    for matching in PERMS:
        is_stable = True
        for m in range(3):
            for w in range(3):
                if w == matching[m]:
                    continue
                woman_current = matching.index(w)
                if men[m][w] < men[m][matching[m]] and women[w][m] < women[w][woman_current]:
                    is_stable = False
                    break
            if not is_stable:
                break
        if not is_stable:
            continue
        v = tuple(sum(rankcounts[m][matching[m]][t] for m in range(3)) for t in range(3))
        prod = gains[0][matching[0]] * gains[1][matching[1]] * gains[2][matching[2]]
        stable[matching] = (v, prod)
    assert stable
    best_lex = max(z[0] for z in stable.values())
    best_nash = max(z[1] for z in stable.values())
    rank_solutions = {a for a in stable if stable[a][0] == best_lex}
    welfare_of_lex = {stable[a][1] for a in rank_solutions}
    assert len(welfare_of_lex) == 1
    welfare_ratio = Fraction(best_nash, welfare_of_lex.pop())
    OBS[welfare_ratio] += 1
    nash_solutions = {a for a in stable if stable[a][1] == best_nash}
    RELATIONS['coinciding' if nash_solutions == rank_solutions else
              'disjoint' if not nash_solutions.intersection(rank_solutions) else
              'overlapping_distinct'] += 1
assert OBS == {Fraction(1):42756, Fraction(4,3):2484, Fraction(16,9):432,
               Fraction(64,27):12, Fraction(8,3):828, Fraction(32,9):72,
               Fraction(16,3):72}, OBS
assert RELATIONS == {'coinciding': 42756, 'disjoint': 3900}, RELATIONS
print('VERIFIED by independent edge-product/base-six enumeration:')
print('ratios:', [(str(k),v) for k,v in sorted(OBS.items())])
print('optimizer relationships:',dict(RELATIONS))
