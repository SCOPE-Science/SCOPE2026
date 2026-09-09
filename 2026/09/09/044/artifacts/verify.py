#!/usr/bin/env python3
"""Independent replay: MN removing SMALLEST part first, full re-derive, cross-checks."""
import json, math, itertools, os
from functools import lru_cache
_HERE = os.path.dirname(os.path.abspath(__file__))

def partitions(n, maxp=None):
    if n == 0: yield (); return
    if maxp is None: maxp = n
    for f in range(min(maxp, n), 0, -1):
        for rest in partitions(n - f, f):
            yield (f,) + rest

def centralizer(mu):
    from collections import Counter
    c = Counter(mu); z = 1
    for l, m in c.items(): z *= math.factorial(m) * (l ** m)
    return z

def rim_hooks(la, m):
    cells = [(i, j) for i in range(len(la)) for j in range(la[i])]
    out = []
    for S in itertools.combinations(cells, m):
        S = set(S)
        rem = [r for r in cells if r not in S]
        ok = True
        for (i, j) in rem:
            if j > 0 and (i, j - 1) not in rem:
                ok = False; break
        if not ok: continue
        if rem:
            rl = {}
            for (i, j) in rem: rl[i] = rl.get(i, 0) + 1
            ks = sorted(rl)
            if ks != list(range(max(ks) + 1)): continue
            lens = [rl[k] for k in ks]
            if any(lens[a] < lens[a + 1] for a in range(len(lens) - 1)): continue
            rem_la = tuple(x for x in lens if x > 0)
            if sum(rem_la) != sum(la) - m: continue
        else:
            rem_la = ()
        stack = [next(iter(S))]; seen = {stack[0]}
        while stack:
            i, j = stack.pop()
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                q = (i + d[0], j + d[1])
                if q in S and q not in seen: seen.add(q); stack.append(q)
        if seen != S: continue
        bad = False
        for (i, j) in S:
            if (i + 1, j) in S and (i, j + 1) in S and (i + 1, j + 1) in S:
                bad = True; break
        if bad: continue
        rows = len(set(i for i, j in S))
        out.append((rem_la, (-1) ** (rows - 1)))
    return out

def make_chi_smallest_first():
    @lru_cache(maxsize=None)
    def chi(la, mu):
        if sum(la) == 0: return 1 if sum(mu) == 0 else 0
        if not mu: return 0
        m = mu[-1]; rest = mu[:-1]  # DIFFERENT recursion order vs compute.py
        t = 0
        for rem, sgn in rim_hooks(la, m):
            t += sgn * chi(rem, rest)
        return t
    return chi

def square_type(mu):
    out = []
    for L in mu:
        if L % 2 == 1: out.append(L)
        else: out.extend([L // 2, L // 2])
    return tuple(sorted(out, reverse=True))

def sign_of(mu):
    return (-1) ** (sum(mu) - len(mu))

def transpose(la):
    if not la: return ()
    return tuple(sum(1 for r in la if r > c) for c in range(la[0]))

def main():
    disk = json.load(open(os.path.join(_HERE, "splitting_tables.json")))
    allok = True
    global_best = (0, None)
    for n in (6, 7, 8):
        chi = make_chi_smallest_first()
        parts = list(partitions(n)); idx = {p: i for i, p in enumerate(parts)}
        fact = math.factorial(n)
        table = [[chi(la, mu) for mu in parts] for la in parts]
        dims = [table[i][idx[tuple([1] * n)]] for i in range(len(parts))]
        assert sum(d * d for d in dims) == fact
        # column orthogonality + transpose symmetry (independent structural checks)
        for k in range(len(parts)):
            for l in range(len(parts)):
                s = sum(table[a][k] * table[a][l] for a in range(len(parts)))
                assert s == (centralizer(parts[k]) if k == l else 0), f"col orth n={n}"
        for la in parts:
            lt = transpose(la)
            for mu in parts:
                assert table[idx[la]][idx[mu]] * sign_of(mu) == table[idx[lt]][idx[mu]], "transpose"
        sqmap = [idx[square_type(mu)] for mu in parts]
        clsizes = [fact // centralizer(mu) for mu in parts]
        diskrows = {(tuple(r["lambda"]), tuple(r["nu"])): r for r in disk[str(n)]["rows"]}
        expect_targets = {tuple(t) for t in disk[str(n)]["targets"]}
        targets = [la for la in parts if len(la) == 3 and la[1] >= 2]
        assert {tuple(t) for t in targets} == expect_targets, "target family mismatch"
        assert len(targets) == [None, None, None, None, None, None, 2, 3, 4][n]
        nchecked = 0
        for la in targets:
            li = idx[la]; d = dims[li]
            for nu in parts:
                ni = idx[nu]
                Sg = sum(table[li][k] ** 2 * table[ni][k] * clsizes[k] for k in range(len(parts)))
                Sm = sum(table[li][sqmap[k]] * table[ni][k] * clsizes[k] for k in range(len(parts)))
                assert Sg % fact == 0 and Sm % fact == 0, f"non-integral class sum n={n} {la} {nu}"
                g, m = Sg // fact, Sm // fact
                s, a = (g + m) // 2, (g - m) // 2
                dr = diskrows[(la, nu)]
                assert (dr["s"], dr["a"], dr["g"], dr["m"]) == (s, a, g, m), \
                    f"MISMATCH n={n} {la}x{nu}: disk {dr} vs replay {(s,a,g,m)}"
                if abs(m) > global_best[0]: global_best = (abs(m), (n, la, nu, s, a, g, m))
                nchecked += 1
        print(f"n={n}: replay VERIFY_OK over {nchecked} rows "
              f"({len(targets)} squares x {len(parts)} constituents)")
    print("GLOBAL MAX GAP:", global_best)
    g = global_best[1]
    n, la, nu, s, a, gg, m = g
    print(f"certificate: n={n} lam={la} nu={nu} (s,a,g,m)={(s,a,gg,m)}; "
          f"class sum S_m = m*n! = {m*math.factorial(n)}")
    print("ALL VERIFY_OK")

main()
