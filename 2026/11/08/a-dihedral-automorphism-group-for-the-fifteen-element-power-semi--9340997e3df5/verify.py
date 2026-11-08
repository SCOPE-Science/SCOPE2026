"""Exact finite multiplication and equivariant candidate checks for P*(Z/4Z).

All computations use Python's standard library. The proof of why every
normalised automorphism is among these candidates is mathematical, not a
consequence of finite enumeration alone.
"""
from itertools import combinations

G = tuple(range(4))
SETS = tuple(frozenset(s) for n in range(1, 5) for s in combinations(G, n))
INDEX = {s: i for i, s in enumerate(SETS)}
ZERO = frozenset(G)

def add(x, y):
    return frozenset((a + b) % 4 for a in x for b in y)

def U(i): return frozenset(((i % 4),))
def A(i): return frozenset(((i % 4), ((i + 1) % 4)))
def B(i): return frozenset(((i % 2), (((i % 2) + 2) % 4)))
def C(i): return ZERO - {i % 4}

assert len(SETS) == 15
assert len(set(U(i) for i in G)) == 4
assert len(set(A(i) for i in G)) == 4
assert len(set(B(i) for i in range(2))) == 2
assert len(set(C(i) for i in G)) == 4
assert len({U(i) for i in G} | {A(i) for i in G} |
           {B(i) for i in range(2)} | {C(i) for i in G} | {ZERO}) == 15

for i in G:
    for j in G:
        assert add(U(i), U(j)) == U(i + j)
        assert add(U(i), A(j)) == A(i + j)
        assert add(U(i), B(j)) == B(i + j)
        assert add(U(i), C(j)) == C(i + j)
        assert add(A(i), A(j)) == C(i + j + 3)
        assert add(A(i), B(j)) == ZERO
        assert add(A(i), C(j)) == ZERO
        assert add(B(i), B(j)) == B(i + j)
        assert add(B(i), C(j)) == ZERO
        assert add(C(i), C(j)) == ZERO
    assert add(ZERO, U(i)) == ZERO
    assert add(ZERO, A(i)) == ZERO
    assert add(ZERO, B(i)) == ZERO
    assert add(ZERO, C(i)) == ZERO

# Enumerate all 4*2*4 candidate maps that commute with unit translations,
# fix the four singleton units, and preserve the A/B/C/Z orbit types.
def normalized(k, ell, m):
    f = {}
    for i in G:
        f[U(i)] = U(i)
        f[A(i)] = A(i + k)
        f[B(i)] = B(i + ell)
        f[C(i)] = C(i + m)
    f[ZERO] = ZERO
    return f

def is_auto(f):
    return len(set(f.values())) == 15 and all(
        f[add(x, y)] == add(f[x], f[y]) for x in SETS for y in SETS)

candidates = [(k,ell,m) for k in G for ell in range(2) for m in G]
valid = [(k,ell,m) for k,ell,m in candidates if is_auto(normalized(k,ell,m))]
assert len(candidates) == 32
assert valid == [(k, 0, 2*k % 4) for k in G], valid

# Extend the four normalized maps by the two group automorphisms x -> +/- x.
full = []
for k,ell,m in valid:
    f = normalized(k,ell,m)
    for alpha in (1,3):
        h = {s: frozenset(alpha*x % 4 for x in s) for s in SETS}
        composite = tuple(INDEX[f[h[s]]] for s in SETS)
        assert len(set(composite)) == 15
        assert is_auto({s: SETS[composite[INDEX[s]]] for s in SETS})
        full.append(composite)
assert len(set(full)) == 8

reduced = frozenset(s for s in SETS if 0 in s)
stabilizer = [p for p in full if frozenset(SETS[p[INDEX[s]]] for s in reduced) == reduced]
assert len(stabilizer) == 2
witness = normalized(1, 0, 2)
assert witness[A(0)] == A(1) == frozenset({1,2})
assert 0 in A(0) and 0 not in witness[A(0)]
print('C4_CANDIDATES: 32 translation-equivariant orbit-preserving normalized bijections; valid=4')
print('C4_GROUP: total_automorphisms=8 reduced_stabilizer=2')
print('C4_WITNESS: {0,1} -> {1,2}')
print('VERIFY_OK')
