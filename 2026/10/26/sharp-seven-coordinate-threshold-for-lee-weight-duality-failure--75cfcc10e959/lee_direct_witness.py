"""Direct finite-field verification of a seven-coordinate Lee-duality witness.

Run: python3 lee_direct_witness.py
Uses only the Python standard library and exhaustive exact arithmetic.
"""
from itertools import product
from collections import Counter

Q = 5
W = (0, 1, 2, 2, 1)
GA = ((1, 1, 2, 2, 2, 2, 2), (4, 4, 0, 1, 2, 4, 4))
GB = ((1, 1, 1, 2, 2, 2, 2), (3, 4, 4, 0, 0, 2, 4))


def distributions(G):
    n = len(G[0])
    primal = Counter()
    for a, b in product(range(Q), repeat=2):
        word = [(a * G[0][j] + b * G[1][j]) % Q for j in range(n)]
        primal[sum(W[x] for x in word)] += 1
    dual = Counter()
    for x in product(range(Q), repeat=n):
        if all(sum(x[j] * row[j] for j in range(n)) % Q == 0 for row in G):
            dual[sum(W[t] for t in x)] += 1
    assert sum(primal.values()) == Q**2
    assert sum(dual.values()) == Q**(n-2)
    return primal, dual


PA, DA = distributions(GA)
PB, DB = distributions(GB)
assert PA == PB
assert DA[4] == 56 and DB[4] == 60
assert DA != DB
assert PA == Counter({0: 1, 6: 2, 7: 6, 8: 4, 9: 4, 10: 2, 11: 4, 12: 2})
print("PRIMAL", sorted(PA.items()))
print("DUAL_A", sorted(DA.items()))
print("DUAL_B", sorted(DB.items()))
print("DIRECT_WITNESS_OK")
