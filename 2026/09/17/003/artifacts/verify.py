"""Reproducible checks for the SCOPE 2026-09-17 q-kernel note.

1) Exhaustively checks the theorem on all loopless simple digraphs with
   minimum in-degree >=2 for n=3,4,5.
2) Exhaustively checks the structural hitting-set lemma on all loopless
   partial functional digraphs (out-degree <=1) for n<=7.

No external packages are required.
"""
from itertools import product, combinations


def reach_within(adj, start_mask, q):
    reached = start_mask
    frontier = start_mask
    for _ in range(q):
        nxt = 0
        x = frontier
        while x:
            b = x & -x
            i = b.bit_length() - 1
            nxt |= adj[i]
            x -= b
        nxt &= ~reached
        reached |= nxt
        frontier = nxt
        if not frontier:
            break
    return reached


def independent(adj, mask):
    x = mask
    while x:
        b = x & -x
        i = b.bit_length() - 1
        if adj[i] & (mask ^ b):
            return False
        x -= b
    return True


def has_small_3kernel(adj):
    n = len(adj)
    cap = n // 3
    full = (1 << n) - 1
    for r in range(1, cap + 1):
        for comb in combinations(range(n), r):
            mask = sum(1 << i for i in comb)
            if independent(adj, mask) and reach_within(adj, mask, 3) == full:
                return True
    return False


def check_all_mindeg2(n):
    incoming_options = []
    for v in range(n):
        allowed = ((1 << n) - 1) ^ (1 << v)
        opts = []
        sub = allowed
        while sub:
            if sub.bit_count() >= 2:
                opts.append(sub)
            sub = (sub - 1) & allowed
        incoming_options.append(opts)

    total = 0
    for incoming in product(*incoming_options):
        total += 1
        adj = [0] * n
        for v, mask in enumerate(incoming):
            x = mask
            while x:
                b = x & -x
                u = b.bit_length() - 1
                adj[u] |= 1 << v
                x -= b
        if not has_small_3kernel(adj):
            return total, False, adj
    return total, True, None


def min_high_indegree_hitting_set(f):
    """f[i] is -1 or the unique out-neighbor of i.

    X is the set of vertices with in-degree >=2. We find the minimum P
    such that each x in X is either in P or has an in-neighbor in P.
    """
    n = len(f)
    indeg = [0] * n
    for i, j in enumerate(f):
        if j >= 0:
            indeg[j] += 1
    X = [j for j, d in enumerate(indeg) if d >= 2]
    if not X:
        return 0
    idx = {x: k for k, x in enumerate(X)}
    cover_masks = []
    for i in range(n):
        mask = 0
        if i in idx:
            mask |= 1 << idx[i]
        j = f[i]
        if j in idx:
            mask |= 1 << idx[j]
        cover_masks.append(mask)
    full = (1 << len(X)) - 1
    dp = {0: 0}
    for cm in cover_masks:
        ndp = dict(dp)
        for mask, cost in dp.items():
            nm = mask | cm
            if cost + 1 < ndp.get(nm, 10**9):
                ndp[nm] = cost + 1
        dp = ndp
    return dp[full]


def check_partial_functional(n):
    choices = [[-1] + [j for j in range(n) if j != i] for i in range(n)]
    total = 0
    for f in product(*choices):
        total += 1
        tau = min_high_indegree_hitting_set(f)
        if 3 * tau > n:
            return total, False, f, tau
    return total, True, None, None


if __name__ == "__main__":
    print("Theorem check: min-in-degree >=2 digraphs")
    for n in (3, 4, 5):
        total, ok, witness = check_all_mindeg2(n)
        print(f"n={n}: checked {total} digraphs; ok={ok}")
        if not ok:
            print("counterexample adjacency masks:", witness)
            raise SystemExit(1)

    print("\nStructural lemma check: partial functional digraphs")
    for n in range(1, 8):
        total, ok, witness, tau = check_partial_functional(n)
        print(f"n={n}: checked {total} maps; ok={ok}")
        if not ok:
            print("counterexample map:", witness, "tau=", tau)
            raise SystemExit(1)
