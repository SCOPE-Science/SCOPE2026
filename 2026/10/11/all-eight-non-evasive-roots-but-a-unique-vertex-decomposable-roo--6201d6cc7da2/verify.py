from functools import lru_cache
from itertools import combinations

# Benedetti--Lutz, arXiv:0912.3723, Theorem 1 and Theorem 2.
# The nineteen tetrahedra of S_32 and the seven removed tetrahedra
# are transcribed from the published construction.
S32_TETRAHEDRA = {
    (0,1,3,4), (0,1,2,6), (0,1,6,7),
    (0,2,5,7), (0,5,6,7), (1,2,4,5), (1,3,4,5),
    (2,4,5,7), (3,4,5,6), (4,5,6,7),
    (0,2,5,6), (0,1,3,7), (0,3,4,7),
    (1,2,5,6), (1,3,5,6), (1,3,6,7), (3,4,6,7),
    (0,1,2,4), (0,2,4,7),
}
REMOVED = {
    (0,2,5,7), (0,5,6,7), (1,2,4,5), (1,3,4,5),
    (2,4,5,7), (3,4,5,6), (4,5,6,7),
}
B_FACETS = S32_TETRAHEDRA - REMOVED
EXPECTED_B_FACETS = {
    (0,1,3,4), (0,1,2,6), (0,1,6,7), (0,2,5,6),
    (0,1,3,7), (0,3,4,7), (1,2,5,6), (1,3,5,6),
    (1,3,6,7), (3,4,6,7), (0,1,2,4), (0,2,4,7),
}
assert B_FACETS == EXPECTED_B_FACETS


def closure(facets):
    faces = set()
    for F in facets:
        F = tuple(sorted(F))
        for r in range(1, len(F) + 1):
            faces.update(combinations(F, r))
    return frozenset(faces)


def vertices(K):
    return tuple(sorted({v for f in K for v in f}))


def deletion(K, v):
    return frozenset(f for f in K if v not in f)


def link(K, v):
    # We store nonempty faces only.  Thus an isolated vertex has empty link.
    out = set()
    for f in K:
        if v in f:
            g = tuple(x for x in f if x != v)
            if g:
                out.add(g)
    return frozenset(out)


def is_simplex(K):
    V = vertices(K)
    return bool(V) and len(K) == 2 ** len(V) - 1


@lru_cache(None)
def nonevasive(K):
    # Standard recursion: a simplex is non-evasive; the empty complex is not.
    K = frozenset(K)
    if is_simplex(K):
        return True
    if not K:
        return False
    return any(
        nonevasive(deletion(K, v)) and nonevasive(link(K, v))
        for v in vertices(K)
    )


def nonevasive_roots(K):
    if is_simplex(K):
        return tuple()
    return tuple(
        v for v in vertices(K)
        if nonevasive(deletion(K, v)) and nonevasive(link(K, v))
    )


def maximal_faces(K):
    faces = list(K)
    sets = [set(f) for f in faces]
    return frozenset(
        faces[i] for i in range(len(faces))
        if not any(sets[i] < sets[j] for j in range(len(faces)))
    )


def pure_dimension(K):
    M = maximal_faces(K)
    if not M:
        return None
    dims = {len(f) - 1 for f in M}
    return next(iter(dims)) if len(dims) == 1 else None


def is_simplex_vd(K):
    return is_simplex(K) and len(maximal_faces(K)) == 1


@lru_cache(None)
def vertex_decomposable(K):
    K = frozenset(K)
    if is_simplex_vd(K):
        return True
    d = pure_dimension(K)
    if d is None:
        return False
    for v in vertices(K):
        D = deletion(K, v)
        L = link(K, v)
        if pure_dimension(D) != d or pure_dimension(L) != d - 1:
            continue
        # Pure shedding condition: no facet of the link is a facet of deletion.
        if maximal_faces(L) & maximal_faces(D):
            continue
        if vertex_decomposable(D) and vertex_decomposable(L):
            return True
    return False


def shedding_roots(K):
    if is_simplex_vd(K):
        return tuple()
    d = pure_dimension(K)
    if d is None:
        return tuple()
    out = []
    for v in vertices(K):
        D = deletion(K, v)
        L = link(K, v)
        if pure_dimension(D) != d or pure_dimension(L) != d - 1:
            continue
        if maximal_faces(L) & maximal_faces(D):
            continue
        if vertex_decomposable(D) and vertex_decomposable(L):
            out.append(v)
    return tuple(out)


B = closure(B_FACETS)
F_VECTOR = tuple(sum(len(f) == k for f in B) for k in (1,2,3,4))
assert F_VECTOR == (8,25,30,12)
assert len(S32_TETRAHEDRA) == 19 and len(REMOVED) == 7 and len(B_FACETS) == 12

# Main non-evasiveness claim: each of the eight vertices may be queried first.
NE_ROOTS = nonevasive_roots(B)
assert NE_ROOTS == tuple(range(8))
for v in range(8):
    assert nonevasive(deletion(B, v))
    assert nonevasive(link(B, v))

# Pure vertex-decomposability behaves sharply differently at the first step.
assert vertex_decomposable(B)
VD_ROOTS = shedding_roots(B)
assert VD_ROOTS == (5,)

# For v != 5, deletion is non-pure: it has maximal triangles as well as tetrahedra.
# For v = 5, deletion is a pure 3-complex with nine tetrahedral facets.
DELETION_PROFILES = {}
for v in range(8):
    profile = {}
    for f in maximal_faces(deletion(B, v)):
        d = len(f)-1
        profile[d] = profile.get(d, 0) + 1
    DELETION_PROFILES[v] = tuple(sorted(profile.items()))
expected_profiles = {
    0: ((2,3),(3,4)),
    1: ((2,2),(3,4)),
    2: ((2,1),(3,7)),
    3: ((2,1),(3,6)),
    4: ((2,1),(3,7)),
    5: ((3,9),),
    6: ((2,3),(3,5)),
    7: ((2,1),(3,6)),
}
assert DELETION_PROFILES == expected_profiles

# Cross-check the published vertex-decomposition start: after 5, vertex 2 is allowed.
B5 = deletion(B, 5)
assert 2 in shedding_roots(B5)

print(
    "VERIFY_OK "
    "f=8,25,30,12 "
    "non_evasive_first_roots=0,1,2,3,4,5,6,7 "
    "vertex_decomposable_first_roots=5 "
    "deletion_profiles=" + ";".join(
        f"{v}:" + ",".join(f"d{d}x{c}" for d,c in DELETION_PROFILES[v])
        for v in range(8)
    )
)
