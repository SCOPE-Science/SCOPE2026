#!/usr/bin/env python3
"""Exact finite chain and equivariance certificate for Cov_{6,2}.

Run: python3 verify.py (Python 3 standard library only).
"""
from collections import Counter, defaultdict, deque
from functools import lru_cache
from itertools import combinations, permutations
from fractions import Fraction

N = 6
EDGES = tuple(combinations(range(N), 2))
EIDX = {e: i for i, e in enumerate(EDGES)}


def parity(seq):
    return -1 if sum(seq[i] > seq[j] for i in range(len(seq)) for j in range(i + 1, len(seq))) % 2 else 1


def boundaries(face):
    indices = [i for i in range(len(EDGES)) if face & (1 << i)]
    return [(face ^ (1 << j), (-1) ** i) for i, j in enumerate(indices)]


def build():
    faces = {0}
    covers = []
    for a, b in combinations(range(N), 2):
        allowed = [i for i, e in enumerate(EDGES) if a in e or b in e]
        cmask = sum(1 << i for i in allowed)
        covers.append(cmask)
        for sub in range(1, 1 << len(allowed)):
            faces.add(sum(1 << allowed[j] for j in range(len(allowed)) if sub >> j & 1))
    return faces, covers


def toggle_match(faces):
    residual = set(faces)
    lower, upper = {}, {}
    for i in range(len(EDGES)):
        b = 1 << i
        for f in tuple(sorted(residual)):
            if f in residual and not f & b and f | b in residual:
                residual.remove(f)
                residual.remove(f | b)
                lower[f] = f | b
                upper[f | b] = f
    return residual, lower, upper


def check_acyclic(faces, lower):
    indeg = {f: 0 for f in faces}
    outgoing = defaultdict(list)
    for higher in faces:
        for smaller, _ in boundaries(higher):
            if lower.get(smaller) == higher:
                src, dst = smaller, higher
            else:
                src, dst = higher, smaller
            outgoing[src].append(dst)
            indeg[dst] += 1
    ready = deque(f for f, d in indeg.items() if d == 0)
    count = 0
    while ready:
        f = ready.popleft()
        count += 1
        for g in outgoing[f]:
            indeg[g] -= 1
            if indeg[g] == 0:
                ready.append(g)
    assert count == len(faces), ('matching has closed gradient path', count, len(faces))
    return count


def projector(critical, lower, upper):
    @lru_cache(None)
    def project(t):
        if t in critical:
            return {t: 1}
        if t in upper:
            return {}
        mate = lower[t]
        pairs = dict(boundaries(mate))
        coeff = pairs.pop(t)
        assert abs(coeff) == 1
        result = defaultdict(int)
        for sub, sign in pairs.items():
            for q, value in project(sub).items():
                result[q] -= sign * coeff * value
        return {q: a for q, a in result.items() if a}
    return project


