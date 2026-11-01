#!/usr/bin/env python3
"""Reproducible integer and binary-linear-algebra verification of a graph magnitude-homology character."""
from collections import Counter
from itertools import product
from pathlib import Path
import csv
import io
import sys

N = 16
adj = [set() for _ in range(N)]
for i in range(8):
    for a,b in ((i,(i+1)%8),(i,8+i),(8+i,8+(i+3)%8)):
        adj[a].add(b);adj[b].add(a)
assert len({tuple(sorted((a,b))) for a in range(N) for b in adj[a]}) == 24
assert all(len(row)==3 for row in adj)

# Floyd--Warshall graph distance over the integers.
d = [[0 if i==j else (1 if j in adj[i] else 999) for j in range(N)] for i in range(N)]
for m in range(N):
    for x in range(N):
        for y in range(N):
            d[x][y] = min(d[x][y], d[x][m]+d[m][y])
assert max(max(row) for row in d)==4
assert d[0][3]==3 and d[0][1]+d[1][2]+d[2][3]==3
assert d[0][8]+d[8][11]+d[11][3]==3

chains = {}
for k in range(1,5):
    chains[k] = [t for t in product(range(N),repeat=k+1)
                 if all(t[i]!=t[i+1] for i in range(k))
                 and sum(d[t[i]][t[i+1]] for i in range(k))==4]
assert [len(chains[i]) for i in range(1,5)]==[16,1056,2592,1296]
index = {k:{t:i for i,t in enumerate(chains[k])} for k in range(1,5)}

def boundary(t):
    """Signed magnitude boundary, with smooth inner vertices deleted."""
    return [(t[:i]+t[i+1:],(-1)**i) for i in range(1,len(t)-1)
            if d[t[i-1]][t[i]]+d[t[i]][t[i+1]]==d[t[i-1]][t[i+1]]]

# Exact integral chain-complex identity, not just mod-two.
for k in (3,4):
    for t in chains[k]:
        tbd=Counter()
        for s,sgn in boundary(t):
            for v,sgn2 in boundary(s):tbd[v]+=sgn*sgn2
        assert all(a==0 for a in tbd.values())

ends=set(s for t in chains[2] for s,z in boundary(t))
assert ends==set(chains[1])  # d2 surjects integrally.

def rank_mod_two(k):
    pivots={}
    for t in chains[k]:
        bits=0
        for s,sgn in boundary(t):bits ^= 1<<index[k-1][s]
        while bits:
            pivot=bits.bit_length()-1
            if pivot in pivots:bits ^= pivots[pivot]
            else:pivots[pivot]=bits;break
    return len(pivots)

assert rank_mod_two(3)==1040
assert rank_mod_two(4)==1248

alt=[(a,b,a,b,a) for a in range(N) for b in sorted(adj[a])]
assert len(alt)==48 and len(set(alt))==48
assert all(not boundary(t) for t in alt)
assert [len(chains[1]),len(chains[2]),len(chains[3]),len(chains[4])]==[16,1056,2592,1296]
# Over Q, these ranks are exact: rank(d3)<=1056-16, and ker(d4) contains the 48 distinct alternating cycles.
assert 1056-1040==16 and 1296-1248==48
assert 2592-1040-1248==304

# Exhaustively enumerate ALL automorphisms as distance-preserving bijections.
# Search is exact, and does not assume any previously reported group order.
perms=[]
mapping={};used=set()
def rec():
    if len(mapping)==N:
        perms.append(tuple(mapping[i] for i in range(N)));return
    opts=[]
    for u in range(N):
        if u in mapping:continue
        candidates=[v for v in range(N) if v not in used and
                    all(d[u][x]==d[v][mapping[x]] for x in mapping)]
        opts.append((len(candidates),u,candidates))
    _,u,candidates=min(opts)
    for v in candidates:
        mapping[u]=v;used.add(v);rec();used.remove(v);del mapping[u]
rec()
assert len(perms)==96 and len(set(perms))==96
assert all(all(d[p[i]][p[j]]==d[i][j] for j in range(N) for i in range(N)) for p in perms)

def order(p):
    t=tuple(range(N))
    for k in range(1,100):
        t=tuple(p[x] for x in t)
        if t==tuple(range(N)):return k
    raise ValueError('unexpected order')

rows=[]
for p in sorted(perms):
    fixed={a for a in range(N) if p[a]==a}
    cfix=[sum(all(x in fixed for x in t) for t in chains[k]) for k in range(1,5)]
    fixed_arcs=sum(1 for a in fixed for b in adj[a] if b in fixed)
    chi=cfix[0]-cfix[1]+cfix[2]-cfix[3]+fixed_arcs
    rows.append((','.join(map(str,p)),order(p),len(fixed),fixed_arcs,*cfix,chi))
assert Counter(row[-1] for row in rows)==Counter({0:75,-4:12,4:8,304:1})
assert Counter((r[2],r[3],r[-1]) for r in rows)==Counter({(0,0,0):75,(4,0,4):8,(4,4,-4):12,(16,48,304):1})
assert sum(r[-1] for r in rows)==288 and 288//96==3

header=['permutation_on_0_to_15','automorphism_order','fixed_vertices','fixed_oriented_edges',
        'fixed_C1_4','fixed_C2_4','fixed_C3_4','fixed_C4_4','trace_on_H3_4']
text=io.StringIO(); w=csv.writer(text,lineterminator='\n');w.writerow(header);w.writerows(rows)
file_path=Path(__file__).with_name('character_table.csv')
if '--write-table' in sys.argv:
    file_path.write_text(text.getvalue(),encoding='utf-8')
else:
    assert file_path.read_text(encoding='utf-8')==text.getvalue()

print('GRAPH_VERTICES=16 GRAPH_EDGES=24 DIAMETER=4')
print('CHAIN_DIMENSIONS_C1_C4=16,1056,2592,1296')
print('BINARY_BOUNDARY_RANKS_D3_D4=1040,1248')
print('ALTERNATING_INTEGRAL_4_CYCLES=48')
print('RATIONAL_HOMOLOGY_BIDEGREE_4: H1=0 H2=0 H3=304 H4=48')
print('AUTOMORPHISMS_EXHAUSTIVE=96')
print('H3_CHARACTER_DISTRIBUTION=304:1,4:8,-4:12,0:75')
print('H3_INVARIANT_DIMENSION=3')
print('NON_GEODETIC_PAIR=0,3 PATHS=(0,1,2,3);(0,8,11,3)')
print('MAGNITUDE_VERIFY_OK')
