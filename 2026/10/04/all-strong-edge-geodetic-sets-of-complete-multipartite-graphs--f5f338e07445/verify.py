from functools import lru_cache
from itertools import combinations
from math import comb

def partitions_min2(n, lo=2):
    if n == 0:
        yield ()
        return
    for x in range(lo, n + 1):
        for rest in partitions_min2(n - x, x):
            yield (x,) + rest

def rho(s):
    return s - 1 if s % 2 == 0 else s - 2

def predicted(parts, mask):
    n = sum(parts)
    blocks = []
    a = 0
    for s in parts:
        blocks.append(range(a, a+s))
        a += s
    inc = []
    for i, block in enumerate(blocks):
        r = sum(1 for v in block if not ((mask >> v) & 1))
        if r:
            inc.append((i, r))
    if not inc:
        return True
    if len(inc) > 1:
        return False
    i, r = inc[0]
    return r <= min(rho(parts[j]) for j in range(len(parts)) if j != i)

def direct_solver(parts, mask):
    part_of = []
    for i, s in enumerate(parts):
        part_of.extend([i] * s)
    n = len(part_of)

    edge_index = {}
    edges = []
    for u in range(n):
        for v in range(u+1, n):
            if part_of[u] != part_of[v]:
                edge_index[(u,v)] = len(edges)
                edges.append((u,v))
    full = (1 << len(edges)) - 1

    selected = [v for v in range(n) if (mask >> v) & 1]

    # For endpoints in different parts the unique shortest path is their edge.
    covered = 0
    for u, v in combinations(selected, 2):
        if part_of[u] != part_of[v]:
            covered |= 1 << edge_index[(min(u,v), max(u,v))]
    if covered == full:
        return True

    # For selected endpoints in one part, enumerate every possible middle vertex.
    pair_options = []
    for u, v in combinations(selected, 2):
        if part_of[u] == part_of[v]:
            opts = []
            for w in range(n):
                if part_of[w] != part_of[u]:
                    bitmask = 0
                    for a, b in ((u,w), (v,w)):
                        bitmask |= 1 << edge_index[(min(a,b), max(a,b))]
                    opts.append(bitmask)
            pair_options.append(tuple(opts))

    @lru_cache(None)
    def dfs(cov, used):
        if cov == full:
            return True
        # Branch on an uncovered graph edge having the fewest currently
        # available selected-pair path choices.
        best = None
        for ei in range(len(edges)):
            bit = 1 << ei
            if cov & bit:
                continue
            choices = []
            for pi, opts in enumerate(pair_options):
                if (used >> pi) & 1:
                    continue
                for om in opts:
                    if om & bit:
                        choices.append((pi, om))
            if not choices:
                return False
            if best is None or len(choices) < len(best):
                best = choices
                if len(best) == 1:
                    break
        for pi, om in best:
            if dfs(cov | om, used | (1 << pi)):
                return True
        return False

    return dfs(covered, 0)

def theorem_value(parts):
    # Theorem 2.7 of Klavzar--Zmazek, for sorted part sizes.
    a = tuple(sorted(parts))
    n1, n2 = a[0], a[1]
    tail = sum(a[1:])
    if n1 % 2 == 0:
        return tail + 1 if n2 in (n1, n1+1) else tail
    else:
        return tail + 2 if n2 == n1 else tail

def formula_value_and_count(parts):
    n = sum(parts)
    Rs = []
    for i, s in enumerate(parts):
        r = min(s, min(rho(parts[j]) for j in range(len(parts)) if j != i))
        Rs.append(r)
    R = max(Rs)
    count = sum(comb(parts[i], R) for i, r in enumerate(Rs) if r == R)
    return n - R, count

graph_count = 0
set_count = 0
for n in range(4, 11):
    for parts in partitions_min2(n):
        if len(parts) < 2:
            continue
        graph_count += 1
        strong_masks = []
        for mask in range(1 << n):
            got = direct_solver(parts, mask)
            pred = predicted(parts, mask)
            assert got == pred, (parts, mask, got, pred)
            if got:
                strong_masks.append(mask)
            set_count += 1

        min_size = min(m.bit_count() for m in strong_masks)
        actual_bases = sum(1 for m in strong_masks if m.bit_count() == min_size)
        fv, fc = formula_value_and_count(parts)
        assert min_size == fv, (parts, min_size, fv)
        assert actual_bases == fc, (parts, actual_bases, fc)

# Separately check that the symmetric formula recovers the published value
# formula for a much larger finite range.
value_checks = 0
for n in range(4, 31):
    for parts in partitions_min2(n):
        if len(parts) < 2:
            continue
        fv, _ = formula_value_and_count(parts)
        assert fv == theorem_value(parts), (parts, fv, theorem_value(parts))
        value_checks += 1

print("VERIFY_OK")
print("direct isomorphism types:", graph_count)
print("direct vertex subsets:", set_count)
print("published-value comparisons:", value_checks)