def cycle_five(T):
    """Alternating Hamilton-path chain on sorted 5-element vertex subset T."""
    c = defaultdict(int)
    for p in permutations(T):
        ei = [EIDX[tuple(sorted((p[j], p[j + 1])))] for j in range(4)]
        face = sum(1 << j for j in ei)
        sign = parity([T.index(x) for x in p]) * parity(ei)
        c[face] += sign
    assert all(a % 2 == 0 for a in c.values())
    return {f: a // 2 for f, a in c.items() if a}


def check_chain(chain):
    d = defaultdict(int)
    for face, a in chain.items():
        for sub, sign in boundaries(face):
            d[sub] += a * sign
    assert all(x == 0 for x in d.values())


def image(chain, project):
    out = defaultdict(int)
    for face, value in chain.items():
        for q, a in project(face).items():
            out[q] += value * a
    return {q: a for q, a in out.items() if a}


def rank(A):
    B = [[Fraction(x) for x in row] for row in A]
    rows = len(B); cols = len(B[0]) if B else 0; pivot = 0
    for j in range(cols):
        i = next((i for i in range(pivot, rows) if B[i][j]), None)
        if i is None: continue
        B[i], B[pivot] = B[pivot], B[i]
        q = B[pivot][j]
        for k in range(j, cols): B[pivot][k] /= q
        for t in range(pivot + 1, rows):
            v = B[t][j]
            if v:
                for k in range(j, cols): B[t][k] -= v * B[pivot][k]
        pivot += 1
        if pivot == rows: break
    return pivot


def det(A):
    n = len(A)
    assert all(len(row) == n for row in A)
    M = [row[:] for row in A]; den = 1; sgn = 1
    for k in range(n - 1):
        if M[k][k] == 0:
            i = next(i for i in range(k + 1, n) if M[i][k] != 0)
            M[i], M[k] = M[k], M[i]; sgn *= -1
        a = M[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = M[i][j] * a - M[i][k] * M[k][j]
                assert num % den == 0
                M[i][j] = num // den
            M[i][k] = 0
        den = a
    return sgn * M[-1][-1]


def cycle_four(U):
    six_edges = [i for i, e in enumerate(EDGES) if set(e).issubset(U)]
    assert len(six_edges) == 6
    return {sum(1 << e for e in six_edges if e != j): (-1) ** k for k, j in enumerate(six_edges)}


def class_characters(covers):
    char_table = []
    def parts(n, maxp=None):
        if n == 0:
            yield ()
            return
        for x in range(min(n, maxp if maxp else n), 0, -1):
            for t in parts(n - x, x): yield (x,) + t
    for cyc in parts(N):
        g = []
        k = 0
        for length in cyc:
            g.extend(list(range(k + 1, k + length)) + [k]); k += length
        remaining = set(range(len(EDGES)))
        orbits = []
        while remaining:
            q = next(iter(remaining)); orbit_mask = 0
            while q in remaining:
                remaining.remove(q)
                orbit_mask |= 1 << q
                a,b = EDGES[q]
                q = EIDX[tuple(sorted((g[a],g[b])))]
            orbits.append(orbit_mask)
        total = 0
        for bits in range(1 << len(orbits)):
            mask = 0
            for j, a in enumerate(orbits):
                if bits >> j & 1: mask |= a
            if any(mask & ~c == 0 for c in covers):
                total += (-1) ** bits.bit_count()
        reduced_lefschetz = -total
        fixed4 = sum(set(g[i] for i in U) == set(U) for U in combinations(range(N),4))
        sign = (-1) ** (N - len(cyc))
        claimed_h3 = sign * (cyc.count(1) - 1)
        assert fixed4 - reduced_lefschetz == claimed_h3, (cyc, fixed4, reduced_lefschetz, claimed_h3)
        char_table.append((cyc, fixed4, reduced_lefschetz, claimed_h3))
    assert len(char_table) == 11
    return char_table



def check_equivariance():
    """Check signed chain-level action for all adjacent transpositions."""
    def transport(chain, g):
        out = defaultdict(int)
        for f,a in chain.items():
            old_idx = [j for j in range(len(EDGES)) if f & 1 << j]
            new_idx = [EIDX[tuple(sorted((g[EDGES[j][0]],g[EDGES[j][1]])))] for j in old_idx]
            out[sum(1 << j for j in new_idx)] += a * parity(new_idx)
        return {q:a for q,a in out.items() if a}
    for i in range(N - 1):
        g = list(range(N));g[i],g[i+1] = g[i+1],g[i]
        for T in combinations(range(N),5):
            sorted_image = tuple(sorted(g[x] for x in T))
            coefficient = parity([sorted_image.index(g[x]) for x in T])
            lhs = transport(cycle_five(T),g)
            rhs = {f:coefficient*a for f,a in cycle_five(sorted_image).items()}
            assert lhs == rhs, (i,T)
    return 30

def main():
    faces,covers = build()
    count = Counter(f.bit_count() - 1 for f in faces if f)
    assert len(faces) == 5142, count
    critical, lower, upper = toggle_match(faces)
    assert len(lower) == len(upper) == 2561
    crit3 = sorted(f for f in critical if f.bit_count() == 4)
    crit4 = sorted(f for f in critical if f.bit_count() == 5)
    assert len(crit3) == 5 and len(crit4) == 15 and len(critical) == 20
    check_acyclic(faces, lower)
    project = projector(critical, lower, upper)
    FIV = []
    for T in combinations(range(N), 5):
        z = cycle_five(T)
        check_chain(z)
        im = image(z, project)
        FIV.append([im.get(q, 0) for q in crit3])
    assert rank(FIV) == 5
    assert all(sum((-1) ** i * FIV[i][j] for i in range(6)) == 0 for j in range(5))
    FOUR = []
    for U in combinations(range(N), 4):
        z = cycle_four(U)
        check_chain(z)
        im = image(z, project)
        FOUR.append([im.get(q, 0) for q in crit4])
    determinant = det(FOUR)
    assert abs(determinant) == 1, determinant
    for q in crit4:
        boundary = defaultdict(int)
        for t,sign in boundaries(q):
            for r,a in project(t).items(): boundary[r] += sign * a
        assert not any(boundary.values())
    symmetry_checks = check_equivariance()
    characters = class_characters(covers)
    print('FACE_VECTOR', dict(sorted(count.items())))
    print('MATCHING_ACYCLIC', len(faces), 'PAIRS', len(lower), 'CRITICAL_3',len(crit3),'CRITICAL_4',len(crit4))
    print('FIVE_SUBSET_IMAGE_MATRIX', FIV)
    print('FIVE_SUBSET_IMAGE_RANK', rank(FIV), 'ALTERNATING_RELATION_VERIFIED', True)
    print('FOUR_SUBSET_MATRIX_DETERMINANT', determinant)
    print('CHAIN_EQUIVARIANCE',symmetry_checks,'ADJACENT_TRANSPOSITION_TESTS')
    print('S6_CHARACTERS', characters)
    print('VERIFY_OK')

if __name__ == '__main__': main()
