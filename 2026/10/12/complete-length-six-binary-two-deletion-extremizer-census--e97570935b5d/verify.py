#!/usr/bin/env python3
from itertools import product, combinations
from collections import Counter

WORDS = [''.join(p) for p in product('01', repeat=6)]

def descendants_choose(word):
    return frozenset(''.join(word[i] for i in I) for I in combinations(range(6), 4))

def delete_once(word):
    return {word[:i] + word[i+1:] for i in range(len(word))}

def descendants_iterated(word):
    one = delete_once(word)
    return frozenset(y for x in one for y in delete_once(x))

D = {w: descendants_choose(w) for w in WORDS}
assert all(D[w] == descendants_iterated(w) for w in WORDS)

ADJ = {w: set() for w in WORDS}
for i, a in enumerate(WORDS):
    for b in WORDS[i+1:]:
        if D[a].isdisjoint(D[b]):
            ADJ[a].add(b)
            ADJ[b].add(a)

edge_count = sum(len(v) for v in ADJ.values()) // 2
assert edge_count == 522

maximal = []
bk_nodes = 0

def bron_kerbosch(R, P, X):
    global bk_nodes
    bk_nodes += 1
    if not P and not X:
        maximal.append(tuple(sorted(R)))
        return
    U = P | X
    pivot = max(sorted(U), key=lambda u: (len(P & ADJ[u]), u)) if U else None
    candidates = sorted(P - (ADJ[pivot] if pivot is not None else set()))
    for v in candidates:
        bron_kerbosch(R | {v}, P & ADJ[v], X & ADJ[v])
        P.remove(v)
        X.add(v)

bron_kerbosch(set(), set(WORDS), set())
hist = Counter(map(len, maximal))
assert dict(sorted(hist.items())) == {2: 217, 3: 276, 4: 16}
assert bk_nodes == 620
maximum = max(hist)
assert maximum == 4
maxima = sorted(c for c in maximal if len(c) == maximum)
assert len(maxima) == 16

# An independent increasing-order enumeration of every 4-clique.
four_cliques = []
for C in combinations(WORDS, 4):
    if all(b in ADJ[a] for a, b in combinations(C, 2)):
        four_cliques.append(C)
assert four_cliques == maxima

core = set(maxima[0])
for C in maxima[1:]:
    core.intersection_update(C)
assert core == {'000000', '111111'}
assert all(sum(w.count('1') for w in C if w not in core) == 6 for C in maxima)
assert all(all(w.count('1') == 3 for w in C if w not in core) for C in maxima)

# Reduced equality-case graph after the universal constants are fixed.
mid = [w for w in WORDS if w.count('1') == 3 and '000000' in ADJ[w] and '111111' in ADJ[w]]
assert len(mid) == 20
mid_edges = [(a,b) for a,b in combinations(mid,2) if b in ADJ[a]]
assert len(mid_edges) == 16
assert {tuple(sorted(('000000', a, b, '111111'))) for a,b in mid_edges} == set(maxima)

# Dominance uses the definition D_2(v) subseteq D_2(u), with u != v.
dominant_over = {
    u: tuple(v for v in WORDS if v != u and D[v].issubset(D[u]))
    for u in WORDS
}
basic = sorted(C for C in maxima if not any(dominant_over[w] for w in C))
assert basic == [
    ('000000','000111','111000','111111'),
    ('000000','001110','110001','111111'),
    ('000000','011100','100011','111111'),
]

def rev(w):
    return w[::-1]

def comp(w):
    return ''.join('1' if x == '0' else '0' for x in w)

def action(C, use_rev, use_comp):
    out=[]
    for w in C:
        z = rev(w) if use_rev else w
        z = comp(z) if use_comp else z
        out.append(z)
    return tuple(sorted(out))

group = [(r,c) for r in (False,True) for c in (False,True)]
assert len({tuple(action((w,),r,c)[0] for w in WORDS) for r,c in group}) == 4
M=set(maxima)
seen=set(); orbits=[]
for C in maxima:
    if C in seen:
        continue
    O={action(C,r,c) for r,c in group}
    assert O <= M
    seen |= O
    orbits.append(tuple(sorted(O)))
assert seen == M
orbit_sizes=sorted(map(len,orbits))
assert orbit_sizes == [1,1,2,2,2,4,4]

B=set(basic); seen=set(); basic_orbits=[]
for C in basic:
    if C in seen:
        continue
    O={action(C,r,c) for r,c in group} & B
    seen |= O
    basic_orbits.append(tuple(sorted(O)))
assert seen == B
assert sorted(map(len,basic_orbits)) == [1,2]
basic_reps=sorted(min(O) for O in basic_orbits)
assert basic_reps == [
    ('000000','000111','111000','111111'),
    ('000000','001110','110001','111111'),
]

coverage_hist=Counter(len(set().union(*(D[w] for w in C))) for C in maxima)
assert dict(sorted(coverage_hist.items())) == {8:1, 11:2, 12:6, 14:1, 16:6}

print(
    'VERIFY_OK '
    f'vertices={len(WORDS)} edges={edge_count} bk_nodes={bk_nodes} '
    'maximal_hist=2:217,3:276,4:16 maximum=4 labeled_maxima=16 '
    'core=000000,111111 middle_weight=3 group_size=4 '
    'orbits=7 orbit_sizes=1,1,2,2,2,4,4 basic_maxima=3 basic_orbits=2 '
    'basic_orbit_sizes=1,2 coverage=8:1,11:2,12:6,14:1,16:6'
)
