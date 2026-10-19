"""Finite checks of free-left-regular-band radical quiver and class-size polynomial.
For proof and unconditional parameters see RESULT.md. Uses only the Python standard library.
"""
from itertools import product
from collections import Counter, defaultdict
from math import factorial, comb


def quiver(n):
    edges = []
    for X in range(1 << n):
        for Y in range(1 << n):
            if X != Y and (Y & X) == Y:
                d = (X ^ Y).bit_count()
                for k in range(max(d - 1, 0)):
                    edges.append((X, Y, k))
    return edges


def left_right_blocks(n):
    E = quiver(n)
    W = defaultdict(lambda: [[], []])
    for i, (X, Y, a) in enumerate(E):
        if 2 <= Y.bit_count() <= n - 2:
            W[Y][0].append(i)
        if 2 <= X.bit_count() <= n - 2:
            W[X][1].append(i)
    return E,W

E,W = left_right_blocks(5)
assert len(E) == 194
assert len(W) == 20
assert Counter((len(a),len(b)) for a,b in W.values()) == {(5,1): 10, (1,5): 10}
arrow_left={i for l,r in W.values() for i in l}
arrow_right={i for l,r in W.values() for i in r}
assert len(arrow_left) == len(arrow_right) == 60
assert not arrow_left & arrow_right
assert len(set(range(194)) - arrow_left - arrow_right) == 74
path_pairs = [(i,j) for i,(_,Y,_) in enumerate(E) for j,(X,_,_) in enumerate(E) if Y == X]
assert len(path_pairs) == 100
for i,j in path_pairs:
    _,Y,_=E[i]; X,_,_=E[j]
    assert Y == X and i in W[Y][0] and j in W[Y][1]
assert len({i for i,j in path_pairs} | {j for i,j in path_pairs}) == 120

# Verify the 20 blocks have no cross multiplication, including all other arrows.
blockid = {}
for U,(left,right) in W.items():
    for ix in left+right:
        assert ix not in blockid
        blockid[ix]=U
for i,j in path_pairs:
    assert blockid[i] == blockid[j]

# Cardinality of all ordered commuting tuples in one generalized Heisenberg factor.
def predicted_tuples(q,s):
    return q ** (5*s) + q**5 * (q**s - 1)

def rank_commutes(rows,q):
    # Rows: s tuples (a_1,...,a_5,b); center irrelevant.
    for i,x in enumerate(rows):
        for y in rows[i+1:]:
            if any((x[k]*y[5]-y[k]*x[5]) % q for k in range(5)):
                return False
    return True

for q,s in [(2,1),(2,2),(2,3),(3,1),(3,2)]:
    vecs = list(product(range(q),repeat=6))
    if s == 1:
        observed=len(vecs)
    elif s == 2:
        observed=sum(rank_commutes([x,y],q) for x in vecs for y in vecs)
    else:
        # Restrict candidate triples by precomputing centralizers; works for q=2.
        comm={x:[y for y in vecs if rank_commutes([x,y],q)] for x in vecs}
        observed=sum(rank_commutes([y,z],q) for x in vecs for y in comm[x] for z in comm[x])
    assert observed == predicted_tuples(q,s),(q,s,observed,predicted_tuples(q,s))

# For each (a,b) one class size q^(0,1,5); count class numbers by dividing
# the number of 11-coordinate elements by the size of each conjugacy class.
for q in [2,3,5]:
    types=Counter()
    for coords in product(range(q), repeat=6):
        a=coords[:5]; b=coords[5]
        rk=5 if b else (1 if any(a) else 0)
        types[rk]+=1
    assert types == {0:1,1:q**5-1,5:(q-1)*q**5}
    # central coordinates contribute q^5 elements to each fiber.
    k0=q**5
    k1=(q**5-1)*q**4
    k5=(q-1)*q**5
    assert k0+k1+k5==q**9+q**4*(q*q-1)
    assert k0 + q*k1 + q**5*k5 == q**11

# Twenty factors: attainable conjugacy-class size exponents
possible={a+5*b for a in range(21) for b in range(21-a)}
assert possible == set(range(89)) | {90,91,92,95,96,100}
print('VERIFY_OK: n=5 194 arrows, 20 disjoint (5,1)/(1,5) blocks, 74 annihilator arrows, 100 two-paths; exhaustive commuting tuples and conjugacy spectra')
