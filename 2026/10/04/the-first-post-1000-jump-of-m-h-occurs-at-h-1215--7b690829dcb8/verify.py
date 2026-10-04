from collections import defaultdict
from math import gcd

H = 1215


def spf_sieve(n):
    spf = list(range(n + 1))
    if n >= 1:
        spf[1] = 1
    i = 2
    while i * i <= n:
        if spf[i] == i:
            for j in range(i * i, n + 1, i):
                if spf[j] == j:
                    spf[j] = i
        i += 1
    return spf


spf = spf_sieve(H + 1)
primes = [p for p in range(2, H + 2) if spf[p] == p]
pindex = {p: i for i, p in enumerate(primes)}


def factor_vector(n):
    out = {}
    while n > 1:
        p = spf[n]
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        out[pindex[p]] = e
    return out


vectors = [None] + [factor_vector(n) for n in range(1, H + 2)]


def plane_key(a, b):
    """Primitive Pluecker coordinates for span_Q(v(a),v(b)); None iff dependent."""
    va, vb = vectors[a], vectors[b]
    inds = sorted(set(va) | set(vb))
    vals = []
    for pos, i in enumerate(inds):
        for j in inds[pos + 1:]:
            z = va.get(i, 0) * vb.get(j, 0) - va.get(j, 0) * vb.get(i, 0)
            if z:
                vals.append((i, j, z))
    if not vals:
        return None
    g = 0
    for _, _, z in vals:
        g = gcd(g, abs(z))
    vals = [(i, j, z // g) for i, j, z in vals]
    if vals[0][2] < 0:
        vals = [(i, j, -z) for i, j, z in vals]
    return tuple(vals)


def maximal_rank_dependent(a, b, c):
    k = plane_key(a, b)
    return k is not None and plane_key(a, c) == k and plane_key(b, c) == k


# Every unordered maximal-rank dependent triple is a triangle in exactly one
# plane-key edge graph. This is an exact finite enumeration, not a relation-
# exponent search.
groups = defaultdict(list)
for a in range(2, H + 1):
    for b in range(a + 1, H + 1):
        k = plane_key(a, b)
        if k is not None:
            groups[k].append((a, b))

candidates = set()
for edges in groups.values():
    if len(edges) < 3:
        continue
    adj = defaultdict(set)
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    for a in sorted(adj):
        higher = {b for b in adj[a] if b > a}
        for b in sorted(higher):
            for c in adj[b]:
                if c > b and c in higher:
                    candidates.add((a, b, c))

consecutive = sorted(
    [t for t in candidates if maximal_rank_dependent(t[0] + 1, t[1] + 1, t[2] + 1)],
    key=lambda t: (t[2], t),
)

expected_new = [(3, 75, 1215), (15, 75, 1215)]
assert len(consecutive) == 15, len(consecutive)
assert sum(c <= 1000 for _, _, c in consecutive) == 13
assert [t for t in consecutive if t[2] > 1000] == expected_new

# Direct relation sanity checks for the two boundary witnesses.
assert 1215**2 == 3**9 * 75
assert 1216 == 4**2 * 76
assert 15**9 == 75**4 * 1215
assert 1216 == 16 * 76
for t in expected_new:
    assert maximal_rank_dependent(*t)
    assert maximal_rank_dependent(*(x + 1 for x in t))

# Ordered M(H) is six times the unordered count because maximal rank forces
# three distinct entries.
assert 6 * sum(c <= 1214 for _, _, c in consecutive) == 78
assert 6 * sum(c <= 1215 for _, _, c in consecutive) == 90
print("VERIFY_OK H=1215 total_unordered=15 le1000=13 new_at_1215=2 M1214=78 M1215=90")
