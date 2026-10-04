from collections import Counter, defaultdict

ADJ = {
    "E1": ["G6","G5","G4","G3","G2","F16","F15","F14","F13","F12"],
    "E2": ["G5","G6","G1","F12","F26","F25","F24","G3","F23","G4"],
    "E3": ["G4","G5","G6","G1","G2","F34","F35","F36","F13","F23"],
    "E4": ["F34","G3","F24","F14","F46","F45","G5","G6","G1","G2"],
    "E5": ["G1","G6","F45","F35","F25","F15","F56","G4","G3","G2"],
    "E6": ["G1","F26","F36","F46","G5","F56","G4","G3","G2","F16"],
    "F12": ["F46","F45","F36","F35","F34","G2","E2","G1","E1","F56"],
    "F13": ["F56","E1","G1","F26","F25","F24","G3","E3","F45","F46"],
    "F14": ["F26","F36","F25","F35","E4","G4","F23","F56","E1","G1"],
    "F15": ["F26","F36","F46","G5","E5","F34","F24","F23","E1","G1"],
    "F16": ["G1","G6","F45","F35","F25","F34","F24","F23","E1","E6"],
    "F23": ["F45","F46","F14","F56","F15","F16","G2","G3","E2","E3"],
    "F24": ["E4","G4","F56","F15","F16","G2","E2","F13","F36","F35"],
    "F25": ["F36","F14","F46","G5","E5","F16","F34","G2","E2","F13"],
    "F26": ["F14","F15","E6","G6","F45","F35","F34","G2","E2","F13"],
    "F34": ["E4","G3","G4","F56","F15","F16","F25","F26","F12","E3"],
    "F35": ["F14","F46","G5","E5","F16","F26","F12","E3","G3","F24"],
    "F36": ["F25","F14","F15","E6","G6","F45","F12","E3","G3","F24"],
    "F45": ["F23","G4","E4","G5","E5","F16","F26","F36","F12","F13"],
    "F46": ["F23","G4","E4","F35","F25","F15","E6","G6","F12","F13"],
    "F56": ["G6","G5","E6","E5","F34","F24","F23","F14","F13","F12"],
    "G1": ["E6","F16","E5","E4","E3","E2","F12","F13","F14","F15"],
    "G2": ["E5","E6","E1","F23","F24","F25","F26","F12","E3","E4"],
    "G3": ["E4","F34","E5","E6","E1","F23","E2","F13","F36","F35"],
    "G4": ["E3","F45","F46","F14","F24","F34","E5","E6","E1","E2"],
    "G5": ["E2","E3","E4","F45","F35","F25","F15","E6","F56","E1"],
    "G6": ["E2","E3","E4","E5","F16","F26","F36","F46","F56","E1"],
}

# The source data are symmetric: each line records its ten intersections.
for a, bs in ADJ.items():
    assert len(bs) == 10 and len(set(bs)) == 10
    for b in bs:
        assert a in ADJ[b]

nodes = sorted({tuple(sorted((a,b))) for a,bs in ADJ.items() for b in bs})
assert len(nodes) == 135
node_id = {p:i for i,p in enumerate(nodes)}
g = [set() for _ in nodes]
for a, bs in ADJ.items():
    for i,b in enumerate(bs):
        c = bs[(i+1) % len(bs)]
        u = node_id[tuple(sorted((a,b)))]
        v = node_id[tuple(sorted((a,c)))]
        g[u].add(v); g[v].add(u)
assert sum(map(len,g)) // 2 == 270
assert set(map(len,g)) == {4}


def cycles_of_length(k):
    """All undirected simple cycles of length k, in cyclic vertex order."""
    out = set()
    n = len(g)
    for s in range(n):
        path=[s]; seen={s}
        def dfs(v):
            if len(path) == k:
                if s in g[v]:
                    # s is the least vertex because we only add vertices > s.
                    # Break reversal symmetry by requiring second < last.
                    if path[1] < path[-1]:
                        out.add(tuple(path))
                return
            for w in sorted(g[v]):
                if w <= s or w in seen:
                    continue
                seen.add(w); path.append(w)
                dfs(w)
                path.pop(); seen.remove(w)
        dfs(s)
    return sorted(out)


def chordless(c):
    S=set(c); k=len(c)
    for i,v in enumerate(c):
        if len(g[v] & S) != 2:
            return False
        if c[(i-1)%k] not in g[v] or c[(i+1)%k] not in g[v]:
            return False
    return True

by_k={k:[c for c in cycles_of_length(k) if chordless(c)] for k in (3,4,5,6)}
assert {k:len(v) for k,v in by_k.items()} == {3:10,4:90,5:30,6:0}
regions=[]
for k in (3,4,5):
    regions += [(k,c) for c in by_k[k]]
assert len(regions)==130

# Each line-segment wall is an edge of G(X). Attach to it the two chamber cycles using it.
wall_regions=defaultdict(list)
for rid,(k,c) in enumerate(regions):
    for i,u in enumerate(c):
        v=c[(i+1)%k]
        e=tuple(sorted((u,v)))
        wall_regions[e].append(rid)
assert len(wall_regions)==270
assert set(len(x) for x in wall_regions.values()) == {2}

# Dual adjacency and wall types.
dual=[set() for _ in regions]
wall_types=Counter()
for e, rr in wall_regions.items():
    a,b=rr
    dual[a].add(b); dual[b].add(a)
    ka,kb=regions[a][0],regions[b][0]
    wall_types[tuple(sorted((ka,kb)))] += 1
assert wall_types == Counter({(3,5):30,(4,5):120,(4,4):120})
assert sum(wall_types.values()) == 270
assert all(len(dual[rid]) == k for rid,(k,_) in enumerate(regions))

# Profile = multiset of neighboring polygon sizes.
profiles=Counter()
for rid,(k,c) in enumerate(regions):
    prof=tuple(sorted(Counter(regions[j][0] for j in dual[rid]).items()))
    profiles[(k,prof)] += 1
expected = Counter({
    (3, ((5,3),)): 10,
    (5, ((3,1),(4,4))): 30,
    (4, ((4,4),)): 20,
    (4, ((4,3),(5,1))): 20,
    (4, ((4,2),(5,2))): 50,
})
assert profiles == expected

# Independent handshake checks from the profile counts.
assert 10*3 == 30
assert 30*5 == 30 + 120
assert 90*4 == 2*120 + 120
assert (10*3 + 90*4 + 30*5)//2 == 270

print("vertices=135")
print("line_segment_walls=270")
print("chambers=triangles:10 quadrilaterals:90 pentagons:30")
print("wall_types=T-P:30 Q-P:120 Q-Q:120 others:0")
print("pentagon_profile=30*(T:1,Q:4)")
print("quadrilateral_profiles=20*(Q:4);20*(Q:3,P:1);50*(Q:2,P:2)")
print("triangle_profile=10*(P:3)")
print("VERIFY_OK")
