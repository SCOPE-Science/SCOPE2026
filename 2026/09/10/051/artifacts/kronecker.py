"""Exact Kronecker coefficient via from-scratch Murnaghan-Nakayama + class algebra.
Usage: python3 kronecker.py [n] [lamA] [lamB] [lamC]  (partitions as comma lists)
   or: python3 kronecker.py --selftest
"""
import sys, math, functools
from collections import Counter

sys.setrecursionlimit(100000)

def partitions_of(n, max_part=None):
    if max_part is None: max_part = n
    if n == 0:
        yield ()
        return
    for f in range(min(max_part, n), 0, -1):
        for rest in partitions_of(n - f, f):
            yield (f,) + rest

def z_of(mu):
    c = Counter(mu)
    z = 1
    for part, m in c.items():
        z *= (part ** m) * math.factorial(m)
    return z

def cells_of(lam):
    s = set()
    for i, r in enumerate(lam):
        for j in range(r):
            s.add((i, j))
    return s

def sub_partitions(lam, target_sum):
    """Yield all partitions nu subset of lam with |nu| = target_sum."""
    L = len(lam)
    out = []
    def rec(i, mx, acc, s):
        if i == L:
            if s == target_sum:
                t = tuple(acc)
                # canonicalize: drop trailing zeros, ensure nonincreasing (guaranteed)
                while t and t[-1] == 0:
                    t = t[:-1]
                out.append(t)
            return
        for v in range(min(mx, lam[i]), -1, -1):
            ns = s + v
            # prune: max achievable
            if ns > target_sum: continue
            # min achievable with rest = ns (rest zeros) <= target; max = ns + sum(lam[i+1:]) cap by mx chain
            rec(i + 1, v, acc + [v], ns)
    rec(0, lam[0] if lam else 0, [], 0)
    return out

_rim_cache = {}
def rim_removals(lam, k):
    """List of (nu, sign) removing a rim hook of size k from lam."""
    key = (lam, k)
    if key in _rim_cache: return _rim_cache[key]
    n = sum(lam)
    res = []
    if k == 0:
        res = [(lam, 1)]
    elif k <= n and lam:
        lamcells = cells_of(lam)
        for nu in sub_partitions(lam, n - k):
            nucells = cells_of(nu)
            skew = lamcells - nucells
            assert len(skew) == k
            # no 2x2 block
            ok = True
            for (i, j) in skew:
                if (i+1, j) in skew and (i, j+1) in skew and (i+1, j+1) in skew:
                    ok = False; break
            if not ok: continue
            # connected (edge adjacency)
            seen = {next(iter(skew))}
            stack = [next(iter(skew))]
            while stack:
                a, b = stack.pop()
                for d in ((1,0),(-1,0),(0,1),(0,-1)):
                    nb = (a+d[0], b+d[1])
                    if nb in skew and nb not in seen:
                        seen.add(nb); stack.append(nb)
            if len(seen) != k: continue
            rows = {i for (i, j) in skew}
            sign = -1 if (len(rows) - 1) % 2 else 1
            res.append((nu, sign))
    _rim_cache[key] = res
    return res

_chi_cache = {}
def chi(lam, mu):
    key = (lam, mu)
    if key in _chi_cache: return _chi_cache[key]
    if not mu:
        r = 1 if not lam else 0
    elif not lam:
        r = 0
    else:
        k = mu[0]; rest = mu[1:]
        t = 0
        for nu, sgn in rim_removals(lam, k):
            t += sgn * chi(nu, rest)
        r = t
    _chi_cache[key] = r
    return r

def kronecker(lamA, lamB, lamC):
    n = sum(lamA)
    assert sum(lamB) == n and sum(lamC) == n
    total = 0
    for mu in partitions_of(n):
        z = z_of(mu)
        a = chi(lamA, mu); 
        if a == 0: continue
        b = chi(lamB, mu)
        if b == 0: continue
        c = chi(lamC, mu)
        if c == 0: continue
        total += a * b * c / z
    # total should be integer; do exact rational via Fraction-free: accumulate numerator
    return total

def kronecker_exact(lamA, lamB, lamC):
    from fractions import Fraction
    n = sum(lamA)
    t = Fraction(0)
    terms = 0
    for mu in partitions_of(n):
        z = z_of(mu)
        a = chi(lamA, mu)
        if a == 0: continue
        b = chi(lamB, mu)
        if b == 0: continue
        c = chi(lamC, mu)
        if c == 0: continue
        t += Fraction(a * b * c, z)
        terms += 1
    return t, terms

def selftest():
    # g((3,2,1)^3) at n=6 should be 5 (per SCOPE failure record SCOPE-FAIL-20260908-017)
    t, terms = kronecker_exact((3,2,1), (3,2,1), (3,2,1))
    print("g((3,2,1)^3) =", t, "terms:", terms)
    assert t == 5, t
    # orthogonality: sum_mu chi(lam,mu)^2 / z = 1
    from fractions import Fraction
    for lam in [(4,2), (3,3), (2,2,2)]:
        s = sum(Fraction(chi(lam, mu)**2, z_of(mu)) for mu in partitions_of(6))
        print(lam, "norm =", s); assert s == 1, (lam, s)
    # g((2,1)^3) at n=3 = 1? (2,1)x(2,1) contains (2,1) once
    t, _ = kronecker_exact((2,1), (2,1), (2,1))
    print("g((2,1)^3) =", t); assert t == 1, t
    print("SELFTEST OK")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--selftest":
        selftest()
    else:
        n = int(sys.argv[1])
        A = tuple(sorted((int(x) for x in sys.argv[2].split(",")), reverse=True))
        B = tuple(sorted((int(x) for x in sys.argv[3].split(",")), reverse=True))
        C = tuple(sorted((int(x) for x in sys.argv[4].split(",")), reverse=True))
        assert sum(A) == n and sum(B) == n and sum(C) == n, (A, B, C)
        import time; t0 = time.time()
        t, terms = kronecker_exact(A, B, C)
        dt = time.time() - t0
        print(f"g({A},{B},{C}) = {t}  [nonzero-term classes: {terms}]  ({dt:.1f}s)")
