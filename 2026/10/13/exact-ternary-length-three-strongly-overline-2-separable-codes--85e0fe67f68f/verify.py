from itertools import product, combinations, permutations
from collections import Counter
import hashlib

Q = range(3)
WORDS = list(product(Q, repeat=3))
INDEX = {w:i for i,w in enumerate(WORDS)}
N = len(WORDS)


def desc_vertices(vertices):
    masks = [0, 0, 0]
    for v in vertices:
        w = WORDS[v]
        for j in range(3):
            masks[j] |= 1 << w[j]
    return tuple(masks)


def box_vertices(D):
    return [v for v,w in enumerate(WORDS)
            if all((D[j] >> w[j]) & 1 for j in range(3))]


def derive_minimal_forbidden_sets():
    # A code fails strong 2-separability iff some singleton/pair C0 has
    # a same-descendant coalition omitting an element of C0. Singleton
    # failure is impossible for a set of distinct words, so enumerate pairs.
    candidates = set()
    for a,b in combinations(range(N), 2):
        D = desc_vertices((a,b))
        box = box_vertices(D)
        for endpoint in (a,b):
            others = [v for v in box if v != endpoint]
            for r in range(1, len(others)+1):
                for X in combinations(others, r):
                    if desc_vertices(X) == D:
                        candidates.add(frozenset((a,b)) | frozenset(X))
    ordered = sorted(candidates, key=lambda F:(len(F), tuple(sorted(F))))
    minimal = []
    for F in ordered:
        if not any(G <= F for G in minimal):
            minimal.append(F)
    return tuple(minimal)


FORBIDDEN = derive_minimal_forbidden_sets()
assert len(FORBIDDEN) == 891
assert Counter(map(len, FORBIDDEN)) == Counter({4:891})
INCIDENT = [[] for _ in range(N)]
for F in FORBIDDEN:
    for v in F:
        INCIDENT[v].append(F)


def legal_add(chosen_set, v):
    enlarged = chosen_set | {v}
    return not any(F <= enlarged for F in INCIDENT[v])


def enumerate_normalized_maxima():
    # Coordinatewise symbol permutations act transitively on the 27 words,
    # so every nonempty code is equivalent to one containing 000 (vertex 0).
    order = sorted(range(1,N), key=lambda v:(-len(INCIDENT[v]), v))
    best = 1
    maxima = []
    nodes = 0
    def dfs(pos, chosen, chosen_set):
        nonlocal best, maxima, nodes
        nodes += 1
        if len(chosen) + (len(order)-pos) < best:
            return
        if pos == len(order):
            t = tuple(sorted(chosen))
            if len(t) > best:
                best = len(t)
                maxima = [t]
            elif len(t) == best:
                maxima.append(t)
            return
        v = order[pos]
        if legal_add(chosen_set, v):
            dfs(pos+1, chosen+[v], chosen_set|{v})
        dfs(pos+1, chosen, chosen_set)
    dfs(0, [0], {0})
    return best, tuple(sorted(set(maxima))), nodes


BEST, NORMALIZED, SEARCH_NODES = enumerate_normalized_maxima()
assert BEST == 10
assert len(NORMALIZED) == 20

PERMS = tuple(permutations(Q))
COORD_PERMS = tuple(permutations(range(3)))

def transform(code, symbol_perms, coord_perm=(0,1,2)):
    out=[]
    for v in code:
        w=WORDS[v]
        nw=tuple(symbol_perms[j][w[coord_perm[j]]] for j in range(3))
        out.append(INDEX[nw])
    return tuple(sorted(out))


def expand_labeled(normalized):
    out=set()
    for code in normalized:
        for p0 in PERMS:
            for p1 in PERMS:
                for p2 in PERMS:
                    out.add(transform(code, (p0,p1,p2)))
    return tuple(sorted(out))

LABELED = expand_labeled(NORMALIZED)
assert len(LABELED) == 54
assert len(NORMALIZED)*27 == len(LABELED)*BEST


