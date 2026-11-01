"""Independent finite checks for the bidirected octahedral multipath complex.

Run: python verify.py. Requires Python 3.10+ and SymPy.
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

PART = (0, 0, 1, 1, 2, 2)
ARCS = tuple((u,v) for u in range(6) for v in range(6) if PART[u] != PART[v])
assert len(ARCS) == 24 and len(set(ARCS)) == 24
ARC_INDEX = {a:i for i,a in enumerate(ARCS)}

def acyclic_partial_map(arcs):
    succ = {}
    targets = set()
    for u,v in arcs:
        if u in succ or v in targets or PART[u] == PART[v]:
            return False
        succ[u] = v
        targets.add(v)
    for u in succ:
        seen = set()
        at = u
        while at in succ:
            if at in seen:
                return False
            seen.add(at)
            at = succ[at]
    return True

# Two different exhaustive parameterizations of the same simplex set.
# The first selects source- and target-injective directed partial maps.
FROM_MAPS = {0}
for k in range(1,6):
    for sources in combinations(range(6),k):
        for targets in permutations(range(6),k):
            aa = tuple(zip(sources, targets))
            if acyclic_partial_map(aa):
                FROM_MAPS.add(sum(1 << ARC_INDEX[a] for a in aa))
# The second tests independently chosen sets of directed edges.
FROM_SUBSETS = {0}
for k in range(1,6):
    for ids in combinations(range(24),k):
        aa = tuple(ARCS[i] for i in ids)
        if acyclic_partial_map(aa):
            FROM_SUBSETS.add(sum(1 << i for i in ids))
assert FROM_MAPS == FROM_SUBSETS
FACES = FROM_MAPS
assert len(FACES) == 1817
fvec = tuple(sum(m.bit_count() == k for m in FACES) for k in range(1,6))
assert fvec == (24,192,616,744,240)
facets = [m for m in FACES if not any((m | (1<<i)) in FACES for i in range(24) if not (m>>i)&1)]
assert Counter(m.bit_count() for m in facets) == {5:240,4:24}

# Deterministic algebraic discrete Morse matching; the empty simplex is excluded.
remaining = set(FACES) - {0}
PAIRS = []
for i in range(24):
    bit = 1 << i
    for low in sorted(remaining):
        if low & bit == 0 and (low | bit) in remaining:
            remaining.remove(low)
            remaining.remove(low | bit)
            PAIRS.append((low,low | bit))
critical = {k:tuple(sorted(m for m in remaining if m.bit_count()==k+1)) for k in range(5)}
assert len(PAIRS) == 835
assert {d:len(x) for d,x in critical.items()} == {0:1,1:0,2:12,3:101,4:32}
LOW_UP = dict(PAIRS)
UP_LOW = {u:l for l,u in PAIRS}
assert len(LOW_UP) == len(UP_LOW) == len(PAIRS)

def boundary(m):
    pos = 0
    while m:
        b = m & -m
        yield b, 1 if pos%2==0 else -1
        m ^= b
        pos += 1

# Reverse every matched Hasse incidence. Explicitly check acyclicity.
indeg = {m:0 for m in FACES if m}
adj = defaultdict(list)
num_incidences = 0
for u in FACES:
    if not u:
        continue
    for bit, s in boundary(u):
        low = u^bit
        if not low:
            continue
        num_incidences += 1
        if UP_LOW.get(u) == low:
            src,dst = low,u
        else:
            src,dst = u,low
        adj[src].append(dst)
        indeg[dst] += 1
assert num_incidences == 6408
queue = deque(m for m in indeg if indeg[m] == 0)
seen = 0
while queue:
    m = queue.popleft()
    seen += 1
    for v in adj[m]:
        indeg[v] -= 1
        if indeg[v] == 0:
            queue.append(v)
assert seen == len(FACES)-1 == 1816, (seen,len(FACES)-1)

# Signed gradient-path elimination. A lower matched cell is replaced using
# its matching upper cell's integral simplicial boundary; a matched upper
# cell is zero. This gives the chain differential on critical generators.
@lru_cache(None)
def reduce_chain_cell(m):
    if m in UP_LOW:
        return ()
    if m not in LOW_UP:
        return ((m,1),)
    top = LOW_UP[m]
    terms = {top ^ bit:s for bit,s in boundary(top)}
    unit = terms.pop(m)
    assert unit in (-1,1)
    acc = Counter()
    for face,coeff in terms.items():
        for target,value in reduce_chain_cell(face):
            acc[target] -= coeff * unit * value
    return tuple((a,v) for a,v in sorted(acc.items()) if v)

def morse_boundary(d):
    lows = critical[d-1]
    highs = critical[d]
    by_low = {m:i for i,m in enumerate(lows)}
    cols = []
    for high in highs:
        vals = Counter()
        for bit,sign in boundary(high):
            for target,value in reduce_chain_cell(high ^ bit):
                vals[target] += sign * value
        cols.append({by_low[m]:v for m,v in vals.items() if v})
    return Matrix(len(lows),len(highs),lambda i,j:cols[j].get(i,0))

D3 = morse_boundary(3)
D4 = morse_boundary(4)
assert D3.shape == (12,101) and D4.shape == (101,32)
assert sum(int(v != 0) for v in D3) == 257
assert all(v == 0 for v in D4)
S3 = smith_normal_form(D3,domain=ZZ)
nonzero_smith = [abs(int(S3[i,i])) for i in range(min(S3.shape)) if S3[i,i] != 0]
assert nonzero_smith == [1]*9
assert D3*D4 == Matrix.zeros(12,32)

# Independent binary rank calculation on the ORIGINAL simplicial chains.
by_size = {k:sorted(m for m in FACES if m.bit_count()==k) for k in range(1,6)}
def rank_mod2(k):
    rows = {m:i for i,m in enumerate(by_size[k-1])}
    basis = {}
    for col in by_size[k]:
        vec = 0
        for bit,s in boundary(col):
            vec ^= 1<<rows[col ^ bit]
        while vec:
            leading = vec.bit_length()-1
            if leading not in basis:
                basis[leading] = vec
                break
            vec ^= basis[leading]
    return len(basis)
rank1,rank2,rank3,rank4 = (rank_mod2(k) for k in (2,3,4,5))
assert (rank1,rank2,rank3,rank4) == (23,169,444,208)
assert (fvec[2]-rank2-rank3, fvec[3]-rank3-rank4, fvec[4]-rank4) == (3,92,32)
assert sum((-1)**k*fvec[k] for k in range(5))-1 == 3-92+32 == -57
print('VERIFY_OK arcs=24 faces_nonempty=1816 f_vector='+str(fvec))
print('VERIFY_OK facets_4simplices=240 facets_3simplices=24 matched_pairs=835 directed_Hasse_incidences=6408 dag_vertices=1816')
print('VERIFY_OK critical_counts=(1,0,12,101,32) morse_D3_12x101_nonzero=257 smith=1^9 morse_D4_101x32_zero')
print('VERIFY_OK original_GF2_ranks=(23,169,444,208) integral_reduced_Betti=(0,0,3,92,32) no_torsion')
