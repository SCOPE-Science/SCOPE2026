#!/usr/bin/env python3
"""Exact verifier for the D_{6,3} discrete-Morse certificate.

The program uses only the Python standard library.  It reconstructs the
simplicial complex from the domination-number definition, rebuilds the
staged matching from the printed edge order, checks acyclicity on the full
modified Hasse diagram, computes the integer Morse differential C_5^M ->
C_4^M by recursive algebraic cancellation, and cross-checks the ordinary
simplicial boundary ranks over F_2 and F_3.
"""

from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations

N = 6
EDGES = [(i, j) for i in range(N) for j in range(i + 1, N)]
EDGE_INDEX = {e: k for k, e in enumerate(EDGES)}
# Vertex labels here are 1,...,6.  Internally they are shifted to 0,...,5.
MATCHING_ORDER_1BASED = [
    (1, 3), (1, 2), (2, 3), (1, 5), (4, 5),
    (4, 6), (5, 6), (1, 4), (3, 4), (3, 6),
    (1, 6), (2, 6), (2, 4), (3, 5), (2, 5),
]
MATCHING_ORDER = [EDGE_INDEX[(a - 1, b - 1)] for a, b in MATCHING_ORDER_1BASED]
EXPECTED_FACE_COUNTS = {1: 15, 2: 105, 3: 455, 4: 1185, 5: 1647, 6: 915, 7: 180}
EXPECTED_CRITICAL_BY_DIM = {0: 1, 4: 115, 5: 24}
EXPECTED_BOUNDARY_RANKS = {2: 14, 3: 91, 4: 364, 5: 821, 6: 711, 7: 180}


def domination_number(mask):
    adj = [0] * N
    for e, (u, v) in enumerate(EDGES):
        if (mask >> e) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    full = (1 << N) - 1
    for r in range(1, N + 1):
        for comb in combinations(range(N), r):
            covered = 0
            for v in comb:
                covered |= 1 << v
                covered |= adj[v]
            if covered == full:
                return r
    raise AssertionError("domination number not found")


def build_complex():
    by_size = defaultdict(list)
    all_faces = set()
    for mask in range(1, 1 << len(EDGES)):
        if domination_number(mask) >= 3:
            by_size[mask.bit_count()].append(mask)
            all_faces.add(mask)
    by_size = {k: sorted(v) for k, v in by_size.items()}
    counts = {k: len(v) for k, v in by_size.items()}
    assert counts == EXPECTED_FACE_COUNTS, (counts, EXPECTED_FACE_COUNTS)
    # Downward closure, checked directly.
    for face in all_faces:
        for e in range(len(EDGES)):
            if (face >> e) & 1:
                sub = face & ~(1 << e)
                if sub:
                    assert sub in all_faces
    return by_size, all_faces


def build_matching(all_faces):
    unmatched = set(all_faces)
    pairs = []
    for e in MATCHING_ORDER:
        bit = 1 << e
        lows = [x for x in unmatched if not (x & bit) and (x | bit) in unmatched]
        for low in lows:
            up = low | bit
            if low in unmatched and up in unmatched:
                unmatched.remove(low)
                unmatched.remove(up)
                pairs.append((low, up))
    # Cover relation and uniqueness checks.
    used = set()
    for low, up in pairs:
        assert low in all_faces and up in all_faces
        assert up.bit_count() == low.bit_count() + 1
        assert low & up == low
        assert low not in used and up not in used
        used.add(low); used.add(up)
    assert not (used & unmatched)
    assert used | unmatched == all_faces
    crit = Counter(x.bit_count() - 1 for x in unmatched)
    assert dict(crit) == EXPECTED_CRITICAL_BY_DIM, crit
    assert len(pairs) == 2181
    return pairs, unmatched


