from itertools import product
from collections import Counter

def friendship(k):
    n = 2*k + 1
    adj = [set() for _ in range(n)]
    c = 0
    for i in range(k):
        a = 1 + 2*i
        b = a + 1
        for u,v in ((c,a),(c,b),(a,b)):
            adj[u].add(v); adj[v].add(u)
    return adj

def proper(adj, col):
    return all(col[u] != col[v] for u in range(len(adj)) for v in adj[u] if u < v)

def pcf(adj, col):
    if not proper(adj, col):
        return False
    for v in range(len(adj)):
        counts = Counter(col[u] for u in adj[v])
        if counts and not any(x == 1 for x in counts.values()):
            return False
    return True

def structural(k, col):
    adj = friendship(k)
    if not proper(adj, col):
        return False
    leaves = col[1:]
    cnt = Counter(leaves)
    return any(v == 1 for v in cnt.values())

def construction(k, used_colors):
    assert k >= 2 and 4 <= used_colors <= 2*k+1
    t = used_colors - 1
    leaves = []
    leaves.extend([0,2])
    for _ in range(1,k):
        leaves.extend([0,1])
    next_color = 3
    while len(set(leaves)) < t:
        cnt = Counter(leaves)
        old = next(c for c,m in cnt.items() if m >= 2)
        pos = next(i for i,c in enumerate(leaves) if c == old)
        leaves[pos] = next_color
        next_color += 1
    center = t
    col = [center] + leaves
    return col

proper_colorings_checked = 0
pcf_colorings_checked = 0
spectra = {}

for k in range(1,4):
    adj = friendship(k)
    n = 2*k+1
    realized = []
    for q in range(1,n+1):
        onto_pcf = 0
        for col in product(range(q), repeat=n):
            if not proper(adj,col):
                continue
            proper_colorings_checked += 1
            d = pcf(adj,col)
            s = structural(k,col)
            if d != s:
                raise AssertionError(("structural mismatch",k,q,col,d,s))
            if d:
                pcf_colorings_checked += 1
                if len(set(col)) == q:
                    onto_pcf += 1
        if onto_pcf:
            realized.append(q)
        if q == (3 if k == 1 else 4):
            expected = 6 if k == 1 else (96 if k == 2 else 24*k*(2**k))
            if onto_pcf != expected:
                raise AssertionError(("minimum count",k,onto_pcf,expected))
    expected_spectrum = [3] if k == 1 else list(range(4,2*k+2))
    if realized != expected_spectrum:
        raise AssertionError(("spectrum",k,realized,expected_spectrum))
    spectra[k] = realized

# Check the explicit spectrum construction through k=20.
constructions = 0
for k in range(2,21):
    adj = friendship(k)
    for q in range(4,2*k+2):
        col = construction(k,q)
        if len(set(col)) != q or not pcf(adj,col):
            raise AssertionError(("construction",k,q,col))
        constructions += 1

# Independently count all minimum four-colorings from the 3-color leaf palette
# for k=2..8. The center is then chosen in 4 ways.
minimum_counts = {}
for k in range(2,9):
    leaf_good = 0
    # Each matching edge receives an ordered pair of distinct colors in {0,1,2}.
    edge_pairs = [(a,b) for a in range(3) for b in range(3) if a != b]
    for choices in product(edge_pairs, repeat=k):
        leaves = [x for pair in choices for x in pair]
        if any(m == 1 for m in Counter(leaves).values()):
            leaf_good += 1
    total = 4*leaf_good
    formula = 96 if k == 2 else 24*k*(2**k)
    if total != formula:
        raise AssertionError(("formula",k,total,formula))
    minimum_counts[k] = total

print(
    "ALL CHECKS PASSED; "
    f"proper_colorings_checked={proper_colorings_checked}; "
    f"pcf_colorings_checked={pcf_colorings_checked}; "
    f"spectrum_constructions={constructions}; "
    "minimum_count_formula_k=2..8; "
    f"minimum_counts={minimum_counts}"
)
