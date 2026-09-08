"""Build S_n character tables (n=6..10) via Murnaghan-Nakayama, dual implementation + checks."""
import math, json
from functools import lru_cache

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None: max_part = n
    for f in range(min(max_part, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def z_of(mu):
    from collections import Counter
    c = Counter(mu); z = 1
    for i, m in c.items(): z *= (i ** m) * math.factorial(m)
    return z

def chi_mn(la, mu):
    la = tuple(la); mu = tuple(mu)
    @lru_cache(maxsize=None)
    def rec(beta, m):
        if not m:
            return 1 if tuple(sorted(beta)) == tuple(range(len(beta))) else 0
        h = m[0]; rest = m[1:]
        tot = 0
        bl = list(beta); s = set(bl)
        for idx, b in enumerate(bl):
            nb = b - h
            if nb < 0 or nb in s: continue
            jumped = sum(1 for c in bl if nb < c < b)
            s2 = set(s); s2.discard(b); s2.add(nb)
            tot += ((-1) ** jumped) * rec(tuple(sorted(s2)), rest)
        return tot
    if sum(la) != sum(mu): return 0
    k = len(la) + 1
    beta = tuple(sorted([(la[i] if i < len(la) else 0) + (k - 1 - i) for i in range(k)]))
    return rec(beta, mu)

def chi_mn2(la, mu):
    la = tuple(la); mu = tuple(mu)
    @lru_cache(maxsize=None)
    def rec(beta, m):
        if not m:
            return 1 if tuple(sorted(beta)) == tuple(range(len(beta))) else 0
        h = m[-1]; rest = m[:-1]
        tot = 0
        bl = list(beta); s = set(bl)
        for idx, b in enumerate(bl):
            nb = b - h
            if nb < 0 or nb in s: continue
            jumped = sum(1 for c in bl if nb < c < b)
            s2 = set(s); s2.discard(b); s2.add(nb)
            tot += ((-1) ** jumped) * rec(tuple(sorted(s2)), rest)
        return tot
    if sum(la) != sum(mu): return 0
    k = len(la) + 2
    beta = tuple(sorted([(la[i] if i < len(la) else 0) + (k - 1 - i) for i in range(k)]))
    return rec(beta, mu)

if __name__ == "__main__":
    from fractions import Fraction
    tables = {}
    for n in range(6, 11):
        parts = list(partitions(n))
        idx = {p: i for i, p in enumerate(parts)}
        T = [[0]*len(parts) for _ in range(len(parts))]
        T2 = [[0]*len(parts) for _ in range(len(parts))]
        for i, la in enumerate(parts):
            for j, mu in enumerate(parts):
                T[i][j] = chi_mn(la, mu)
                T2[i][j] = chi_mn2(la, mu)
        assert T == T2, f"dual MN mismatch at n={n}"
        z = [z_of(mu) for mu in parts]
        fact = math.factorial(n)
        for i in range(len(parts)):
            for k in range(len(parts)):
                s = sum(Fraction(T[i][j]*T[k][j], z[j]) for j in range(len(parts)))
                assert s == (1 if i == k else 0), (n, i, k, s)
        for j in range(len(parts)):
            for l in range(len(parts)):
                s = sum(Fraction(T[i][j]*T[i][l], 1) for i in range(len(parts)))
                assert s == (z[j] if j == l else 0), (n, j, l)
        ones = tuple([1]*n); j1 = idx[ones]
        assert all(T[i][j1] > 0 for i in range(len(parts)))
        assert sum(T[i][j1]**2 for i in range(len(parts))) == fact
        tables[n] = {"parts": parts, "T": T, "z": z}
        print(f"n={n}: p={len(parts)}, dual-MN agree, orthog OK, sum dim^2={fact}", flush=True)
    out = {str(n): {"parts": v["parts"], "T": v["T"], "z": v["z"]} for n, v in tables.items()}
    with open("chartables.json", "w") as f:
        json.dump(out, f)
    print("saved chartables.json")
