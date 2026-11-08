"""Exact finite character and coset verification for a Klein quartic threefold.

Run with Python 3 standard library: python3 verify.py.
No random sampling, external data, or symbolic numerical approximations.
"""
from itertools import product
from collections import defaultdict

P = 61
WEIGHTS = tuple(pow(-3, i, P) for i in range(5))
assert WEIGHTS == (1, 58, 9, 34, 20)
assert sum(WEIGHTS) % P == 0
assert all((3 * WEIGHTS[i] + WEIGHTS[(i + 1) % 5]) % P == 0 for i in range(5))

# Complete 35-dimensional vector space of degree-three monomials.
monomial_weight = defaultdict(list)
for exponents in product(range(4), repeat=5):
    if sum(exponents) != 3:
        continue
    character = sum(exponents[i] * WEIGHTS[i] for i in range(5)) % P
    monomial_weight[character].append(exponents)
assert sum(map(len, monomial_weight.values())) == 35
assert len(monomial_weight) == 30

# The five independent cubic partial derivatives have distinct characters.
partial_characters = {(-w) % P for w in WEIGHTS}
assert partial_characters == {3, 27, 41, 52, 60}
assert all(len(monomial_weight[c]) == 2 for c in partial_characters)
assert all(len(exps) == 1 for c, exps in monomial_weight.items() if c not in partial_characters)

# Quotient by those five 1-dimensional derivative spaces.
character_set = set(monomial_weight)
assert len(character_set) == 30
assert 0 not in character_set
assert character_set == {
    2, 3, 4, 7, 8, 11, 13, 14, 15, 16, 18, 19, 22, 26, 27,
    28, 30, 32, 36, 37, 38, 40, 41, 44, 49, 51, 52, 55, 56, 60,
}
assert not character_set.intersection({(-x) % P for x in character_set})
assert character_set | {(-x) % P for x in character_set} == set(range(1, P))

H = {pow(-3, i, P) for i in range(5)}
assert H == {1, 9, 20, 34, 58}
assert all({(h * a) % P for a in character_set} == character_set for h in H)
assert [r for r in range(1, P)
        if {(r * a) % P for a in character_set} == character_set] == sorted(H)

# Complete twelve-coset certificate; all nontrivial cases have a witness.
covered = set()
coset_witnesses = {}
for r in range(1, P):
    if r in covered:
        continue
    orbit = {r * h % P for h in H}
    covered.update(orbit)
    witness = next((a for a in sorted(character_set)
                    if r * a % P not in character_set), None)
    coset_witnesses[r] = witness
assert len(coset_witnesses) == 12
assert [r for r, w in coset_witnesses.items() if w is None] == [1]
assert set(coset_witnesses) == {1, 2, 3, 4, 5, 6, 8, 10, 12, 13, 23, 26}

# Six H-orbits are exactly the selected 30 embeddings.
assert len({min({h * a % P for h in H}) for a in character_set}) == 6
print('VERIFY_OK')
print('Degree-three monomials:', 35)
print('Jacobian-relation characters:', *sorted(partial_characters))
print('Hodge characters:', *sorted(character_set))
print('CM type stabilizer:', *sorted(H))
print('Twelve coset representative tests:',
      '; '.join(f'{r}:{w if w is not None else "stabilizer"}'
                for r, w in coset_witnesses.items()))
