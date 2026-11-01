#!/usr/bin/env python3
"""Reproduce the Fano-incidence magnitude homology and its full symmetry character.

No external dependencies. All distances use the fourteen-vertex graph metric.
"""
from collections import Counter, deque
from itertools import product

N = 14

def dot2(a, b):
    return (a & b).bit_count() & 1

adj = [set() for _ in range(N)]
for point in range(1, 8):
    for normal in range(1, 8):
        if dot2(point, normal) == 0:
            u, v = point - 1, normal + 6
            adj[u].add(v)
            adj[v].add(u)
assert [len(x) for x in adj] == [3] * 14
assert sum(map(len, adj)) // 2 == 21

dist = []
for s in range(N):
    d = [100] * N
    d[s] = 0
    queue = deque([s])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if d[v] == 100:
                d[v] = d[u] + 1
                queue.append(v)
    dist.append(d)
assert max(max(row) for row in dist) == 3


def basis(k, length=4):
    result = []
    def visit(seq, remaining):
        if len(seq) == k + 1:
            if remaining == 0:
                result.append(tuple(seq))
            return
        u = seq[-1]
        for v in range(N):
            dd = dist[u][v]
            if 0 < dd <= remaining:
                visit(seq + [v], remaining - dd)
    for u in range(N):
        visit([u], length)
    return result

bases = {k: basis(k) for k in (2, 3, 4)}
assert tuple(len(bases[k]) for k in (2, 3, 4)) == (840, 2268, 1134)


def boundary(seq):
    terms = {}
    for i in range(1, len(seq)-1):
        if dist[seq[i-1]][seq[i+1]] == dist[seq[i-1]][seq[i]] + dist[seq[i]][seq[i+1]]:
            t = seq[:i] + seq[i+1:]
            terms[t] = terms.get(t, 0) + (-1 if i & 1 else 1)
    return {t:c for t,c in terms.items() if c}

b2 = set(bases[2]); b3 = set(bases[3])
cols3 = [boundary(seq) for seq in bases[3]]
cols4 = [boundary(seq) for seq in bases[4]]
assert all(set(col) <= b2 for col in cols3)
assert all(set(col) <= b3 for col in cols4)
for col4 in cols4:
    composite = {}
    for t, a in col4.items():
        for s, b in boundary(t).items():
            composite[s] = composite.get(s, 0) + a*b
    assert all(c == 0 for c in composite.values())

# In girth six, each three-chain contains one unique distance-two step.
# Consequently different four-chain columns have disjoint supports.
support_owner = {}
for i, col in enumerate(cols4):
    for t, c in col.items():
        assert abs(c) == 1
        assert t not in support_owner
        support_owner[t] = i
zero_four_chains = {seq for seq,col in zip(bases[4], cols4) if not col}
alt_walks = {(u,v,u,v,u) for u in range(N) for v in adj[u]}
assert zero_four_chains == alt_walks
assert len(zero_four_chains) == 42
rank4 = len(bases[4]) - len(zero_four_chains)
assert rank4 == 1092


def rank_binary(cols, row_index):
    pivots = {}
    for column in cols:
        bits = 0
        for r, coefficient in column.items():
            if coefficient & 1:
                bits ^= 1 << row_index[r]
        while bits:
            pivot = bits.bit_length() - 1
            if pivot in pivots:
                bits ^= pivots[pivot]
            else:
                pivots[pivot] = bits
                break
    return len(pivots)

rank3 = rank_binary(cols3, {s:i for i,s in enumerate(bases[2])})
assert rank3 == len(bases[2]) == 840
# Integral surjectivity is established by explicit preimages in the proof;
# the characteristic-two rank check independently tests that construction.
rank_h3 = len(bases[3]) - rank3 - rank4
assert rank_h3 == 336


def apply_matrix(cols, v):
    x = 0
    for j in range(3):
        if (v >> j) & 1:
            x ^= cols[j]
    return x


def invert_matrix(cols):
    for trial in product(range(8), repeat=3):
        if all(apply_matrix(trial, apply_matrix(cols, x)) == x for x in range(1, 8)):
            return trial
    raise AssertionError('not invertible')


def transpose_matrix(cols):
    return tuple(sum(1 << j for j in range(3) if cols[j] & (1 << i)) for i in range(3))

matrices = [C for C in product(range(8),repeat=3)
            if len({apply_matrix(C,x) for x in range(1,8)}) == 7]
assert len(matrices) == 168

def as_permutation(C):
    contragredient = transpose_matrix(invert_matrix(C))
    result = tuple([apply_matrix(C,x)-1 for x in range(1,8)]
                   + [6+apply_matrix(contragredient,x) for x in range(1,8)])
    assert all({result[v] for v in adj[u]} == adj[result[u]] for u in range(N))
    return result

collineations = [as_permutation(C) for C in matrices]
swap = tuple([i+7 for i in range(7)] + [i for i in range(7)])
correlations = [tuple(swap[g[i]] for i in range(N)) for g in collineations]
assert len(set(collineations + correlations)) == 336


def permutation_order(g):
    current = tuple(range(N))
    for power in range(1, 20):
        current = tuple(g[current[i]] for i in range(N))
        if current == tuple(range(N)):
            return power
    raise AssertionError('order exceeds bound')


def fixed_chain_count(k, fixed):
    def visit(seq, remaining):
        if len(seq) == k+1:
            return int(remaining == 0)
        u = seq[-1]
        return sum(visit(seq+[v],remaining-dist[u][v])
                   for v in fixed if v!=u and 0 < dist[u][v] <= remaining)
    return sum(visit([u],4) for u in fixed)


def trace(g):
    fixed = [v for v in range(N) if g[v]==v]
    C2 = fixed_chain_count(2,fixed)
    C3 = fixed_chain_count(3,fixed)
    C4 = fixed_chain_count(4,fixed)
    oriented_edges = sum(1 for u in fixed for v in adj[u] if v in fixed)
    return C3-C2-C4+oriented_edges, (len(fixed),oriented_edges,C2,C3,C4)

classes = Counter()
for label, group in [('collineation', collineations), ('correlation', correlations)]:
    for g in group:
        tr, counts = trace(g)
        classes[(label,permutation_order(g),*counts,tr)] += 1
assert sum(classes.values()) == 336
assert sum(n for (*_,trace_value),n in classes.items() if trace_value != 0) == 1
assert trace(tuple(range(N)))[0] == 336
assert sum(key[-1]*size for key,size in classes.items()) == 336

print('magnitude_chain_ranks C2,C3,C4:', [len(bases[k]) for k in (2,3,4)])
print('mod2_rank_d3:', rank3)
print('integral_rank_d4:', rank4)
print('zero_d4_columns_equal_oriented_edges:', len(zero_four_chains))
print('computed_H3_Q_dimension:', rank_h3)
print('automorphism_group_size:', len(collineations)+len(correlations))
print('orbit_class_summary: label,order,fixed_vertices,fixed_oriented_edges,C2,C3,C4,trace,multiplicity')
for key,size in sorted(classes.items()):
    print(*key,size,sep=',')
print('character_is_regular:',True)
print('invariant_rational_dimension:',1)
print('FANO_MAGNITUDE_REGULAR_CHARACTER_OK')
