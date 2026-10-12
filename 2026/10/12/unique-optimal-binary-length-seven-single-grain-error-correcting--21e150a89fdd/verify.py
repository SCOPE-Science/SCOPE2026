#!/usr/bin/env python3
"""Exact length-seven single-grain code census (standard-library only).

Physical coordinates are numbered 0,...,6 from left to right. Integer
bit i represents physical coordinate i (least significant bit first).
"""

from itertools import combinations

N = 7
HALF = 1 << (N - 1)
FULL = 1 << N


def received_direct(word):
    bits = tuple((word >> i) & 1 for i in range(N))
    outcomes = {bits}
    for i in range(1, N):
        outcomes.add(bits[:i] + (bits[i - 1],) + bits[i + 1:])
    return {sum(v << i for i, v in enumerate(bits_out)) for bits_out in outcomes}


def received_transition(word):
    outcomes = {word}
    for i in range(1, N):
        if ((word >> i) & 1) != ((word >> (i - 1)) & 1):
            outcomes.add(word ^ (1 << i))
    return outcomes


# Every physical channel ball is independently reconstructed two ways.
BALLS = []
for word in range(FULL):
    a = received_direct(word)
    b = received_transition(word)
    assert a == b
    assert all((received & 1) == (word & 1) for received in a)
    BALLS.append(frozenset(a))

# The graph contains only the 64 words whose physical coordinate 0 is zero;
# even integer 2*j maps to branch vertex j.
COMPAT = [0] * HALF
conflicts = 0
for j in range(HALF):
    for k in range(HALF):
        if j == k:
            continue
        if BALLS[2 * j].isdisjoint(BALLS[2 * k]):
            COMPAT[j] |= 1 << k
        elif k > j:
            conflicts += 1
assert conflicts == 432
assert sum(a.bit_count() for a in COMPAT) // 2 == 1584

# Every distinct pair in opposite first-coordinate branches is compatible.
assert all(BALLS[2 * j].isdisjoint(BALLS[2 * k + 1])
           for j in range(HALF) for k in range(HALF))

# Bitwise global complementation conjugates one branch to the other.
assert all({x ^ 127 for x in BALLS[2 * j]} == BALLS[(2 * j) ^ 127]
           for j in range(HALF))

# A complete Bron--Kerbosch recursion with pivoting. Its cardinality prune
# discards only branches incapable of containing a clique of size >=13.
full_candidates = (1 << HALF) - 1
bk_nodes = 0
bk_solutions = set()


def bron_kerbosch(R, P, X):
    global bk_nodes
    bk_nodes += 1
    if len(R) + P.bit_count() < 13:
        return
    if not P and not X:
        if len(R) >= 13:
            bk_solutions.add(tuple(sorted(R)))
        return
    U = P | X
    if U:
        pivot = max((v for v in range(HALF) if (U >> v) & 1),
                    key=lambda v: (P & COMPAT[v]).bit_count())
        Q = P & ~COMPAT[pivot]
    else:
        Q = P
    while Q:
        bit = Q & -Q
        v = bit.bit_length() - 1
        Q ^= bit
        bron_kerbosch(R + (v,), P & COMPAT[v], X & COMPAT[v])
        P ^= bit
        X |= bit


bron_kerbosch((), full_candidates, 0)
assert len(bk_solutions) == 1

# Independent increasing-vertex clique enumeration. Greedy coloring of the
# induced candidate graph partitions it into independent color classes, so
# the number of colors is an honest upper bound on its clique number.
def coloring_upper_bound(P):
    colors = 0
    while P:
        colors += 1
        independent = 0
        available = P
        while available:
            bit = available & -available
            v = bit.bit_length() - 1
            independent |= bit
            available &= ~(bit | COMPAT[v])
        P &= ~independent
    return colors


def fixed_size_cliques(target):
    found = set()
    calls = 0

    def extend(chosen, candidates, missing):
        nonlocal calls
        calls += 1
        if missing == 0:
            found.add(chosen)
            return
        if candidates.bit_count() < missing or coloring_upper_bound(candidates) < missing:
            return
        while candidates and candidates.bit_count() >= missing:
            if coloring_upper_bound(candidates) < missing:
                break
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            candidates ^= bit
            extend(chosen + (v,), candidates & COMPAT[v], missing - 1)

    extend((), full_candidates, target)
    return found, calls


thirteen, nodes13 = fixed_size_cliques(13)
fourteen, nodes14 = fixed_size_cliques(14)
assert thirteen == bk_solutions
assert not fourteen
assert len(thirteen) == 1

# Canonical branch and global maximum, in true physical order.
J = tuple(sorted(next(iter(thirteen))))
EXPECTED_J = (0, 3, 6, 9, 21, 28, 31, 42, 45, 48, 51, 54, 57)
assert J == EXPECTED_J
LOWER_HALF = frozenset(2 * j for j in J)
UPPER_HALF = frozenset(x ^ 127 for x in LOWER_HALF)
CODE = LOWER_HALF | UPPER_HALF
assert len(CODE) == 26
assert all(BALLS[x].isdisjoint(BALLS[y]) for x, y in combinations(sorted(CODE), 2))
assert sum(len(BALLS[x] & BALLS[y]) > 0 for x in range(FULL)
           for y in range(x + 1, FULL)) == 864


def bitstring(x):
    return ''.join(str((x >> i) & 1) for i in range(N))


print('CHANNEL_OK ambient=128 independent_ball_formulations=true first_bit_preserved=true')
print('BRANCH_OK vertices=64 confusability_edges=432 compatibility_edges=1584')
print('EXHAUSTIVE_OK BK_nodes=%d ordered13_nodes=%d ordered14_nodes=%d' %
      (bk_nodes, nodes13, nodes14))
print('LOWER_HALF', ','.join(bitstring(x) for x in sorted(LOWER_HALF)))
print('GLOBAL_CODE', ','.join(bitstring(x) for x in sorted(CODE)))
print('VERIFY_OK maximum=26 labeled_maxima=1 branch_maximum=13 branch_maxima=1 complementary_halves=true')
