from collections import deque

def rt_forward(a, b):
    """Forward power-automaton BFS from Q (bitmask ints)."""
    n = len(a)
    full = (1 << n) - 1
    dist = {full: 0}
    dq = deque([full])
    while dq:
        s = dq.popleft()
        if s & (s - 1) == 0:
            return dist[s]
        for f in (a, b):
            t = 0
            m = s
            while m:
                lsb = m & (-m)
                q = lsb.bit_length() - 1
                t |= (1 << f[q])
                m ^= lsb
            if t not in dist:
                dist[t] = dist[s] + 1
                dq.append(t)
    return None

def rt_reverse(a, b):
    """Independent code: reverse BFS from singletons via preimages; distance of Q."""
    n = len(a)
    # preimages as bitmasks
    prea = [0]*n; preb = [0]*n
    for q in range(n):
        prea[a[q]] |= (1 << q)
        preb[b[q]] |= (1 << q)
    def preimg(mask, pre):
        # {q : f(q) in mask} = union of pre[y] for y in mask
        r = 0
        m = mask
        while m:
            lsb = m & (-m)
            y = lsb.bit_length() - 1
            r |= pre[y]
            m ^= lsb
        return r
    full = (1 << n) - 1
    dist = {}
    dq = deque()
    for q in range(n):
        dist[1 << q] = 0
        dq.append(1 << q)
    while dq:
        s = dq.popleft()
        for pre in (prea, preb):
            t = preimg(s, pre)
            if t not in dist:
                dist[t] = dist[s] + 1
                dq.append(t)
    return dist.get(full, None)

def rt_pair_lower_bound(a, b):
    """Pair-automaton BFS: max over pairs of merge distance (lower bound on rt)."""
    n = len(a)
    INF = 10**9
    md = [[INF]*n for _ in range(n)]
    dq = deque()
    for p in range(n):
        for q in range(p+1, n):
            if a[p] == a[q] or b[p] == b[q]:
                md[p][q] = 1
                dq.append((p, q))
    while dq:
        p, q = dq.popleft()
        for f in (a, b):
            for r in range(n):
                for s in range(r+1, n):
                    if (f[r] == p and f[s] == q) or (f[r] == q and f[s] == p):
                        if md[r][s] == INF:
                            md[r][s] = md[p][q] + 1
                            dq.append((r, s))
    vals = [md[p][q] for p in range(n) for q in range(p+1, n)]
    if any(v == INF for v in vals):
        return None  # not synchronizing
    return max(vals)

if __name__ == '__main__':
    a = (1,2,3,4,5,0,7,7)
    b = (0,5,6,3,6,1,2,4)
    r1 = rt_forward(a, b)
    r2 = rt_reverse(a, b)
    lb = rt_pair_lower_bound(a, b)
    print("forward:", r1, "reverse:", r2, "pair-lb:", lb)
    assert r1 == r2 == 25
    # also cross-check Cerny automata rt=(n-1)^2 for n=3..8 (sanity of BFS codes)
    for n in range(3, 9):
        ca = tuple((q+1) % n for q in range(n))
        cb = tuple(list(range(n-1)) + [0])
        r1 = rt_forward(ca, cb); r2 = rt_reverse(ca, cb)
        print(f"Cerny n={n}: fwd={r1} rev={r2} expect={(n-1)**2}")
