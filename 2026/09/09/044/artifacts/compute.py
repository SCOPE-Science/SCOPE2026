#!/usr/bin/env python3
"""From-scratch MN tables + symmetric/alternating splitting of non-hook 3-row squares, n=6..8."""
import json, math, itertools
from functools import lru_cache

def partitions(n, maxp=None):
    if n == 0:
        yield ();
        return
    if maxp is None: maxp = n
    for f in range(min(maxp, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def centralizer(mu):
    from collections import Counter
    c = Counter(mu); z = 1
    for l, m in c.items(): z *= (math.factorial(m) * (l ** m))
    return z

def hook_dim(la):
    cells = [(i, j) for i in range(len(la)) for j in range(la[i])]
    n = len(cells); prod = 1
    for (i, j) in cells:
        h = (la[i] - j) + sum(1 for r in range(i + 1, len(la)) if la[r] > j) - 1 + 1
        # hook = arm + leg + 1
        arm = la[i] - j - 1
        leg = sum(1 for r in range(i + 1, len(la)) if la[r] > j)
        prod *= (arm + leg + 1)
    return math.factorial(n) // prod

def rim_hooks(la, m):
    """All rim hooks of size m: subsets S of cells, remainder a diagram, S connected, no 2x2."""
    cells = [(i, j) for i in range(len(la)) for j in range(la[i])]
    out = []
    for S in itertools.combinations(cells, m):
        S = set(S)
        rem = [r for r in cells if r not in S]
        # remainder is Young diagram: rows left-justified & decreasing
        lens = {}
        for (i, j) in rem: lens[i] = lens.get(i, 0) + 1
        ok = True
        for (i, j) in rem:
            if j > 0 and (i, j - 1) not in rem and (i, j - 1) not in S:
                pass
            if j > 0 and (i, j - 1) not in rem:
                # cell (i,j) present but (i,j-1) removed -> invalid unless j-1 not in diagram... it is
                ok = False; break
        if not ok: continue
        # row lengths of remainder (only rows present)
        if rem:
            maxr = max(i for i, j in rem)
            rl = [sum(1 for (i, j) in rem if i == r) for r in range(maxr + 1)]
            for a in range(len(rl) - 1):
                if rl[a] < rl[a + 1]: ok = False; break
            if not ok: continue
        # connectivity of S (edge)
        stack = [next(iter(S))]; seen = set(stack)
        while stack:
            i, j = stack.pop()
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (i + d[0], j + d[1])
                if q in S and q not in seen: seen.add(q); stack.append(q)
        if seen != S: continue
        # no 2x2 block
        bad = False
        for (i, j) in S:
            if (i + 1, j) in S and (i, j + 1) in S and (i + 1, j + 1) in S:
                bad = True; break
        if bad: continue
        rows = len(set(i for i, j in S))
        rem_la = tuple(sorted([sum(1 for (i, j) in rem if i == r)
                               for r in set(i for i, j in rem)], reverse=False)) if rem else ()
        # build remainder partition properly
        if rem:
            maxr = max(i for i, j in rem)
            rem_la = tuple(sum(1 for (ii, jj) in rem if ii == r) for r in range(maxr + 1))
            if any(rem_la[a] < rem_la[a + 1] for a in range(len(rem_la) - 1)):
                continue
            rem_la = tuple(x for x in rem_la if x > 0)
            if sum(rem_la) != sum(la) - m: continue
        else:
            rem_la = ()
        out.append((rem_la, (-1) ** (rows - 1)))
    # dedupe identical (rem,sign) arising once each; each subset is distinct hook so keep all
    return out

from functools import lru_cache as lc

def make_chi():
    @lc(maxsize=None)
    def chi(la, mu):
        if sum(la) == 0: return 1 if sum(mu) == 0 else 0
        if not mu: return 0
        m = mu[0]; rest = mu[1:]
        t = 0
        for rem, sgn in rim_hooks(la, m):
            t += sgn * chi(rem, rest)
        return t
    return chi

def square_type(mu):
    """cycle type of w^2 for w of type mu."""
    out = []
    for L in mu:
        if L % 2 == 1: out.append(L)
        else: out.extend([L // 2, L // 2])
    return tuple(sorted(out, reverse=True))

def run(n):
    chi = make_chi()
    parts = list(partitions(n))
    idx = {p: i for i, p in enumerate(parts)}
    fact = math.factorial(n)
    # order classes in same partition order
    table = [[chi(la, mu) for mu in parts] for la in parts]
    # checks
    dims = [hook_dim(la) for la in parts]
    assert dims == [chi(la, tuple([1] * n)) for la in parts], "dim mismatch"
    assert sum(d * d for d in dims) == fact, "sum dim^2 != n!"
    # orthogonality
    for a in range(len(parts)):
        for b in range(len(parts)):
            s = sum(table[a][k] * table[b][k] * fact // centralizer(parts[k]) for k in range(len(parts)))
            assert s == (fact if a == b else 0), f"row orth {n} {a} {b} {s}"
    sqmap = [idx[square_type(mu)] for mu in parts]
    clsizes = [fact // centralizer(mu) for mu in parts]
    targets = [la for la in parts if len(la) == 3 and la[1] >= 2]
    rows = []
    for la in targets:
        li = idx[la]; d = dims[li]
        for nu in parts:
            ni = idx[nu]
            g = sum(table[li][k] ** 2 * table[ni][k] * clsizes[k] for k in range(len(parts))) / fact
            m = sum(table[li][sqmap[k]] * table[ni][k] * clsizes[k] for k in range(len(parts))) / fact
            g = int(round(g)); m = int(round(m))
            assert (g + m) % 2 == 0 and (g - m) % 2 == 0
            s, a = (g + m) // 2, (g - m) // 2
            assert s >= 0 and a >= 0 and s + a == g
            rows.append({"lambda": list(la), "nu": list(nu), "s": s, "a": a, "g": g, "m": m})
        # degree identities
        R = [r for r in rows if r["lambda"] == list(la)]
        assert sum(r["g"] * dims[idx[tuple(r["nu"])]] for r in R) == d * d
        assert sum(r["s"] * dims[idx[tuple(r["nu"])]] for r in R) == d * (d + 1) // 2
        assert sum(r["a"] * dims[idx[tuple(r["nu"])]] for r in R) == d * (d - 1) // 2
    return {"n": n, "dims": dims, "targets": [list(t) for t in targets],
            "classes": [list(p) for p in parts], "rows": rows}

if __name__ == "__main__":
    allrows = {}
    for n in (6, 7, 8):
        r = run(n)
        allrows[str(n)] = r
        print(f"n={n} targets={r['targets']} rows={len(r['rows'])}")
    # maximal gap
    best = []
    for n, r in allrows.items():
        for row in r["rows"]:
            if abs(row["s"] - row["a"]) > 0:
                best.append((abs(row["s"] - row["a"]), n, row))
    best.sort(key=lambda b: -b[0])
    print("TOP GAPS:", [(b[0], b[1], b[2]["lambda"], b[2]["nu"], b[2]["s"], b[2]["a"], b[2]["g"]) for b in best[:8]])
    sc = [r for r in allrows["6"]["rows"] if r["lambda"] == [3, 2, 1]]
    print("(3,2,1)^2 containment: all g>0?", all(r["g"] > 0 for r in sc), "s>0:", sum(1 for r in sc if r["s"] > 0), "/11")
    for r in sc: print(r["nu"], r["s"], r["a"], r["g"])
    with open("splitting_tables.json", "w") as f:
        json.dump(allrows, f, indent=1)
    print("wrote splitting_tables.json")
