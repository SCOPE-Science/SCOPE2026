"""Exact finite certificate for mobile domination on the Pappus incidence graph.

Usage: python3 verify_incidence.py
Uses only the Python standard library. Vertex labels are defined below.
"""
from itertools import combinations, product

Q = range(3)
N_VERT = 18
VERT = range(N_VERT)
ALL = (1 << N_VERT) - 1
P = lambda x, y: 3 * (x % 3) + (y % 3)
L = lambda m, b: 9 + 3 * (m % 3) + (b % 3)
EDGES = {tuple(sorted((P(x, m*x+b), L(m, b))))
         for x, m, b in product(Q, repeat=3)}
assert len(EDGES) == 27
CLOSED = [1 << v for v in VERT]
for a, b in EDGES:
    CLOSED[a] |= 1 << b
    CLOSED[b] |= 1 << a
assert all(t.bit_count() == 4 for t in CLOSED)


def dominating(mask):
    cover = 0
    while mask:
        u = (mask & -mask).bit_length() - 1
        mask &= mask - 1
        cover |= CLOSED[u]
    return cover == ALL


def all_sets(k):
    return [sum(1 << v for v in sub) for sub in combinations(VERT, k)
            if dominating(sum(1 << v for v in sub))]


def possible_destinations(mask, valid):
    """Enumerate injective one-step guard moves, including staying put."""
    positions = tuple(v for v in VERT if mask & (1 << v))
    dest = set()

    def visit(i, taken):
        if i == len(positions):
            if taken in valid:
                dest.add(taken)
            return
        choices = CLOSED[positions[i]] & ~taken
        while choices:
            bit = choices & -choices
            choices ^= bit
            visit(i + 1, taken | bit)

    visit(0, 0)
    return dest


def apply_perm(mask, perm):
    return sum(1 << perm(v) for v in VERT if mask & (1 << v))


def F(v):
    if v < 9:
        x, y = divmod(v, 3)
        return P(x+1, y+x)
    m, b = divmod(v-9, 3)
    return L(m+1, b-m-1)


def G(v):
    if v < 9:
        x, y = divmod(v, 3)
        return P(x, y+1)
    m, b = divmod(v-9, 3)
    return L(m, b+1)


def D(v):
    if v < 9:
        x, y = divmod(v, 3)
        return L(x, -y)
    m, b = divmod(v-9, 3)
    return P(m, -b)


def verify_automorphism(f):
    assert set(f(v) for v in VERT) == set(VERT)
    assert {tuple(sorted((f(a), f(b)))) for a, b in EDGES} == EDGES

for perm in (F, G, D):
    verify_automorphism(perm)
assert all(F(F(F(v))) == v and G(G(G(v))) == v and D(D(v)) == v for v in VERT)
assert all(F(G(v)) == G(F(v)) for v in VERT)
assert all(D(F(D(v))) == G(F(v)) for v in VERT)
assert all(D(G(D(v))) == G(G(v)) for v in VERT)

assert len(all_sets(4)) == 0
S5 = all_sets(5)
S6 = all_sets(6)
assert len(S5) == 18 and len(S6) == 423

orbit = {S5[0]}
frontier = [S5[0]]
while frontier:
    state = frontier.pop()
    for f in (F, G, D):
        nxt = apply_perm(state, f)
        if nxt not in orbit:
            orbit.add(nxt)
            frontier.append(nxt)
assert orbit == set(S5)
# F, G act regularly on each incidence side and D interchanges the sides;
# hence the generated order-18 subgroup acts regularly on vertices.
assert len({apply_perm(1, f) for f in (F, G, D)}) == 3

def assess(states):
    allowed = set(states)
    attack_count = 0
    bad_vertices = []
    min_options = 10**9
    max_options = 0
    shifts = 0
    for state in states:
        targets = possible_destinations(state, allowed)
        shifts += len(targets)
        nonoccupied = ALL & ~state
        cannot = set()
        while nonoccupied:
            bit = nonoccupied & -nonoccupied
            nonoccupied ^= bit
            v = bit.bit_length()-1
            count = sum(bool(t & bit) for t in targets)
            attack_count += 1
            min_options = min(min_options, count)
            max_options = max(max_options, count)
            if count == 0:
                cannot.add(v)
        bad_vertices.append(cannot)
    return shifts, attack_count, bad_vertices, min_options, max_options

sh5, a5, bad5, mi5, ma5 = assess(S5)
assert sh5 == 234 and a5 == 234
assert all(len(t) == 1 for t in bad5)
assert {next(iter(t)) for t in bad5} == set(VERT)
sh6, a6, bad6, mi6, ma6 = assess(S6)
assert sh6 == 72891 and a6 == 5076
assert all(not t for t in bad6)
assert (mi6, ma6) == (25, 81)
print('PAPPUS_INCIDENCE_OK vertices=18 edges=27')
print('domination_sizes_4_5_6=0,18,423')
print('five_minima_one_orbit=18')
print('five_shift_pairs=234 five_attack_pairs=234')
print('five_each_one_undefeatable_attack=18 bijective_attack_labels=18')
print('six_shift_pairs=72891 six_attack_pairs=5076')
print('six_every_attack_defensible=5076 options_min_max=25,81')
print('m_eternal_domination=6 ordinary_domination=5')
print('VERIFY_OK')
