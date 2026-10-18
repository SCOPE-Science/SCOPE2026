"""Exact, dependency-free certificate for the A5 proper-coset-poset homology character.

Run with Python 3.9 or newer: python3 verify.py
The underlying homological concentration is the published theorem of Ramras;
this checks the new equivariant cellular character and its module multiplicities.
"""
from itertools import permutations
from collections import Counter, defaultdict, deque

G = [p for p in permutations(range(5)) if sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5)) % 2 == 0]
G.sort()
z = {p: i for i, p in enumerate(G)}
N = len(G)
e = z[tuple(range(5))]
assert N == 60 and e == 0
mul = [[z[tuple(a[b[i]] for i in range(5))] for b in G] for a in G]
inv = [next(j for j in range(N) if mul[i][j] == e) for i in range(N)]

def subgroup_generated(H, g):
    gens = [h for h in range(N) if (H >> h) & 1 and h != e] + [g]
    seen, q = {e}, deque([e])
    while q:
        x = q.popleft()
        for a in gens:
            y = mul[x][a]
            if y not in seen:
                seen.add(y)
                q.append(y)
    return sum(1 << k for k in seen)

subs = {1 << e}
queue = deque(subs)
while queue:
    H = queue.popleft()
    for g in range(N):
        if (H >> g) & 1:
            continue
        K = subgroup_generated(H, g)
        if K not in subs:
            subs.add(K)
            queue.append(K)
assert len(subs) == 59
assert Counter(H.bit_count() for H in subs) == {1:1,2:15,3:10,4:5,5:6,6:10,10:6,12:5,60:1}
proper = [H for H in subs if H.bit_count() < N]

# Method I: all 1018 distinct cosets, then fixed-point lower-interval recursion.
cosets = set()
for H in proper:
    for a in range(N):
        x = 0
        for h in range(N):
            if (H >> h) & 1:
                x |= 1 << mul[a][h]
        cosets.add(x)
cosets = sorted(cosets, key=lambda x:(x.bit_count(), x))
assert len(cosets) == 1018
assert Counter(x.bit_count() for x in cosets) == {1:60,2:450,3:200,4:75,5:72,6:100,10:36,12:25}

def order(g):
    x, n = g, 1
    while x != e:
        x = mul[x][g]
        n += 1
    return n

def direct(g):
    fixed = [x for x in cosets if all(((x >> h)&1) == ((x >> mul[g][h])&1) for h in range(N))]
    local = []
    for i, x in enumerate(fixed):
        local.append(1 - sum(local[j] for j in range(i) if (fixed[j] & x) == fixed[j]))
    return -1 + sum(local), len(fixed)

# Method II: only the subgroup lattice, via independent conjugacy centralizer counts.
desc = sorted(proper, key=lambda H:(-H.bit_count(), H))
weight = {}
for H in desc:
    weight[H] = 1 - sum(weight[K] for K in weight if (H & K) == H)
assert Counter((H.bit_count(), weight[H]) for H in desc) == {
    (1,60):1, (2,-4):15, (3,-2):10, (4,0):5,
    (5,0):6, (6,1):10, (10,1):6, (12,1):5,
}

def fixed_coset_count(g,H):
    centralizer = sum(mul[a][g] == mul[g][a] for a in range(N))
    conj = {mul[mul[inv[a]][g]][a] for a in range(N)}
    intersect = sum((H >> h) & 1 for h in conj)
    assert centralizer * intersect % H.bit_count() == 0
    return centralizer * intersect // H.bit_count()

def subgroup_character(g):
    return -1 + sum(weight[H] * fixed_coset_count(g,H) for H in desc)

classes = defaultdict(list)
for g in range(N):
    classes[order(g)].append(g)
assert {k:len(v) for k,v in classes.items()} == {1:1,2:15,3:20,5:24}
expected = {1:1560,2:-84,3:-21,5:5}
expected_fixed = {1:1018,2:82,3:40,5:18}
for k, els in sorted(classes.items()):
    for g in els:
        trace, nfixed = direct(g)
        assert (trace, nfixed) == (expected[k], expected_fixed[k]), (k,g,trace,nfixed)
        assert subgroup_character(g) == trace

# Additional independent chain-count convolution under subgroup chain order.
chain_counts = {}
for H in desc:
    v = [1]
    for K in desc:
        if H != K and (H & K) == H:
            for i, t in enumerate(chain_counts[K]):
                while len(v) <= i+1:
                    v.append(0)
                v[i+1] += t
    chain_counts[H] = v
for k,els in sorted(classes.items()):
    g = els[0]
    counts = []
    for H in desc:
        n = fixed_coset_count(g,H)
        for i, v in enumerate(chain_counts[H]):
            while len(counts) <= i:
                counts.append(0)
            counts[i] += v*n
    assert -1 + sum((-1)**i*c for i,c in enumerate(counts)) == expected[k]
    expected_counts = {1:[1018,6867,8310,900],2:[82,195,30],3:[40,60],5:[18,12]}
    assert counts[:len(expected_counts[k])] == expected_counts[k] and all(v == 0 for v in counts[len(expected_counts[k]):]), (k, counts)
    print('element-order',k,'class-size',len(els),'fixed chains',counts,'top trace',expected[k])

# Rational A5 irreducible characters; the six-dimensional constituent has
# complex Schur multiplicity two under character inner product.
chars = {'V6':({1:6,2:-2,3:0,5:1},2,100),
         'V4':({1:4,2:0,3:1,5:-1},1,95),
         'V5':({1:5,2:1,3:-1,5:0},1,116),
         'trivial':({1:1,2:1,3:1,5:1},1,0)}
for a,(av,anorm,_) in chars.items():
    for b,(bv,bnorm,_) in chars.items():
        ip = sum(len(els)*av[k]*bv[k] for k,els in classes.items())
        assert ip == (60*anorm if a==b else 0), (a,b,ip)
for name,(irrep,schur,mult_target) in chars.items():
    product = sum(len(els)*expected[k]*irrep[k] for k,els in classes.items())
    assert product % (60*schur) == 0
    multiplicity = product // (60*schur)
    assert multiplicity == mult_target, (name,multiplicity)
    print(name,'rational multiplicity',multiplicity)
assert 100*6+95*4+116*5 == 1560
print('ALL_CHECKS_PASSED')
