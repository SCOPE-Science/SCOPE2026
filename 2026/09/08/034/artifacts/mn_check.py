from functools import lru_cache
from fractions import Fraction
import itertools, math
from collections import Counter

def partitions(n, max_part=None):
    if n == 0:
        yield (); return
    if max_part is None: max_part = n
    for first in range(min(max_part, n), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest

def conj(p):
    if not p: return ()
    m = max(p)
    return tuple(sum(1 for x in p if x > j) for j in range(m))

def rim_hooks(shape, k):
    cells = [(r, c) for r, row in enumerate(shape) for c in range(row)]
    S = set(cells)
    n = sum(shape)
    if k > n or k <= 0:
        return []
    r = len(shape)
    out = []
    def rec(i, rem, prev, cur):
        if i == r:
            if rem == 0:
                out.append(tuple(cur))
            return
        for v in range(min(prev, shape[i], rem), -1, -1):
            cur.append(v); rec(i + 1, rem - v, v, cur); cur.pop()
    rec(0, n - k, min(n - k, shape[0]) if shape else 0, [])
    results = []
    seen = set()
    for mu_raw in out:
        skew = [c for c in cells if not (c[0] < len(mu_raw) and c[1] < mu_raw[c[0]])]
        if len(skew) != k: continue
        Sk = set(skew)
        q = [skew[0]]; vis = {skew[0]}
        while q:
            a = q.pop()
            for d in ((1,0),(-1,0),(0,1),(0,-1)):
                b = (a[0]+d[0], a[1]+d[1])
                if b in Sk and b not in vis:
                    vis.add(b); q.append(b)
        if len(vis) != k: continue
        bad = False
        for (rr, cc) in Sk:
            if (rr+1,cc) in Sk and (rr,cc+1) in Sk and (rr+1,cc+1) in Sk:
                bad = True; break
        if bad: continue
        rows = set(rr for rr, cc in Sk)
        h = len(rows) - 1
        mu_trim = tuple(x for x in mu_raw if x > 0)
        key = (mu_trim, h)
        if key in seen: continue
        seen.add(key)
        results.append((mu_trim, h))
    return results

def char_table(n):
    parts = list(partitions(n))
    cache = {}
    def chi(la, mu):
        key = (la, mu)
        if key in cache: return cache[key]
        if not la and not mu:
            cache[key] = 1; return 1
        if not mu:
            cache[key] = 0; return cache[key]
        k = mu[0]; rest = mu[1:]
        tot = 0
        for (nla, h) in rim_hooks(la, k):
            tot += ((-1) ** h) * chi(nla, rest)
        cache[key] = tot
        return tot
    table = {}
    for la in parts:
        for mu in parts:
            table[(la, mu)] = chi(la, tuple(sorted(mu, reverse=True)))
    return parts, table

def class_size(n, mu):
    c = Counter(mu)
    z = 1
    for l, m in c.items():
        z *= (l ** m) * math.factorial(m)
    return math.factorial(n) // z

if __name__ == "__main__":
    import sys
    for n in (6, 7, 8):
        parts, tab = char_table(n)
        fn = math.factorial(n)
        ok = True
        for i, a in enumerate(parts):
            for b in parts[i:]:
                s = sum(class_size(n, mu) * tab[(a, mu)] * tab[(b, mu)] for mu in parts)
                if s != (fn if a == b else 0):
                    print("ORTH FAIL", n, a, b, s); ok = False
        print(n, len(parts), "orth_ok=", ok)
