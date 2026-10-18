"""Exact induced-matching reconfiguration verifier, affine-incidence construction.

No nonstandard dependencies. All search spaces are exhaustively enumerated.
"""
import json
from collections import Counter, deque
from pathlib import Path

P = [(x,y) for x in range(3) for y in range(3)]
L = [(m,b) for m in range(3) for b in range(3)]
E = sorted((i, 9+j) for i,(x,y) in enumerate(P)
           for j,(m,b) in enumerate(L) if (y-m*x-b)%3 == 0)
assert len(E) == 27
N = [set() for _ in range(18)]
for u,v in E:
    N[u].add(v); N[v].add(u)
assert all(len(t)==3 for t in N)

# Conflict mask for each edge, including itself. Two graph edges conflict
# exactly when one endpoint is equal or adjacent to one endpoint of the other.
conf = []
for u,v in E:
    block = 0
    for j,(a,b) in enumerate(E):
        if any(s==t or t in N[s] for s in (u,v) for t in (a,b)):
            block |= 1 << j
    conf.append(block)
assert all((conf[i]>>i)&1 for i in range(27))

levels = {k: [] for k in range(7)}
def enumerate_cliques_as_matchings(selection, candidates):
    size = selection.bit_count()
    assert size <= 6
    levels[size].append(selection)
    while candidates:
        bit = candidates & -candidates
        j = bit.bit_length()-1
        candidates ^= bit
        enumerate_cliques_as_matchings(selection|bit, candidates & ~conf[j])
enumerate_cliques_as_matchings(0,(1<<27)-1)
levels = {k: sorted(v) for k,v in levels.items()}
counts = tuple(len(levels[k]) for k in range(7))
assert counts == (1,27,189,387,135,27,0), counts
M = levels[5]
assert len(M) == 27
# Maximal induced matching sizes: only 3 and 5.
all_states = set().union(*(set(levels[k]) for k in range(7)))
maximal = [s for k in range(1,6) for s in levels[k]
           if not any((s|(1<<j)) in all_states for j in range(27) if not (s>>j&1))]
assert Counter(s.bit_count() for s in maximal) == {3:153, 5:27}

# Token addition-removal, with strict cardinality floor three (TAR >= 3).
S = sorted(levels[3]+levels[4]+levels[5]); index = {s:i for i,s in enumerate(S)}
A = [set() for _ in S]
for a,s in enumerate(S):
    for j in range(27):
        if s & (1<<j):
            v = s ^ (1<<j)
            if v in index:
                b = index[v]
                A[a].add(b); A[b].add(a)
edges_TAR = sorted((a,b) for a in range(len(S)) for b in A[a] if a<b)
assert len(S) == 549 and len(edges_TAR) == 675

def components(A):
    seen=set(); comps=[]
    for x in range(len(A)):
        if x in seen:continue
        q=[x];seen.add(x)
        for a in q:
            for b in A[a]:
                if b not in seen:seen.add(b);q.append(b)
        comps.append(q)
    return comps
assert Counter(map(len,components(A))) == {396:1,1:153}

# Effective two-delete/two-add transition among maximum matchings.
H = [set() for _ in M]
for i,s in enumerate(M):
    for j,t in enumerate(M[:i]):
        if (s&t).bit_count()==3:
            H[i].add(j);H[j].add(i)
assert all(len(v)==4 for v in H)
assert sum(map(len,H))//2 == 54

# The certificate is an explicit adjacency-preserving bijection from H
# onto the line graph of the *same* affine-incidence Pappus graph.
cert = json.loads((Path(__file__).parent/'induced_matching_certificate.json').read_text())
assert cert['maxima_masks'] == M
assert cert['states_at_least_three'] == S
assert cert['tar_edges'] == [[a,b] for a,b in edges_TAR]
f = cert['line_graph_edge_mapping']
assert sorted(f)==list(range(27))
for i in range(27):
    for j in range(i):
        assert (j in H[i]) == (len(set(E[f[i]])&set(E[f[j]]))==1)

D = Counter(); max_ecc = Counter()
for i,s in enumerate(M):
    start=index[s]; q=deque([start]); dist={start:0}
    while q:
        a=q.popleft()
        for b in A[a]:
            if b not in dist:dist[b]=dist[a]+1;q.append(b)
    assert len(dist)==396
    distances_to_M=[dist[index[t]] for t in M]
    max_ecc[max(distances_to_M)] += 1
    # Independently compute the compressed graph distances for this source.
    q=deque([i]); hdist={i:0}
    while q:
        a=q.popleft()
        for b in H[a]:
            if b not in hdist:hdist[b]=hdist[a]+1;q.append(b)
    assert len(hdist)==27
    for j,t in enumerate(M):
        assert distances_to_M[j]==4*hdist[j]
        if j>i:D[distances_to_M[j]]+=1
assert dict(sorted(D.items())) == {4:54,8:108,12:162,16:27}
assert max_ecc == {16:27}

# With a one-edge reserve (floor four), all 27 optima remain disconnected.
S4=levels[4]+levels[5]
A4={s:set() for s in S4}
for s in S4:
    for j in range(27):
        if (s>>j)&1 and (s^(1<<j)) in A4:
            t=s^(1<<j);A4[s].add(t);A4[t].add(s)
assert len(S4)==162 and sum(map(len,A4.values()))//2==135
seen=set();sizes=[]
for s in S4:
    if s in seen:continue
    q=[s];seen.add(s)
    for u in q:
        for v in A4[u]:
            if v not in seen:seen.add(v);q.append(v)
    sizes.append(len(q))
assert sorted(sizes)==[6]*27
print('VERIFY_OK incidence; levels=' + str(counts)
      + '; maximal={3:153,5:27}; floor4=27x6; floor3=396+153x1'
      + '; compressed=4_regular_27_line(Pappus); TAR_max_dist={4:54,8:108,12:162,16:27}')
