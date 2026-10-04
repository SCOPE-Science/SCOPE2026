#!/usr/bin/env python3
from collections import Counter

# Four-point minimal circle model C: two minimal points 0,1 and two maximal points 2,3.
C = range(4)
leC = [[False]*4 for _ in C]
for i in C:
    leC[i][i] = True
for i in (0,1):
    for j in (2,3):
        leC[i][j] = True

# P=C x C, the 16-point product model T^2_{0,0}.
P = [(i,j) for i in C for j in C]
index = {p:k for k,p in enumerate(P)}
N = len(P)
le = [[leC[P[i][0]][P[j][0]] and leC[P[i][1]][P[j][1]]
       for j in range(N)] for i in range(N)]
down = [sum(1 << i for i in range(N) if le[i][j]) for j in range(N)]
up   = [sum(1 << j for j in range(N) if le[i][j]) for i in range(N)]
ALL = (1 << N) - 1

# Two explicit H_1 cycles. Edges are oriented by the poset order.
z1 = [
    (index[(0,0)], index[(2,0)], +1),
    (index[(1,0)], index[(2,0)], -1),
    (index[(1,0)], index[(3,0)], +1),
    (index[(0,0)], index[(3,0)], -1),
]
z2 = [
    (index[(0,0)], index[(0,2)], +1),
    (index[(0,1)], index[(0,2)], -1),
    (index[(0,1)], index[(0,3)], +1),
    (index[(0,0)], index[(0,3)], -1),
]
cycles = (z1,z2)

# Pullbacks of the elementary circle 1-cocycle e^*(0<2).
def cocycle(edge_u, edge_v, coord):
    a = P[edge_u][coord]
    b = P[edge_v][coord]
    return 1 if (a,b)==(0,2) else 0

# Check z1,z2 are cycles by vertex boundaries.
for cyc in cycles:
    bd = [0]*N
    for u,v,s in cyc:
        assert le[u][v] and u != v
        bd[v] += s
        bd[u] -= s
    assert all(x==0 for x in bd)

# Check alpha,beta are 1-cocycles on every strict 3-chain x<y<z.
strict = lambda a,b: a != b and le[a][b]
for coord in (0,1):
    for x in range(N):
        for y in range(N):
            if not strict(x,y):
                continue
            for z in range(N):
                if strict(y,z):
                    assert (cocycle(y,z,coord)
                            - cocycle(x,z,coord)
                            + cocycle(x,y,coord)) == 0

# Their pairings with (z1,z2) are the identity matrix.
pairing = []
for coord in (0,1):
    row=[]
    for cyc in cycles:
        row.append(sum(s*cocycle(u,v,coord) for u,v,s in cyc))
    pairing.append(tuple(row))
assert pairing == [(1,0),(0,1)]

assignment = [-1]*N
counts = Counter()
bijective_count = 0
rank2_count = 0

def allowed(v):
    mask = ALL
    for u,a in enumerate(assignment):
        if a < 0:
            continue
        if le[u][v]:
            mask &= up[a]
        if le[v][u]:
            mask &= down[a]
        if not mask:
            break
    return mask

def induced_matrix():
    vals=[]
    for coord in (0,1):
        for cyc in cycles:
            s=0
            for u,v,coef in cyc:
                fu,fv=assignment[u],assignment[v]
                if fu != fv:
                    s += coef*cocycle(fu,fv,coord)
            vals.append(s)
    return tuple(vals)  # (a11,a12,a21,a22)

def visit(depth=0):
    global bijective_count, rank2_count
    if depth == N:
        m = induced_matrix()
        counts[m] += 1
        a,b,c,d = m
        det = a*d-b*c
        is_bij = len(set(assignment)) == N
        if is_bij:
            bijective_count += 1
        if det != 0:
            rank2_count += 1
            assert abs(det)==1
            assert is_bij
        return

    best = None
    best_mask = None
    best_size = N+1
    for v in range(N):
        if assignment[v] < 0:
            mask = allowed(v)
            size = mask.bit_count()
            if size == 0:
                return
            if size < best_size:
                best, best_mask, best_size = v, mask, size
                if size == 1:
                    break

    mask = best_mask
    while mask:
        bit = mask & -mask
        a = bit.bit_length()-1
        mask -= bit
        assignment[best] = a
        visit(depth+1)
        assignment[best] = -1

visit()

EXPECTED = {
 (0,0,0,0): 7997584,
 (1,0,0,0):5656, (-1,0,0,0):5656,
 (0,1,0,0):5656, (0,-1,0,0):5656,
 (0,0,1,0):5656, (0,0,-1,0):5656,
 (0,0,0,1):5656, (0,0,0,-1):5656,
 (1,0,1,0):4, (1,0,-1,0):4, (-1,0,1,0):4, (-1,0,-1,0):4,
 (0,1,0,1):4, (0,1,0,-1):4, (0,-1,0,1):4, (0,-1,0,-1):4,
 (1,0,0,1):4, (1,0,0,-1):4, (-1,0,0,1):4, (-1,0,0,-1):4,
 (0,1,1,0):4, (0,1,-1,0):4, (0,-1,1,0):4, (0,-1,-1,0):4,
}
assert counts == Counter(EXPECTED)
assert sum(counts.values()) == 8042896
assert len(counts) == 25
assert bijective_count == 32
assert rank2_count == 32

rank2_matrices = sorted(m for m in counts if m[0]*m[3]-m[1]*m[2] != 0)
signed_permutation = sorted([
    ( 1,0,0, 1),( 1,0,0,-1),(-1,0,0, 1),(-1,0,0,-1),
    (0, 1, 1,0),(0, 1,-1,0),(0,-1, 1,0),(0,-1,-1,0),
])
assert rank2_matrices == signed_permutation
assert (1,1,0,1) not in counts  # a Dehn-twist matrix

print("VERIFY_OK")
print("continuous_self_maps=8042896")
print("induced_H1_matrices=25")
print("rank2_maps=32")
print("bijective_maps=32")
print("rank2_matrices=signed_permutation_matrices")
print("dehn_twist_matrix_present=false")
