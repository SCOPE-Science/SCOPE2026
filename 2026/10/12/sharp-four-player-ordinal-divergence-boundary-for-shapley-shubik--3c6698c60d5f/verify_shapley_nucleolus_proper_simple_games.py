#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations, permutations
from collections import Counter
import math


def antichains(n):
    subsets = list(range(1, 1 << n))
    for mask in range(1, 1 << len(subsets)):
        fam = [subsets[i] for i in range(len(subsets)) if (mask >> i) & 1]
        if all(not ((a & b) == a or (a & b) == b)
               for i, a in enumerate(fam) for b in fam[i+1:]):
            yield tuple(fam)


def value(fam, S):
    return int(any((m & S) == m for m in fam))


def proper(n, fam):
    N = (1 << n) - 1
    return all(not (value(fam, S) and value(fam, N ^ S)) for S in range(1 << n))


def shapley_shubik(n, fam):
    ans = [Fraction(0) for _ in range(n)]
    nf = math.factorial(n)
    for i in range(n):
        for S in range(1 << n):
            if (S >> i) & 1:
                continue
            if value(fam, S | (1 << i)) != value(fam, S):
                k = S.bit_count()
                ans[i] += Fraction(math.factorial(k) * math.factorial(n-k-1), nf)
    return tuple(ans)


def relabel_family(fam, p):
    out = []
    for S in fam:
        T = 0
        for i in range(len(p)):
            if (S >> i) & 1:
                T |= 1 << p[i]
        out.append(T)
    return tuple(sorted(out))


def canonical_family(fam, n):
    return min(relabel_family(fam, p) for p in permutations(range(n)))


def automorphisms(fam, n):
    return tuple(p for p in permutations(range(n)) if relabel_family(fam, p) == fam)


def veto_players(n, fam):
    wins = [S for S in range(1 << n) if value(fam, S)]
    return tuple(i for i in range(n) if all((S >> i) & 1 for S in wins))


