from itertools import product, combinations, permutations
from hashlib import sha256

Q = range(3)
WORDS = list(product(Q, repeat=3))
INDEX = {w:i for i,w in enumerate(WORDS)}


def in_descendant(x, a, b):
    return all(x[j] == a[j] or x[j] == b[j] for j in range(3))


def is_frameproof(indices):
    code = [WORDS[i] for i in indices]
    for x in code:
        others = [y for y in code if y != x]
        for a, b in combinations(others, 2):
            if in_descendant(x, a, b):
                return False
    return True

# A triple is forbidden exactly when one member is a descendant of the other two.
PAIR_FORBID = {(i,j):0 for i in range(27) for j in range(i+1,27)}
bad_triples = 0
for tri in combinations(range(27),3):
    ws = [WORDS[i] for i in tri]
    if any(in_descendant(ws[k], ws[(k+1)%3], ws[(k+2)%3]) for k in range(3)):
        bad_triples += 1
        a,b,c = tri
        PAIR_FORBID[(a,b)] |= 1 << c
        PAIR_FORBID[(a,c)] |= 1 << b
        PAIR_FORBID[(b,c)] |= 1 << a


def enumerate_size(k):
    out = []
    nodes = 0
    def dfs(chosen, candidates):
        nonlocal nodes
        nodes += 1
        need = k - len(chosen)
        if need == 0:
            out.append(tuple(chosen))
            return
        if candidates.bit_count() < need:
            return
        rem = candidates
        while rem:
            bit = rem & -rem
            v = bit.bit_length() - 1
            rem ^= bit
            if rem.bit_count() < need - 1:
                break
            newrem = rem
            for u in chosen:
                newrem &= ~PAIR_FORBID[(min(u,v), max(u,v))]
            dfs(chosen + [v], newrem)
    dfs([], (1 << 27) - 1)
    return out, nodes

size10, nodes10 = enumerate_size(10)
size9, nodes9 = enumerate_size(9)
assert len(size10) == 0
assert len(size9) == 12
assert all(is_frameproof(S) for S in size9)
MAXIMA = {frozenset(S) for S in size9}

# Every equality case has bijective projection on each coordinate pair.
for S in MAXIMA:
    for a,b in ((0,1),(0,2),(1,2)):
        assert len({(WORDS[i][a], WORDS[i][b]) for i in S}) == 9

# Independently enumerate all Latin squares of order 3 and compare their graphs.
PERMS = list(permutations(Q))
latin_graphs = set()
for rows in product(PERMS, repeat=3):
    if all(len({rows[r][c] for r in Q}) == 3 for c in Q):
        latin_graphs.add(frozenset(INDEX[(r,c,rows[r][c])] for r in Q for c in Q))
assert len(latin_graphs) == 12
assert latin_graphs == MAXIMA

# Natural Hamming-isometry group: independent symbol permutations and coordinate permutations.
coord_perms = list(permutations(range(3)))
rep = min(MAXIMA, key=lambda S: tuple(sorted(S)))
orbit = set()
stabilizer = 0
for ps in product(PERMS, repeat=3):
    for cp in coord_perms:
        image = []
        for i in rep:
            w = WORDS[i]
            tmp = tuple(ps[j][w[j]] for j in range(3))
            z = tuple(tmp[cp[j]] for j in range(3))
            image.append(INDEX[z])
        T = frozenset(image)
        orbit.add(T)
        if T == rep:
            stabilizer += 1
assert len(PERMS)**3 * len(coord_perms) == 1296
assert orbit == MAXIMA
assert stabilizer == 108

# Stable census digest: one line per maximum, words lexicographically ordered.
lines = []
for S in sorted(MAXIMA, key=lambda s: tuple(sorted(s))):
    lines.append(','.join(''.join(map(str, WORDS[i])) for i in sorted(S)))
census = ('\n'.join(lines) + '\n').encode('ascii')
digest = sha256(census).hexdigest()
rep_words = ','.join(''.join(map(str, WORDS[i])) for i in sorted(rep))
print('VERIFY_OK')
print('bad_triples', bad_triples)
print('maximum', 9)
print('size10', len(size10), 'nodes10', nodes10)
print('labeled_maxima', len(MAXIMA), 'nodes9', nodes9)
print('latin_graphs', len(latin_graphs))
print('natural_group', 1296, 'orbits', 1, 'orbit_size', len(orbit), 'stabilizer', stabilizer)
print('representative', rep_words)
print('census_sha256', digest)
