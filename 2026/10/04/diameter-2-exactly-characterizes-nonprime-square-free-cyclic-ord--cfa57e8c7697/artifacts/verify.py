#!/usr/bin/env python3
"""Finite exact checks for the cyclic psi-divisibility diameter theorem."""
from collections import deque
from math import gcd

def factor(n):
    f = {}
    d = 2
    while d*d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f

def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d*d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

def divisors(n):
    out = [1]
    for p, a in factor(n).items():
        old = list(out)
        out = []
        pp = 1
        for _ in range(a + 1):
            out.extend(x * pp for x in old)
            pp *= p
    return sorted(out)

def psi_pp(p, a):
    return (p ** (2*a + 1) + 1) // (p + 1)

def psi_cyclic(n):
    z = 1
    for p, a in factor(n).items():
        z *= psi_pp(p, a)
    return z

def graph(n):
    vs = [d for d in divisors(n) if d > 1]
    ps = {d: psi_cyclic(d) for d in vs}
    adj = {d: set() for d in vs}
    for i, a in enumerate(vs):
        for b in vs[i+1:]:
            if b % a == 0 and ps[b] % ps[a] == 0:
                adj[a].add(b); adj[b].add(a)
            elif a % b == 0 and ps[a] % ps[b] == 0:
                adj[a].add(b); adj[b].add(a)
    return adj

def distance(adj, s, t):
    q = deque([(s, 0)])
    seen = {s}
    while q:
        v, d = q.popleft()
        if v == t:
            return d
        for w in adj[v]:
            if w not in seen:
                seen.add(w)
                q.append((w, d + 1))
    return None

def diameter(adj):
    if len(adj) <= 1:
        return 0
    best = 0
    for v in adj:
        q = deque([(v, 0)])
        seen = {v}
        far = 0
        while q:
            x, d = q.popleft()
            far = max(far, d)
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    q.append((y, d + 1))
        if len(seen) != len(adj):
            return None
        best = max(best, far)
    return best

def choose_t(alpha):
    if alpha == 2:
        return 2
    if alpha == 3:
        return 2
    if alpha == 4:
        return 3
    for t in range(alpha // 2 + 1, alpha + 1):
        if is_prime(2*t + 1) and alpha < 3*t - 2:
            return t
    raise AssertionError(("no t", alpha))

def main():
    for alpha in range(2, 501):
        t = choose_t(alpha)
        assert is_prime(2*t + 1)
        assert 2 <= t <= alpha
        assert alpha < 3*t - 2

    # Exhaustive cyclic graph check over a moderate range.
    for n in range(2, 1201):
        fac = factor(n)
        d = diameter(graph(n))
        squarefree_multi = len(fac) >= 2 and all(a == 1 for a in fac.values())
        assert (d == 2) == squarefree_multi, (n, fac, d)

    # Explicit proof-witness checks for sampled mixed-prime factorizations.
    primes = [2, 3, 5, 7, 11, 13]
    for p in primes:
        for alpha in range(2, 8):
            for q in primes:
                if q == p:
                    continue
                for beta in (1, 2):
                    n = (p ** alpha) * (q ** beta)
                    if n > 2_000_000:
                        continue
                    t = choose_t(alpha)
                    m = n // (p ** alpha)
                    h = p ** t
                    k = (p ** (t - 1)) * m
                    d = distance(graph(n), h, k)
                    assert d is not None and d >= 3, (n, h, k, d)

    print("VERIFY_OK")

if __name__ == "__main__":
    main()
