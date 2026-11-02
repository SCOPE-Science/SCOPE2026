"""Independent direct-sum verification of the 120 labeled double-Fano codebooks.
Run: python3 verify_orbit.py. Uses only the Python standard library.
"""
from itertools import combinations, permutations

N = 7
W = tuple(combinations(range(N), 3))
cyclic = {tuple(sorted(((s % 7), ((s + b) % 7), ((s + 3) % 7))))
          for s in range(N) for b in (1, 2)}
assert len(cyclic) == 14

def signature(pair):
    return tuple(sum(i in a for a in pair) for i in range(N))

def b2(code):
    values = [signature(pair) for pair in combinations(code, 2)]
    return len(values) == len(set(values))

def balanced(code):
    return all(sum({i, j}.issubset(t) for t in code) == 2
               for i, j in combinations(range(N), 2))

orbit = set()
for perm in permutations(range(N)):
    translated = frozenset(tuple(sorted(perm[i] for i in t)) for t in cyclic)
    orbit.add(translated)
assert len(orbit) == 120
assert all(len(code) == 14 and b2(code) and balanced(code) for code in orbit)
print('VERIFY_ORBIT_OK labeled=120 all_sum_unique=1 all_pair_incidence_two=1')
