#!/usr/bin/env python3
from itertools import product, combinations

Q=range(3)
W=list(product(Q, repeat=3))
INDEX={w:i for i,w in enumerate(W)}

def pair_failure(S):
    """Directly test failure of the strongly-2-separable condition inside S.

    A pair {x,y} fails when, after deleting x or y, the remaining codewords
    lying in desc({x,y}) still realize the same coordinate symbol sets.
    """
    S=set(S)
    for a,b in combinations(S,2):
        D=[{W[a][j],W[b][j]} for j in range(3)]
        for target in (a,b):
            cand=[z for z in S if z!=target and all(W[z][j] in D[j] for j in range(3))]
            if all({W[z][j] for z in cand}==D[j] for j in range(3)):
                return True
    return False

# Any failure for one target member of a pair has a witness of size at most 5:
# the pair plus at most one replacement codeword per coordinate.  Therefore it
# suffices to classify bad subsets through size five.
for r in (2,3):
    assert not any(pair_failure(c) for c in combinations(range(27),r))

bad4=[]
for c in combinations(range(27),4):
    if pair_failure(c):
        bad4.append(frozenset(c))
bad4set=set(bad4)
assert len(bad4)==891

bad5=0
for c in combinations(range(27),5):
    if pair_failure(c):
        bad5 += 1
        assert any(frozenset(d) in bad4set for d in combinations(c,4))

witness=[
    (0,0,1),(0,1,1),(0,2,0),(0,2,2),(1,0,2),
    (1,1,0),(1,2,1),(2,0,0),(2,1,2),(2,2,1),
]
WIT={INDEX[x] for x in witness}
assert len(WIT)==10 and not pair_failure(WIT)
assert all(not e.issubset(WIT) for e in bad4)

# Exact upper bound.  Independent symbol permutations in the three coordinates
# preserve the property and can send any selected word to 000, so a hypothetical
# 11-word code may be normalized to contain vertex 0.
edge_masks=[sum(1<<v for v in e) for e in bad4]
byv=[[] for _ in range(27)]
for em in edge_masks:
    for v in range(27):
        if (em>>v)&1:
            byv[v].append(em)

nodes=0
found11=False

def search(chosen,cand):
    global nodes,found11
    nodes += 1
    if found11:
        return
    bc=chosen.bit_count()
    if bc>=11:
        found11=True
        return
    if bc+cand.bit_count()<=10:
        return
    vs=[v for v in range(27) if (cand>>v)&1]
    if not vs:
        return
    def score(v):
        s=0
        for e in byv[v]:
            k=(e&chosen).bit_count()
            s += (10 if k>=2 else 2 if k==1 else 0)
            if (e&cand).bit_count()<=3:
                s += 1
        return s
    v=max(vs,key=score)
    vb=1<<v
    rest=cand^vb
    ch2=chosen|vb
    if not any((e&ch2)==e for e in byv[v]):
        search(ch2,rest)
    search(chosen,rest)

search(1, ((1<<27)-1)^1)
assert not found11
print(f"VERIFY_OK maximum=10 witness=10 bad4={len(bad4)} bad5={bad5} normalized_nodes={nodes}")