def solve_unique(A, b, nvars):
    M = [list(map(Fraction, row)) + [Fraction(bb)] for row, bb in zip(A, b)]
    r = 0
    piv = []
    for c in range(nvars):
        p = next((i for i in range(r, len(M)) if M[i][c]), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        z = M[r][c]
        M[r] = [x / z for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                z = M[i][c]
                M[i] = [M[i][j] - z * M[r][j] for j in range(nvars + 1)]
        piv.append(c)
        r += 1
    for row in M:
        if all(row[c] == 0 for c in range(nvars)) and row[nvars] != 0:
            return None
    if len(piv) != nvars:
        return None
    x = [Fraction(0)] * nvars
    for i, c in enumerate(piv):
        x[c] = M[i][nvars]
    return tuple(x)


def least_core_vertices(n, fam):
    # One exact rational LP: minimize epsilon over imputations.
    # Enumerate all vertices of the bounded optimal polytope.
    N = (1 << n) - 1
    coalitions = [S for S in range(1, N)]
    nvars = n + 1
    eqA = [[Fraction(1)] * n + [Fraction(0)]]
    eqb = [Fraction(1)]
    inequalities = []
    for S in coalitions:
        row = [Fraction(-1) if (S >> i) & 1 else Fraction(0) for i in range(n)] + [Fraction(-1)]
        inequalities.append((row, Fraction(-value(fam, S))))
    for i in range(n):
        row = [Fraction(0)] * (n + 1)
        row[i] = Fraction(-1)
        inequalities.append((row, Fraction(-value(fam, 1 << i))))

    vertices = set()
    # Sum equality has rank one, so a vertex uses n further independent tight inequalities.
    for inds in combinations(range(len(inequalities)), n):
        A = list(eqA)
        b = list(eqb)
        for j in inds:
            A.append(inequalities[j][0])
            b.append(inequalities[j][1])
        sol = solve_unique(A, b, nvars)
        if sol is None:
            continue
        if any(sum(a*x for a, x in zip(row, sol)) > bb for row, bb in inequalities):
            continue
        vertices.add(sol)
    assert vertices
    eps = min(z[-1] for z in vertices)
    opt = sorted(z for z in vertices if z[-1] == eps)
    return eps, tuple(opt)


def weak_order(v):
    return tuple((v[i] > v[j]) - (v[i] < v[j])
                 for i in range(len(v)) for j in range(i+1, len(v)))


def fixed_by_automorphisms(x, auts):
    return all(tuple(x[p[i]] for i in range(len(x))) == tuple(x) for p in auts)


# Canonical nucleolus table. Each entry is certified below either by the core-veto
# characterization or by an exact least-core vertex computation plus symmetry.
NUC = {
    1: {(1,): (Fraction(1),)},
    2: {
        (1,): (Fraction(1), Fraction(0)),
        (3,): (Fraction(1,2), Fraction(1,2)),
    },
    3: {
        (1,): (Fraction(1), Fraction(0), Fraction(0)),
        (3,): (Fraction(1,2), Fraction(1,2), Fraction(0)),
        (3,5): (Fraction(1), Fraction(0), Fraction(0)),
        (3,5,6): (Fraction(1,3), Fraction(1,3), Fraction(1,3)),
        (7,): (Fraction(1,3), Fraction(1,3), Fraction(1,3)),
    },
    4: {
        (1,): (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (3,): (Fraction(1,2), Fraction(1,2), Fraction(0), Fraction(0)),
        (3,5): (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (3,5,6): (Fraction(1,3), Fraction(1,3), Fraction(1,3), Fraction(0)),
        (3,5,9): (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (3,5,9,14): (Fraction(2,5), Fraction(1,5), Fraction(1,5), Fraction(1,5)),
        (3,5,14): (Fraction(1,3), Fraction(1,3), Fraction(1,3), Fraction(0)),
        (3,13): (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (3,13,14): (Fraction(1,3), Fraction(1,3), Fraction(1,6), Fraction(1,6)),
        (7,): (Fraction(1,3), Fraction(1,3), Fraction(1,3), Fraction(0)),
        (7,11): (Fraction(1,2), Fraction(1,2), Fraction(0), Fraction(0)),
        (7,11,13): (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        (7,11,13,14): (Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(1,4)),
        (15,): (Fraction(1,4), Fraction(1,4), Fraction(1,4), Fraction(1,4)),
    },
}

# Enumerate all proper games and their isomorphism orbits.
ORBIT_COUNTS = {}
for n in (1,2,3,4):
    oc = Counter()
    for fam in antichains(n):
        if proper(n, fam):
            oc[canonical_family(fam, n)] += 1
    ORBIT_COUNTS[n] = oc
    assert set(oc) == set(NUC[n])

assert {n: sum(ORBIT_COUNTS[n].values()) for n in ORBIT_COUNTS} == {1:1,2:3,3:11,4:80}

# Certify the nucleolus table.
for n in (1,2,3,4):
    for fam in NUC[n]:
        eta = NUC[n][fam]
        assert sum(eta) == 1
        assert all(x >= value(fam, 1 << i) for i, x in enumerate(eta))
        auts = automorphisms(fam, n)
        assert fixed_by_automorphisms(eta, auts)
        veto = veto_players(n, fam)
        if veto:
            # In a simple game with veto players, every core allocation gives zero
            # to non-veto players and distributes the unit payoff among veto players.
            # The nucleolus lies in the core. For every canonical core case here,
            # automorphisms act transitively on the veto set, so the unique invariant
            # core point is equal division among veto players.
            for i in range(n):
                assert eta[i] == (Fraction(1, len(veto)) if i in veto else 0)
            assert all(any(p[i] == j for p in auts) for i in veto for j in veto)
        else:
            eps, opt = least_core_vertices(n, fam)
            opt_x = tuple(z[:-1] for z in opt)
            if len(set(opt_x)) == 1:
                # Singleton least core, hence it is the nucleolus.
                assert eta == opt_x[0]
            else:
                # The only non-singleton least-core case among the canonical games
                # through four players is (3,13,14): its two extreme points are
                # interchanged by the player-2/player-3 symmetry, and the unique
                # symmetry-fixed point of the segment is the stated nucleolus.
                assert n == 4 and fam == (3,13,14)
                assert len(set(opt_x)) == 2
                a, b = sorted(set(opt_x))
                mid = tuple((a[i] + b[i]) / 2 for i in range(n))
                assert eta == mid

# Compute exact Shapley-Shubik/nucleolus ranking divergence orbitwise.
divergence_counts = {}
divergent_orbits = Counter()
for n in (1,2,3,4):
    d = 0
    for fam, orbit_size in ORBIT_COUNTS[n].items():
        phi = shapley_shubik(n, fam)
        eta = NUC[n][fam]
        if weak_order(phi) != weak_order(eta):
            d += orbit_size
            if n == 4:
                divergent_orbits[fam] = orbit_size
    divergence_counts[n] = d

assert divergence_counts == {1:0,2:0,3:0,4:36}
assert divergent_orbits == Counter({(3,5):12, (3,5,14):12, (3,13):12})

assert shapley_shubik(4,(3,5)) == (Fraction(2,3),Fraction(1,6),Fraction(1,6),Fraction(0))
assert shapley_shubik(4,(3,5,14)) == (Fraction(5,12),Fraction(1,4),Fraction(1,4),Fraction(1,12))
assert shapley_shubik(4,(3,13)) == (Fraction(7,12),Fraction(1,4),Fraction(1,12),Fraction(1,12))

# Dummy-free refinement.
def dummy_count(n, fam):
    return sum(x == 0 for x in shapley_shubik(n, fam))

proper_nodummy = 0
divergent_nodummy = 0
nodummy_orbits = Counter()
for fam, orbit_size in ORBIT_COUNTS[4].items():
    if dummy_count(4, fam):
        continue
    proper_nodummy += orbit_size
    if weak_order(shapley_shubik(4,fam)) != weak_order(NUC[4][fam]):
        divergent_nodummy += orbit_size
        nodummy_orbits[fam] = orbit_size

assert proper_nodummy == 50
assert divergent_nodummy == 24
assert nodummy_orbits == Counter({(3,5,14):12, (3,13):12})

print('VERIFY_OK')
print('proper_counts', {n:sum(ORBIT_COUNTS[n].values()) for n in ORBIT_COUNTS})
print('proper_isomorphism_classes', {n:len(ORBIT_COUNTS[n]) for n in ORBIT_COUNTS})
print('divergence_counts', divergence_counts)
print('divergent_orbits', dict(divergent_orbits))
for fam in sorted(divergent_orbits):
    print('orbit', fam, 'size', divergent_orbits[fam],
          'shapley_shubik', shapley_shubik(4,fam), 'nucleolus', NUC[4][fam])
print('proper_nodummy', proper_nodummy)
print('divergent_nodummy', divergent_nodummy)
print('nodummy_orbits', dict(nodummy_orbits))
