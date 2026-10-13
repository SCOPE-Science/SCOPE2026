from collections import defaultdict
from itertools import product
from math import comb

P = 5
EW = (0, 1, 4, 4, 1)

# Representatives for F_5^2\{0} modulo multiplication by +/-1.
REPS = (
    (0,1),(0,2),(1,0),(2,0),(1,2),(2,4),
    (1,4),(2,3),(1,3),(2,1),(1,1),(2,2),
)

ETA_C = (0,0,0,0,0,0,0,1,1,1,4,2)
ETA_D = (0,0,0,0,0,1,2,1,2,0,0,3)
G_C = (
    (2,1,2,1,1,1,1,2,2),
    (3,3,1,1,1,1,1,2,2),
)
G_D = (
    (2,1,1,2,1,1,2,2,2),
    (4,4,4,3,3,3,2,2,2),
)
EXPECTED_PRIMAL = {
    0:1, 6:2, 9:2, 13:2, 17:2, 18:2, 21:4,
    22:2, 23:2, 24:4, 27:2,
}


def rank2(cols):
    if not cols:
        return 0
    first = None
    for v in cols:
        if v != (0,0):
            first = v
            break
    if first is None:
        return 0
    for v in cols:
        if (first[0]*v[1] - first[1]*v[0]) % P:
            return 2
    return 1


def columns_from_eta(eta):
    out = []
    for rep, mult in zip(REPS, eta):
        out.extend([rep] * mult)
    return out


def columns_from_matrix(G):
    return [(G[0][j] % P, G[1][j] % P) for j in range(len(G[0]))]


def canonical_rep(v):
    if v == (0,0):
        raise ValueError("zero column has no effective representative")
    for r in REPS:
        if v == r or v == ((-r[0]) % P, (-r[1]) % P):
            return r
    raise AssertionError(v)


def eta_from_matrix(G):
    index = {r:i for i,r in enumerate(REPS)}
    eta = [0]*len(REPS)
    for v in columns_from_matrix(G):
        eta[index[canonical_rep(v)]] += 1
    return tuple(eta)


def primal_enum_from_columns(cols):
    out = defaultdict(int)
    for a,b in product(range(P), repeat=2):
        w = 0
        for x,y in cols:
            w += EW[(a*x + b*y) % P]
        out[w] += 1
    return dict(sorted(out.items()))


def primal_signature_from_eta(eta):
    # Sorted weights of the 24 nonzero messages; this is equivalent to the enumerator.
    weights = []
    for a,b in product(range(P), repeat=2):
        if a == 0 and b == 0:
            continue
        w = 0
        for mult,(x,y) in zip(eta,REPS):
            if mult:
                w += mult * EW[(a*x + b*y) % P]
        weights.append(w)
    return tuple(sorted(weights))


def dual_a2_from_eta(eta):
    return 2 * sum(comb(m,2) for m in eta)


def dual_enum_dp(cols):
    # Count all vectors x by syndrome sum_j x_j g_j and Euclidean weight.
    dp = {(0,0,0): 1}
    for gx,gy in cols:
        nd = defaultdict(int)
        for (sx,sy,w), count in dp.items():
            for a in range(P):
                nd[((sx + a*gx) % P, (sy + a*gy) % P, w + EW[a])] += count
        dp = nd
    out = defaultdict(int)
    for (sx,sy,w), count in dp.items():
        if sx == 0 and sy == 0:
            out[w] += count
    return dict(sorted(out.items()))


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total-x, parts-1, prefix+(x,))


# Direct checks of the displayed pair.
assert len(G_C) == len(G_D) == 2
assert len(G_C[0]) == len(G_C[1]) == len(G_D[0]) == len(G_D[1]) == 9
assert rank2(columns_from_matrix(G_C)) == rank2(columns_from_matrix(G_D)) == 2
assert eta_from_matrix(G_C) == ETA_C
assert eta_from_matrix(G_D) == ETA_D

Ccols = columns_from_matrix(G_C)
Dcols = columns_from_matrix(G_D)
assert primal_enum_from_columns(Ccols) == EXPECTED_PRIMAL
assert primal_enum_from_columns(Dcols) == EXPECTED_PRIMAL
assert dual_a2_from_eta(ETA_C) == 14
assert dual_a2_from_eta(ETA_D) == 10

Cdual = dual_enum_dp(Ccols)
Ddual = dual_enum_dp(Dcols)
assert sum(Cdual.values()) == sum(Ddual.values()) == 5**7
assert Cdual.get(2,0) == 14
assert Ddual.get(2,0) == 10
assert Cdual != Ddual

# Exhaustive sharpness check for every effective two-dimensional code of length <= 8.
# After coordinate sign changes and permutation, every nonzero generator column is
# represented by one of REPS, hence by a 12-part multiplicity vector eta.
state_counts = {}
for n in range(2, 9):
    seen = {}
    full_rank_states = 0
    for eta in compositions(n, len(REPS)):
        cols = [REPS[i] for i,m in enumerate(eta) if m]
        if rank2(cols) != 2:
            continue
        full_rank_states += 1
        sig = primal_signature_from_eta(eta)
        a2 = dual_a2_from_eta(eta)
        old = seen.get(sig)
        if old is None:
            seen[sig] = a2
        else:
            assert old == a2, (n, eta, old, a2)
    state_counts[n] = full_rank_states

assert state_counts == {2:60,3:340,4:1335,5:4332,6:12334,7:31776,8:75528}

# The explicit length-9 pair is a collision of primal signatures with distinct dual A_2.
assert primal_signature_from_eta(ETA_C) == primal_signature_from_eta(ETA_D)
assert dual_a2_from_eta(ETA_C) != dual_a2_from_eta(ETA_D)

print("VERIFY_OK")
