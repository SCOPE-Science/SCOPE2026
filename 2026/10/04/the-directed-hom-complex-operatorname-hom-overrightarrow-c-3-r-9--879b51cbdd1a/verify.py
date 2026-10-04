#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, deque

N = 9

# Regular cyclic tournament R_9: i -> j iff the positive cyclic difference is 1,2,3,4.
def arc(i, j):
    d = (j - i) % N
    return 1 <= d <= 4

# Cells of Hom(C3->,R9) are triples (A,B,C) of nonempty subsets with
# A x B, B x C, C x A contained in the arc set.
def valid_cell(A, B, C):
    if not A or not B or not C:
        return False
    return (all(arc(a,b) for a in A for b in B)
            and all(arc(b,c) for b in B for c in C)
            and all(arc(c,a) for c in C for a in A))

cells = []
for state in product(range(4), repeat=N):
    A = tuple(i for i,s in enumerate(state) if s == 1)
    B = tuple(i for i,s in enumerate(state) if s == 2)
    C = tuple(i for i,s in enumerate(state) if s == 3)
    if valid_cell(A,B,C):
        cells.append((A,B,C))

cells = sorted(cells)
cellset = set(cells)
assert len(cells) == 720

def dim(c):
    return sum(map(len,c)) - 3

f = defaultdict(int)
for c in cells:
    f[dim(c)] += 1
assert dict(sorted(f.items())) == {0:90, 1:270, 2:270, 3:90}

# Hasse covers: d is obtained from c by deleting one vertex from exactly one coordinate.
covers = []
for upper in cells:
    for k in range(3):
        if len(upper[k]) <= 1:
            continue
        for v in upper[k]:
            coord = tuple(x for x in upper[k] if x != v)
            lower = list(upper)
            lower[k] = coord
            lower = tuple(lower)
            assert lower in cellset
            covers.append((lower, upper))
assert len(covers) == 1917
coverset = set(covers)

# Deterministic staged matching. At stage (coordinate k, vertex v), among the cells
# still unmatched, pair a cell not containing v in coordinate k with the cell obtained
# by adjoining v whenever both are valid and still unmatched.
unmatched = set(cells)
matching = []
for k in range(3):
    for v in range(N):
        used_this_stage = set()
        for lower in sorted(unmatched):
            if lower in used_this_stage or v in lower[k]:
                continue
            newcoord = tuple(sorted(lower[k] + (v,)))
            upper = list(lower)
            upper[k] = newcoord
            upper = tuple(upper)
            if upper in unmatched and upper not in used_this_stage and (lower,upper) in coverset:
                matching.append((lower,upper))
                used_this_stage.add(lower)
                used_this_stage.add(upper)
        unmatched.difference_update(used_this_stage)

assert len(matching) == 359
assert len(unmatched) == 2
critical = sorted(unmatched, key=lambda c:(dim(c),c))
assert [dim(c) for c in critical] == [0,1]
assert critical[0] == ((0,), (1,), (5,))
assert critical[1] == ((6,), (1,), (2,5))

# Acyclicity: direct every unmatched cover from upper to lower, and reverse each matched cover.
matchset = set(matching)
adj = defaultdict(list)
indeg = {c:0 for c in cells}
for lower,upper in covers:
    if (lower,upper) in matchset:
        a,b = lower,upper
    else:
        a,b = upper,lower
    adj[a].append(b)
    indeg[b] += 1
q = deque(c for c in cells if indeg[c] == 0)
visited = 0
while q:
    x = q.popleft()
    visited += 1
    for y in adj[x]:
        indeg[y] -= 1
        if indeg[y] == 0:
            q.append(y)
assert visited == len(cells)

# Independent mod-2 cellular boundary computation. A product-of-simplices cell has
# one codimension-one face for each deletion preserving nonempty coordinates; signs
# disappear over F_2.
bydim = {d: sorted([c for c in cells if dim(c)==d]) for d in range(4)}

def gf2_rank_columns(columns):
    piv = {}
    rank = 0
    for x in columns:
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                rank += 1
                break
    return rank

ranks = {}
for d in range(1,4):
    rows = {c:i for i,c in enumerate(bydim[d-1])}
    cols = []
    for upper in bydim[d]:
        bits = 0
        for k in range(3):
            if len(upper[k]) <= 1:
                continue
            for v in upper[k]:
                coord = tuple(x for x in upper[k] if x != v)
                lower = list(upper)
                lower[k] = coord
                lower = tuple(lower)
                bits ^= (1 << rows[lower])
        cols.append(bits)
    ranks[d] = gf2_rank_columns(cols)
assert ranks == {1:89, 2:180, 3:90}

b0 = len(bydim[0]) - ranks[1]
b1 = len(bydim[1]) - ranks[1] - ranks[2]
b2 = len(bydim[2]) - ranks[2] - ranks[3]
b3 = len(bydim[3]) - ranks[3]
assert (b0,b1,b2,b3) == (1,1,0,0)
assert sum(((-1)**d)*len(bydim[d]) for d in range(4)) == 0

# The acyclic matching has exactly one critical 0-cell and one critical 1-cell and
# no other critical cells. Forman's theorem therefore yields a CW complex with one
# 0-cell and one 1-cell, hence a circle.
print('cells=720 f_vector=90,270,270,90 hasse=1917')
print('matching_pairs=359 critical_dims=0,1')
print('gf2_boundary_ranks=89,180,90 betti=1,1,0,0')
print('CYCLIC_R9_HOMC3_VERIFY_OK')
