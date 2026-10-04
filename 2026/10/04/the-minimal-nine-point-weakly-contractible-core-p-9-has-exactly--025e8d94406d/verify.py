#!/usr/bin/env python3
from functools import lru_cache
from itertools import combinations

POINTS = ('c0','c1','c2','p','q','y','g','h','k')
INDEX = {x:i for i,x in enumerate(POINTS)}
COVERS = (
    ('c0','p'),('c0','y'),
    ('c1','p'),('c1','q'),('c1','y'),
    ('c2','q'),('c2','y'),
    ('p','g'),('p','h'),
    ('q','g'),('q','k'),
    ('y','h'),('y','k'),
)
N = len(POINTS)
FULL = (1 << N) - 1

# Transitive closure of the displayed cover relation.
LE = [[False]*N for _ in range(N)]
for i in range(N): LE[i][i] = True
for a,b in COVERS: LE[INDEX[a]][INDEX[b]] = True
for k in range(N):
    for i in range(N):
        for j in range(N):
            LE[i][j] = LE[i][j] or (LE[i][k] and LE[k][j])

def members(mask):
    return tuple(POINTS[i] for i in range(N) if (mask >> i) & 1)

def is_open(mask):
    # Under U_x={z:z<=x}, opens are precisely lower sets.
    for j in range(N):
        if (mask >> j) & 1:
            for i in range(N):
                if LE[i][j] and not ((mask >> i) & 1):
                    return False
    return True

def beat_deletions(mask):
    S = [i for i in range(N) if (mask >> i) & 1]
    ans = []
    for x in S:
        upper = [z for z in S if z != x and LE[x][z]]
        mins = [u for u in upper if all(LE[u][z] for z in upper)]
        if len(mins) == 1:
            ans.append((x,'up',mins[0]))
        lower = [z for z in S if z != x and LE[z][x]]
        maxs = [u for u in lower if all(LE[z][u] for z in lower)]
        if len(maxs) == 1:
            ans.append((x,'down',maxs[0]))
    return ans

@lru_cache(None)
def reduction_certificate(mask):
    # Returns one complete beat-point reduction to a singleton, or None.
    if mask and mask & (mask-1) == 0:
        return ()
    for x,kind,dom in beat_deletions(mask):
        tail = reduction_certificate(mask & ~(1 << x))
        if tail is not None:
            return ((POINTS[x],kind,POINTS[dom]),) + tail
    return None

def contractible(mask):
    return mask != 0 and reduction_certificate(mask) is not None

opens = tuple(m for m in range(1 << N) if is_open(m))
contractible_opens = tuple(m for m in opens if contractible(m))
max_contractible = tuple(
    m for m in contractible_opens
    if not any(m != z and (m | z) == z for z in contractible_opens)
)
covering_pairs = tuple(
    (a,b) for a,b in combinations(contractible_opens,2) if (a | b) == FULL
)

expected_max = {
    frozenset(('c0','c1','c2','p','q','g')),
    frozenset(('c0','c1','c2','p','q','y','h','k')),
}
assert len(opens) == 27
assert len(contractible_opens) == 11
assert len(max_contractible) == 2
assert {frozenset(members(m)) for m in max_contractible} == expected_max
assert len(covering_pairs) == 1
assert {frozenset(members(m)) for m in covering_pairs[0]} == expected_max
assert reduction_certificate(FULL) is None
assert beat_deletions(FULL) == []
for m in contractible_opens:
    cert = reduction_certificate(m)
    assert cert is not None
    # Recheck every listed deletion in the stage where it is used.
    stage = m
    for xname,kind,dname in cert:
        x,dom = INDEX[xname], INDEX[dname]
        assert any(t[0] == x and t[1] == kind and t[2] == dom for t in beat_deletions(stage))
        stage &= ~(1 << x)
    assert stage and stage & (stage-1) == 0

print('VERIFY_OK opens=27 contractible_nonempty=11 maximal=2 covering_pairs=1 '
      'maximal=' + ';'.join(','.join(members(m)) for m in max_contractible) +
      ' full_has_no_beat=true')
