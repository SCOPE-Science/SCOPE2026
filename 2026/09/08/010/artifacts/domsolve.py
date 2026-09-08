"""Fast exact domination solver for maximal outerplanar graphs (bitmask B&B)."""
import sys


def gamma_exact(n, masks):
    full = (1 << n) - 1
    # greedy upper bound
    uncovered = full
    g = 0
    while uncovered:
        bi, bc = -1, -1
        for i in range(n):
            c = bin(masks[i] & uncovered).count("1")
            if c > bc:
                bc, bi = c, i
        uncovered &= ~masks[bi]
        g += 1
    best = [g]
    N = masks

    def dfs(covered, chosen):
        if chosen >= best[0]:
            return
        if covered == full:
            best[0] = chosen
            return
        rem = full & ~covered
        r = bin(rem).count("1")
        mx = 0
        for i in range(n):
            c = bin(N[i] & rem).count("1")
            if c > mx:
                mx = c
        lb = (r + mx - 1) // mx
        if chosen + lb >= best[0]:
            return
        u = (rem & -rem).bit_length() - 1
        m = N[u]
        cands = []
        v = 0
        while m:
            if m & 1:
                cands.append(v)
            v += 1
            m >>= 1
        cands.sort(key=lambda i: -bin(N[i] & rem).count("1"))
        for i in cands:
            dfs(covered | N[i], chosen + 1)

    dfs(0, 0)
    return best[0]


def gamma_bruteforce(n, masks):
    import itertools
    full = (1 << n) - 1
    for k in range(n + 1):
        for combo in itertools.combinations(range(n), k):
            cov = 0
            for v in combo:
                cov |= masks[v]
            if cov == full:
                return k
    return n
