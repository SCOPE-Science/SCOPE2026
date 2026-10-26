from fractions import Fraction
from itertools import permutations, combinations

N = (0, 1, 2)
E = {(0, 1): Fraction(1), (1, 2): Fraction(1), (2, 0): Fraction(1)}

def internal(S):
    S = set(S)
    return sum((w for (i, j), w in E.items() if i in S and j in S), Fraction(0))

def external(S):
    S = set(S)
    total = Fraction(0)
    for j in S:
        incoming_from_outside = [w for (i, k), w in E.items() if k == j and i not in S]
        if incoming_from_outside:
            total += min(incoming_from_outside)
    return total

def value(S):
    return internal(S) + external(S)

def shapley(game):
    result = {i: Fraction(0) for i in N}
    orders = list(permutations(N))
    for order in orders:
        S = set()
        before = game(S)
        for i in order:
            S.add(i)
            after = game(S)
            result[i] += after - before
            before = after
    return {i: result[i] / len(orders) for i in N}

all_coalitions = [frozenset(i for i in N if mask & (1 << i)) for mask in range(1 << len(N))]
assert value(frozenset()) == 0
assert all(value(frozenset({i})) == 1 for i in N)
assert all(value(frozenset(pair)) == 2 for pair in combinations(N, 2))
assert value(frozenset(N)) == 3

phi_full = shapley(value)
phi_internal = shapley(internal)
phi_external = shapley(external)

for i in N:
    outgoing = sum((w for (p, q), w in E.items() if p == i), Fraction(0))
    incoming = sum((w for (p, q), w in E.items() if q == i), Fraction(0))
    corrected_internal = (outgoing + incoming) / 2
    mutual_only_internal = sum((E[(i, j)] + E[(j, i)]) / 2 for j in N
                               if (i, j) in E and (j, i) in E)
    assert phi_internal[i] == corrected_internal == 1
    assert phi_external[i] == 0
    assert phi_full[i] == corrected_internal + phi_external[i] == 1
    assert mutual_only_internal + phi_external[i] == 0

print('Coalition values: empty=0; each singleton=1; each pair=2; grand coalition=3.')
print('Exact Shapley values by permutation enumeration (6 orders):', {i: str(phi_full[i]) for i in N})
print('Exact internal contributions:', {i: str(phi_internal[i]) for i in N})
print('Exact external contributions:', {i: str(phi_external[i]) for i in N})
print('Reciprocal-edge-only internal term:', {i: '0' for i in N})
print('PASS: all 8 coalitions and all 6 player orders checked with exact rational arithmetic.')