def check_acyclic(all_faces, pairs):
    faces = sorted(all_faces)
    idx = {m: i for i, m in enumerate(faces)}
    matched = set(pairs)
    adj = [[] for _ in faces]
    indeg = [0] * len(faces)
    cover_count = 0
    for up in faces:
        if up.bit_count() < 2:
            continue
        for e in range(len(EDGES)):
            if (up >> e) & 1:
                low = up & ~(1 << e)
                if not low or low not in all_faces:
                    continue
                cover_count += 1
                if (low, up) in matched:
                    a, b = idx[low], idx[up]
                else:
                    a, b = idx[up], idx[low]
                adj[a].append(b)
                indeg[b] += 1
    assert cover_count == 21300, cover_count
    q = deque(i for i, d in enumerate(indeg) if d == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    assert seen == len(faces), (seen, len(faces))
    return cover_count


def incidence(up, low):
    diff = up ^ low
    assert diff and diff & (diff - 1) == 0 and (up & diff)
    removed = diff.bit_length() - 1
    pos = sum(1 for j in range(removed) if (up >> j) & 1)
    return -1 if pos & 1 else 1


def check_morse_boundary(pairs, critical):
    low_to_up = {lo: up for lo, up in pairs}
    up_to_low = {up: lo for lo, up in pairs}
    crit4 = sorted(x for x in critical if x.bit_count() == 5)
    crit5 = sorted(x for x in critical if x.bit_count() == 6)
    c4_index = {x: i for i, x in enumerate(crit4)}
    visiting = set()

    @lru_cache(None)
    def project4(alpha):
        # Projection of a 4-simplex to the critical Morse 4-chains after
        # algebraic cancellation of all matched pairs.
        if alpha in c4_index:
            return ((c4_index[alpha], 1),)
        if alpha in up_to_low:
            # Upper element of a (3,4)-pair is eliminated as an upper cell.
            return ()
        assert alpha in low_to_up
        if alpha in visiting:
            raise AssertionError("cycle in Morse projection dependencies")
        visiting.add(alpha)
        beta = low_to_up[alpha]
        pivot = incidence(beta, alpha)
        out = {}
        for e in range(len(EDGES)):
            if (beta >> e) & 1:
                gamma = beta & ~(1 << e)
                if gamma == alpha:
                    continue
                coeff = -incidence(beta, gamma) * pivot
                for j, v in project4(gamma):
                    out[j] = out.get(j, 0) + coeff * v
                    if out[j] == 0:
                        del out[j]
        visiting.remove(alpha)
        return tuple(sorted(out.items()))

    nonzero_columns = []
    for beta in crit5:
        out = {}
        for e in range(len(EDGES)):
            if (beta >> e) & 1:
                alpha = beta & ~(1 << e)
                coeff = incidence(beta, alpha)
                for j, v in project4(alpha):
                    out[j] = out.get(j, 0) + coeff * v
                    if out[j] == 0:
                        del out[j]
        if out:
            nonzero_columns.append((beta, out))
    assert not nonzero_columns, nonzero_columns[:1]
    return len(crit4), len(crit5), project4.cache_info().currsize


def boundary_rank_mod_p(by_size, k, p):
    # Boundary from (k-1)-simplices (k vertices in the abstract complex)
    # to (k-2)-simplices, with standard increasing-vertex orientation.
    rows = {m: i for i, m in enumerate(by_size[k - 1])}
    basis = {}
    rank = 0
    for up in by_size[k]:
        vec = {}
        bits = [e for e in range(len(EDGES)) if (up >> e) & 1]
        for pos, e in enumerate(bits):
            low = up & ~(1 << e)
            r = rows[low]
            c = 1 if pos % 2 == 0 else p - 1
            vec[r] = (vec.get(r, 0) + c) % p
            if vec[r] == 0:
                del vec[r]
        while vec:
            pivot = max(vec)
            if pivot not in basis:
                inv = pow(vec[pivot], -1, p)
                basis[pivot] = {r: (c * inv) % p for r, c in vec.items()}
                rank += 1
                break
            factor = vec[pivot]
            b = basis[pivot]
            for r, c in b.items():
                nv = (vec.get(r, 0) - factor * c) % p
                if nv:
                    vec[r] = nv
                elif r in vec:
                    del vec[r]
    return rank


def check_homology_crosscheck(by_size):
    for p in (2, 3):
        ranks = {k: boundary_rank_mod_p(by_size, k, p) for k in range(2, 8)}
        assert ranks == EXPECTED_BOUNDARY_RANKS, (p, ranks)
        betti = {}
        for k in range(1, 8):
            dim = k - 1
            incoming = ranks.get(k, 0)
            outgoing = ranks.get(k + 1, 0)
            betti[dim] = len(by_size[k]) - incoming - outgoing
        assert betti == {0: 1, 1: 0, 2: 0, 3: 0, 4: 115, 5: 24, 6: 0}, (p, betti)


def main():
    by_size, all_faces = build_complex()
    pairs, critical = build_matching(all_faces)
    cover_count = check_acyclic(all_faces, pairs)
    c4, c5, projected = check_morse_boundary(pairs, critical)
    check_homology_crosscheck(by_size)
    chi = sum(((-1) ** (k - 1)) * len(v) for k, v in by_size.items())
    assert chi == 92
    print("faces", sum(len(v) for v in by_size.values()))
    print("face_counts", EXPECTED_FACE_COUNTS)
    print("hasse_covers", cover_count)
    print("matched_pairs", len(pairs))
    print("critical_by_dimension", EXPECTED_CRITICAL_BY_DIM)
    print("morse_boundary_C5_to_C4", f"zero {c4}x{c5}")
    print("projected_4_cells", projected)
    print("boundary_ranks_F2_F3", EXPECTED_BOUNDARY_RANKS)
    print("euler_characteristic", chi)
    print("D63_MIXED_WEDGE_VERIFY_OK")


if __name__ == "__main__":
    main()
