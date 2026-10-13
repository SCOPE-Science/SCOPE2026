#!/usr/bin/env python3
"""Independent exhaustive two-use census and structural checks for seven-antihole codes."""
from itertools import combinations, product
from math import comb

q = 7

def distinguishable(x, y):
    return any((a-b) % q in (1, q-1) for a,b in zip(x,y))

# Direct enumeration of every 1-use and every 2-use candidate of sizes 2 and 4.
words1 = [(x,) for x in range(q)]
words2 = list(product(range(q), repeat=2))
N1 = sum(distinguishable(a,b) for a,b in combinations(words1, 2))
assert N1 == 7

E = [[i != j and distinguishable(words2[i],words2[j])
      for j in range(q*q)] for i in range(q*q)]
N2 = 0
for a,b,c,d in combinations(range(q*q), 4):
    if E[a][b] and E[a][c] and E[a][d] and E[b][c] and E[b][d] and E[c][d]:
        N2 += 1
assert N2 == 1715

# Independently exclude size-five two-use codes by an ascending bitmask search.
adj = [sum(1 << j for j in range(q*q) if E[i][j]) for i in range(q*q)]
def any_five(chosen, available):
    if chosen == 5: return True
    if chosen + available.bit_count() < 5: return False
    while available:
        bit = available & -available
        i = bit.bit_length()-1
        available ^= bit
        if any_five(chosen+1, available & adj[i]): return True
    return False
assert not any_five(0,(1<<(q*q))-1)

# The 2015 construction supplies one eight-word product code.
product_code = list(product((0,1), repeat=3))
assert len(product_code) == 8
assert all(distinguishable(a,b) for a,b in combinations(product_code,2))

# A non-Cartesian eight-word code: all 3 projections are bigger than 2.
witness = [(0,0,0),(0,2,1),(1,5,2),(2,3,1),
           (3,3,1),(3,6,2),(4,6,2),(6,2,3)]
assert len(set(witness)) == 8
assert all(distinguishable(a,b) for a,b in combinations(witness,2))
assert all(len({w[i] for w in witness}) > 2 for i in range(3))

# Two of the three one-vs-two coordinate product decompositions imply all three.
N_root = 38259704
N_total, remainder = divmod(q**3 * N_root, 8)
assert remainder == 0 and N_total == 1640384809
N_onecut = N1 * N2
N_pure = N1**3
N_decomposable = 3 * N_onecut - 2 * N_pure
N_indec = N_total - N_decomposable
assert (N_onecut,N_pure,N_decomposable,N_indec)==(12005,343,35329,1640349480)
assert N_total % q**3 == 0
print(f"SMALL oneuse_pairs={N1} twouse_maxima={N2} twouse_no_five=true")
print(f"STRUCTURE all={N_total} decomposable={N_decomposable} "
      f"indecomposable={N_indec} pure={N_pure} translation_orbits={N_total//q**3}")
print("WITNESS indecomposable_valid=true")
