#!/usr/bin/env python3
from itertools import product

Q = range(3)
WORDS = list(product(Q, repeat=4))

def shadow(w):
    return {w[:i] + w[i+1:] for i in range(4)}

SHADOWS = [shadow(w) for w in WORDS]

WITNESS_STR = [
    "0000","0011","0022","0120","1100","1111",
    "1122","2102","2200","2211","2222"
]
WITNESS = [tuple(map(int, s)) for s in WITNESS_STR]

def compatible(i, j):
    return SHADOWS[i].isdisjoint(SHADOWS[j])

# Exact compatibility graph.
ADJ = []
for i in range(len(WORDS)):
    m = 0
    for j in range(len(WORDS)):
        if i != j and compatible(i, j):
            m |= 1 << j
    ADJ.append(m)

# Exact maximum-clique search with a greedy coloring upper bound.
# A clique in the compatibility graph is exactly a one-deletion-correcting code.
best = []
nodes = 0

def color_sort(P):
    order = []
    bounds = []
    U = P
    color = 0
    while U:
        color += 1
        Qm = U
        while Qm:
            bit = Qm & -Qm
            v = bit.bit_length() - 1
            order.append(v)
            bounds.append(color)
            U &= ~bit
            Qm &= ~bit
            Qm &= ~ADJ[v]
            Qm &= U
    return order, bounds

def expand(R, P):
    global best, nodes
    nodes += 1
    if not P:
        if len(R) > len(best):
            best = R[:]
        return
    order, bounds = color_sort(P)
    for k in range(len(order) - 1, -1, -1):
        if len(R) + bounds[k] <= len(best):
            return
        v = order[k]
        bit = 1 << v
        if not (P & bit):
            continue
        expand(R + [v], P & ADJ[v])
        P &= ~bit

# Check the displayed lower-bound code directly.
assert len(WITNESS) == 11
widx = [WORDS.index(w) for w in WITNESS]
for a in range(len(widx)):
    for b in range(a):
        assert compatible(widx[a], widx[b])

# Independently solve the complete finite instance.
expand([], (1 << len(WORDS)) - 1)
assert len(best) == 11

# Equality-case obstruction in the symbolic proof.
# For each repeated outer symbol a, the middle symbols are the other two
# in either order. A hypothetical size-12 code would require one such word
# for each a, with pairwise disjoint deletion shadows.
c42 = {}
for a in Q:
    other = [x for x in Q if x != a]
    c42[a] = [
        (a, other[0], other[1], a),
        (a, other[1], other[0], a),
    ]

triple_count = 0
feasible_triples = 0
for choices in product(range(2), repeat=3):
    triple_count += 1
    ws = [c42[a][choices[a]] for a in Q]
    ss = [shadow(w) for w in ws]
    ok = all(ss[i].isdisjoint(ss[j]) for i in range(3) for j in range(i))
    feasible_triples += int(ok)
assert triple_count == 8
assert feasible_triples == 0

best_words = ["".join(map(str, WORDS[i])) for i in best]
print(
    "VERIFY_OK q=3 n=4 optimum=11 words=81 "
    f"witness_size={len(WITNESS)} equality_triples={triple_count} "
    f"feasible_c42_triples={feasible_triples} search_nodes={nodes}"
)
print("one_exact_optimum=" + " ".join(best_words))