def is_strong_2_separable(code):
    m=len(code)
    full_masks=[]
    # all nonempty coalition descendants once
    for mask in range(1,1<<m):
        verts=[code[i] for i in range(m) if (mask>>i)&1]
        full_masks.append((mask, desc_vertices(verts)))
    for r in (1,2):
        for inds in combinations(range(m), r):
            c0mask=sum(1<<i for i in inds)
            D=desc_vertices(code[i] for i in inds)
            intersection=(1<<m)-1
            found=False
            for mask,D2 in full_masks:
                if D2==D:
                    intersection &= mask
                    found=True
            assert found
            if intersection != c0mask:
                return False
    return True

# Replay the original definition on every labeled maximum.
assert all(is_strong_2_separable(code) for code in LABELED)

# Reconstruct complete orbit under coordinate permutations and independent
# symbol permutations in each coordinate: (S_3)^3 semidirect S_3.
remaining=set(LABELED)
orbits=[]
while remaining:
    code=min(remaining)
    orb=set()
    for cp in COORD_PERMS:
        for p0 in PERMS:
            for p1 in PERMS:
                for p2 in PERMS:
                    orb.add(transform(code,(p0,p1,p2),cp))
    assert orb <= set(LABELED)
    orbits.append(orb)
    remaining -= orb
assert len(orbits)==1 and len(orbits[0])==54
GROUP_ORDER = 6**4
STABILIZER = GROUP_ORDER//54
assert STABILIZER==24


def profile(code):
    ws=[WORDS[v] for v in code]
    coord=tuple(sorted(tuple(sorted(Counter(w[j] for w in ws).values(), reverse=True))
                       for j in range(3)))
    hd=Counter(sum(x!=y for x,y in zip(a,b)) for a,b in combinations(ws,2))
    box=Counter()
    for a,b in combinations(ws,2):
        D=tuple((1<<a[j])|(1<<b[j]) for j in range(3))
        k=sum(all((D[j]>>z[j])&1 for j in range(3)) for z in ws)
        box[k]+=1
    return coord, tuple(sorted(hd.items())), tuple(sorted(box.items()))

profiles=Counter(profile(c) for c in LABELED)
expected_profile=(
    ((4,3,3),(4,3,3),(4,3,3)),
    ((1,3),(2,30),(3,12)),
    ((2,33),(3,12)),
)
assert profiles == Counter({expected_profile:54})
REP = min(LABELED)
REP_WORDS = tuple(''.join(map(str,WORDS[v])) for v in REP)
assert REP_WORDS == ('000','001','012','022','102','110','121','202','211','220')


def canonical_lines(codes):
    lines=[]
    for code in codes:
        lines.append(','.join(''.join(map(str,WORDS[v])) for v in code))
    return ('\n'.join(lines)+'\n').encode()

norm_sha=hashlib.sha256(canonical_lines(NORMALIZED)).hexdigest()
lab_sha=hashlib.sha256(canonical_lines(LABELED)).hexdigest()
forb_lines=('\n'.join(','.join(''.join(map(str,WORDS[v])) for v in sorted(F)) for F in FORBIDDEN)+'\n').encode()
forb_sha=hashlib.sha256(forb_lines).hexdigest()

print(
    'VERIFY_OK vertices=27 forbidden_minimal=891 forbidden_size=4 '
    f'search_nodes={SEARCH_NODES} maximum={BEST} normalized_maxima={len(NORMALIZED)} '
    f'labeled_maxima={len(LABELED)} natural_group={GROUP_ORDER} orbits=1 orbit_size=54 stabilizer={STABILIZER} '
    'coordinate_profile=4,3,3x3 hamming_profile=1x3,2x30,3x12 '
    'pair_box_profile=2x33,3x12 '
    'representative=' + ','.join(REP_WORDS) + ' '
    f'forbidden_sha256={forb_sha} normalized_sha256={norm_sha} labeled_sha256={lab_sha}'
)
