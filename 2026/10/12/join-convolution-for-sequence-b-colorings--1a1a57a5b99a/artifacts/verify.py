from itertools import combinations, product
from functools import lru_cache

def edges_of_n(n):
    return list(combinations(range(n), 2))

def graph_from_mask(n, mask):
    adj = [0] * n
    for j, (u, v) in enumerate(edges_of_n(n)):
        if (mask >> j) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return tuple(adj)

def connected(adj):
    n = len(adj)
    if n == 0:
        return False
    seen = 1
    while True:
        nxt = seen
        for v in range(n):
            if (seen >> v) & 1:
                nxt |= adj[v]
        if nxt == seen:
            break
        seen = nxt
    return seen == (1 << n) - 1

def join(a, b):
    na, nb = len(a), len(b)
    out = [0] * (na + nb)
    mask_b = ((1 << nb) - 1) << na
    mask_a = (1 << na) - 1
    for u in range(na):
        out[u] = a[u] | mask_b
    for v in range(nb):
        out[na + v] = (b[v] << na) | mask_a
    return tuple(out)

def proper_surjective(coloring, k, adj):
    if set(coloring) != set(range(k)):
        return False
    n = len(adj)
    for u in range(n):
        for v in range(u + 1, n):
            if ((adj[u] >> v) & 1) and coloring[u] == coloring[v]:
                return False
    return True

def cdv_counts(coloring, k, adj):
    n = len(adj)
    counts = [0] * k
    all_colors = set(range(k))
    for v in range(n):
        seen = {coloring[v]}
        for u in range(n):
            if (adj[v] >> u) & 1:
                seen.add(coloring[u])
        if seen == all_colors:
            counts[coloring[v]] += 1
    return tuple(counts)

profile_cache = {}
colorings_examined = 0

def b_profiles(adj):
    global colorings_examined
    if adj in profile_cache:
        return profile_cache[adj]
    n = len(adj)
    profiles = set()
    for k in range(1, n + 1):
        for c in product(range(k), repeat=n):
            colorings_examined += 1
            if not proper_surjective(c, k, adj):
                continue
            counts = cdv_counts(c, k, adj)
            if min(counts) >= 1:
                profiles.add(tuple(sorted(counts, reverse=True)))
    profile_cache[adj] = profiles
    return profiles

connected_graphs = []
graphs_by_order = {}
for n in range(1, 4):
    local = []
    for mask in range(1 << len(edges_of_n(n))):
        g = graph_from_mask(n, mask)
        if connected(g):
            local.append(g)
            connected_graphs.append(g)
    graphs_by_order[n] = len(local)

join_pairs = 0
for g in connected_graphs:
    pg = b_profiles(g)
    for h in connected_graphs:
        ph = b_profiles(h)
        j = join(g, h)
        observed = b_profiles(j)
        predicted = {
            tuple(sorted(a + b, reverse=True))
            for a in pg
            for b in ph
        }
        if observed != predicted:
            raise AssertionError(("join profile mismatch", g, h, observed, predicted))
        join_pairs += 1

def multipartite_adj(parts):
    part_of = []
    for i, n in enumerate(parts):
        part_of.extend([i] * n)
    N = len(part_of)
    adj = [0] * N
    for u in range(N):
        for v in range(N):
            if u != v and part_of[u] != part_of[v]:
                adj[u] |= 1 << v
    return tuple(adj)

def part_profiles(total, min_part=1, cur=()):
    if total == 0:
        if len(cur) >= 2:
            yield cur
        return
    for x in range(min_part, total + 1):
        yield from part_profiles(total - x, x, cur + (x,))

def requirement_sequences(length, max_entry, last=None):
    if length == 0:
        yield ()
        return
    if last is None:
        last = max_entry
    for x in range(last, 0, -1):
        for tail in requirement_sequences(length - 1, max_entry, x):
            yield (x,) + tail

def brute_labeled_b_counts(adj, k):
    global colorings_examined
    n = len(adj)
    vecs = []
    for c in product(range(k), repeat=n):
        colorings_examined += 1
        if not proper_surjective(c, k, adj):
            continue
        counts = cdv_counts(c, k, adj)
        if min(counts) >= 1:
            vecs.append(counts)
    return vecs

multipartite_profiles = 0
requirements_checked = 0
for N in range(2, 7):
    for parts in part_profiles(N):
        multipartite_profiles += 1
        r = len(parts)
        adj = multipartite_adj(parts)

        possible_k = {len(p) for p in b_profiles(adj)}
        if possible_k != {r}:
            raise AssertionError(("wrong b-color counts", parts, possible_k, r))

        labeled = brute_labeled_b_counts(adj, r)
        max_entry = max(parts)
        for S in requirement_sequences(r, max_entry):
            requirements_checked += 1
            brute = sum(
                1 for counts in labeled
                if all(counts[i] >= S[i] for i in range(r))
            )
            cvals = [sum(1 for n in parts if n >= S[i]) for i in range(r)]
            formula = 1
            for i, cval in enumerate(cvals, start=1):
                factor = cval - i + 1
                if factor <= 0:
                    formula = 0
                    break
                formula *= factor
            if brute != formula:
                raise AssertionError(("multipartite count mismatch", parts, S, brute, formula))

print(
    "ALL CHECKS PASSED; "
    f"connected_graphs=1:{graphs_by_order[1]},2:{graphs_by_order[2]},3:{graphs_by_order[3]}; "
    f"join_pairs={join_pairs}; "
    f"multipartite_profiles={multipartite_profiles}; "
    f"requirement_sequences={requirements_checked}; "
    f"colorings_examined={colorings_examined}"
)
