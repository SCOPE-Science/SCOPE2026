#!/usr/bin/env python3
from itertools import product, combinations, permutations
from collections import Counter

ALPHABET = "ACGT"
COMP = {0:3, 3:0, 1:2, 2:1}
N, W, D = 4, 2, 3

def rc(x):
    return tuple(COMP[a] for a in reversed(x))

def hamming(x, y):
    return sum(a != b for a, b in zip(x, y))

def gc_content(x):
    return sum(a in (1,2) for a in x)

def word(x):
    return ''.join(ALPHABET[a] for a in x)

V = [x for x in product(range(4), repeat=N)
     if gc_content(x) == W and hamming(x, rc(x)) >= D]
index = {x:i for i,x in enumerate(V)}
adj = [set() for _ in V]
for i,j in combinations(range(len(V)),2):
    if hamming(V[i],V[j]) >= D and hamming(V[i],rc(V[j])) >= D:
        adj[i].add(j); adj[j].add(i)

# Exact Bron--Kerbosch enumeration of every maximal clique.
maximal = []
def bronk(R,P,X):
    if not P and not X:
        maximal.append(tuple(sorted(R)))
        return
    u = max(P|X, key=lambda z: len(P & adj[z])) if P or X else None
    candidates = list(P - (adj[u] if u is not None else set()))
    for v in candidates:
        bronk(R|{v}, P & adj[v], X & adj[v])
        P.remove(v); X.add(v)
bronk(set(), set(range(len(V))), set())
hist = Counter(map(len, maximal))
maximum = max(hist)
maxima = [frozenset(c) for c in maximal if len(c) == maximum]
assert maximum == 6
assert len(maxima) == 512

# Independent increasing-order enumeration of all six-cliques.
k6 = []
def enum_k(prefix, cand, target):
    if len(prefix) == target:
        k6.append(tuple(prefix)); return
    need = target - len(prefix)
    if len(cand) < need: return
    for pos,v in enumerate(cand):
        rest = [u for u in cand[pos+1:] if u in adj[v]]
        enum_k(prefix+[v], rest, target)
enum_k([], list(range(len(V))), 6)
assert len(k6) == 512
assert {frozenset(c) for c in k6} == set(maxima)

# Universal equality-case structure.
for M in maxima:
    L = sorted(M)
    assert all(hamming(V[i], rc(V[i])) == 4 for i in L)
    direct4, cross4 = set(), set()
    for a,b in combinations(L,2):
        hd = hamming(V[a],V[b])
        hc = hamming(V[a],rc(V[b]))
        assert hd in (3,4) and hc in (3,4)
        if hd == 4: direct4.add((a,b))
        if hc == 4: cross4.add((a,b))
    assert direct4 == cross4 and len(direct4) == 3
    deg = Counter()
    for a,b in direct4:
        deg[a] += 1; deg[b] += 1
    assert all(deg[i] == 1 for i in L)

# Explicit 64-element symmetry subgroup: coordinate permutations commuting
# with reversal, times alphabet permutations commuting with Watson--Crick
# complement. At W=N/2 these alphabet permutations preserve GC content.
rev = tuple(reversed(range(N)))
coord = [p for p in permutations(range(N))
         if all(p[rev[i]] == rev[p[i]] for i in range(N))]
symbol = [s for s in permutations(range(4))
          if all(s[COMP[a]] == COMP[s[a]] for a in range(4))
          and all(gc_content(tuple(s[a] for a in x)) == W for x in V)]
assert len(coord) == 8 and len(symbol) == 8

def act_word(x,p,s):
    return tuple(s[x[p[i]]] for i in range(N))

max_index = {M:i for i,M in enumerate(maxima)}
actions = []
for p in coord:
    for s in symbol:
        amap=[]
        for M in maxima:
            image=frozenset(index[act_word(V[i],p,s)] for i in M)
            assert image in max_index
            amap.append(max_index[image])
        actions.append(amap)
assert len(actions) == 64
seen=set(); orbits=[]
for i in range(len(maxima)):
    if i in seen: continue
    orb={a[i] for a in actions}
    orbits.append(sorted(orb)); seen |= orb
sizes=sorted(map(len,orbits))
assert sizes == [32]*12 + [64]*2
stabilizers=sorted(64//len(o) for o in orbits)
assert stabilizers == [1]*2 + [2]*12

reps=[]
for orb in sorted(orbits, key=lambda o:(len(o), o[0])):
    M=maxima[min(orb)]
    reps.append([word(V[i]) for i in sorted(M)])

print("VERIFY_OK",
      f"eligible_vertices={len(V)}",
      f"edges={sum(map(len,adj))//2}",
      f"maximal_cliques={len(maximal)}",
      "maximal_hist="+','.join(f"{k}:{hist[k]}" for k in sorted(hist)),
      f"maximum={maximum}",
      f"labeled_maxima={len(maxima)}",
      "self_rc_distance=4",
      "distance4_matching=3",
      "all_other_pairs_distance=3",
      "group_size=64",
      f"orbits={len(orbits)}",
      "orbit_sizes=32x12,64x2",
      "stabilizers=2x12,1x2")
print("ORBIT_REPRESENTATIVES")
for r in reps:
    print(' '.join(r))
