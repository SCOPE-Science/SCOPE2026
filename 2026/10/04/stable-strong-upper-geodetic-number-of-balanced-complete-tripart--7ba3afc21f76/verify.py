from collections import deque
from math import comb

def maxflow(cap, s, t):
    n = len(cap)
    flow = 0
    while True:
        prev = [-1] * n
        prev[s] = s
        q = deque([s])
        while q and prev[t] < 0:
            u = q.popleft()
            for v, c in enumerate(cap[u]):
                if c > 0 and prev[v] < 0:
                    prev[v] = u
                    q.append(v)
                    if v == t:
                        break
        if prev[t] < 0:
            return flow
        aug = 10**9
        v = t
        while v != s:
            u = prev[v]
            aug = min(aug, cap[u][v])
            v = u
        v = t
        while v != s:
            u = prev[v]
            cap[u][v] -= aug
            cap[v][u] += aug
            v = u
        flow += aug

def strong(n, svec):
    tvec = [n - x for x in svec]
    pvec = [comb(x, 2) for x in svec]
    cap = [[0] * 8 for _ in range(8)]
    for i in range(3):
        cap[0][1+i] = tvec[i]
        for j in range(3):
            if i != j:
                cap[1+i][4+j] = 10**6
        cap[4+i][7] = pvec[i]
    return maxflow(cap, 0, 7) == sum(tvec)

def minimal(n, svec):
    if not strong(n, svec):
        return False
    for i, x in enumerate(svec):
        if x:
            z = list(svec)
            z[i] -= 1
            if strong(n, z):
                return False
    return True

def maximum_minimal(n):
    best = -1
    pats = set()
    for a in range(n + 1):
        for b in range(n + 1):
            for c in range(n + 1):
                s = (a, b, c)
                if minimal(n, s):
                    k = sum(s)
                    if k > best:
                        best, pats = k, {s}
                    elif k == best:
                        pats.add(s)
    return best, pats

for n in range(12, 31):
    best, pats = maximum_minimal(n)
    target = {(2, 2, n-2), (2, n-2, 2), (n-2, 2, 2)}
    assert best == n + 2, (n, best)
    assert pats == target, (n, pats, target)

print("VERIFY_OK")
print("checked n=12..30 by independent max-flow enumeration")
print("the infinite theorem rests on the accompanying proof")
