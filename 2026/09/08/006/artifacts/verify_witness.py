from collections import deque

def rt_bfs(a, b):
    n = len(a)
    full = (1 << n) - 1
    # image of subset mask under letter
    def img(mask, f):
        r = 0
        m = mask
        while m:
            lsb = m & (-m)
            q = lsb.bit_length() - 1
            r |= (1 << f[q])
            m ^= lsb
        return r
    dist = {full: 0}
    dq = deque([full])
    parent = {full: None}
    while dq:
        s = dq.popleft()
        if s & (s - 1) == 0:  # singleton
            # reconstruct word
            w = []
            cur = s
            while parent[cur] is not None:
                cur, ch = parent[cur]
                w.append(ch)
            return dist[s], ''.join(reversed(w)), s
        for ch, f in (('a', a), ('b', b)):
            t = img(s, f)
            if t not in dist:
                dist[t] = dist[s] + 1
                parent[t] = (s, ch)
                dq.append(t)
    return None, None, None  # not synchronizing

def indeg(f, n):
    d = [0]*n
    for q in range(n):
        d[f[q]] += 1
    return d

def is_eulerian(a, b):
    n = len(a)
    da, db = indeg(a, n), indeg(b, n)
    return all(da[q]+db[q] == 2 for q in range(n))

def apply_word(a, b, word):
    n = len(a)
    cur = set(range(n))
    for ch in word:
        f = a if ch == 'a' else b
        cur = {f[q] for q in cur}
    return cur

def is_sync_eppstein(a, b):
    # pair merging test
    n = len(a)
    from collections import deque
    merge = [[False]*n for _ in range(n)]
    dq = deque()
    for p in range(n):
        for q in range(p+1, n):
            if a[p] == a[q] or b[p] == b[q]:
                merge[p][q] = True
                dq.append((p, q))
    funcs = (a, b)
    # need reverse edges: predecessors
    pre = [[[], []] for _ in range(n)]  # not needed; do forward preimage over pairs
    while dq:
        p, q = dq.popleft()
        for li in range(2):
            f = funcs[li]
            # all pairs (r,s) with f(r)=p... actually need pairs mapping to (p,q): r in pre(p), s in pre(q)
            for r in range(n):
                if f[r] != p: continue
                for s in range(n):
                    if f[s] != q: continue
                    x, y = (r, s) if r < s else (s, r)
                    if x != y and not merge[x][y]:
                        merge[x][y] = True
                        dq.append((x, y))
    return all(merge[p][q] for p in range(n) for q in range(p+1, n))

if __name__ == '__main__':
    a = (1,2,3,4,5,0,7,7)
    b = (0,5,6,3,6,1,2,4)
    n = 8
    print("indeg_a:", indeg(a, n))
    print("indeg_b:", indeg(b, n))
    print("eulerian:", is_eulerian(a, b))
    rt, w, sing = rt_bfs(a, b)
    print("rt:", rt, "singleton:", sing)
    print("bfs word:", w, "len:", len(w) if w else None)
    # claimed word
    cw = "bbaabaababbaaababaabaaaab"
    print("claimed len:", len(cw), "image:", apply_word(a, b, cw))
    print("eppstein sync:", is_sync_eppstein(a, b))
    # stepwise compression of claimed word
    cur = set(range(n))
    print("start:", sorted(cur))
    for i, ch in enumerate(cw):
        f = a if ch == 'a' else b
        cur = {f[q] for q in cur}
        print(i, ch, sorted(cur), len(cur))
