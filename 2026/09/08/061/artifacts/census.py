"""Linear-extension census over all unlabelled posets n<=8 from Chapel Hill StdPsts seeds.

Child form semantics (datastrc.html): element k's list = elements covered by k
(lower covers), naturally labelled, 1-based in files.
We parse each line into cover pairs (j -> k) for j in covers[k], then all
computations use only the transitive closure (pred bitmasks).
"""
import ast, math, sys, json
from fractions import Fraction

def parse_childform(line):
    t = line.decode().strip().replace('{', '[').replace('}', ']')
    return ast.literal_eval(t)

def analyze(covers0):
    n = len(covers0)
    # pred masks: direct lower covers (0-based), natural labelling => j<k
    pred = [0]*n
    for k, lst in enumerate(covers0):
        for j in lst:
            pred[k] |= (1 << (j-1))
    # transitive closure
    ch = [pred[k] for k in range(n)]
    for m in range(n):
        pm = ch[m]
        for k in range(n):
            if (ch[k] >> m) & 1:
                ch[k] |= pm
    pred = ch
    full = (1 << n) - 1
    # down-sets test: I is ideal iff for every k in I, pred[k] subset I
    is_ideal = bytearray(1 << n)
    for mask in range(1 << n):
        ok = True
        mm = mask
        while mm:
            lsb = mm & (-mm)
            k = lsb.bit_length() - 1
            if pred[k] & ~mask:
                ok = False; break
            mm ^= lsb
        is_ideal[mask] = ok
    nideals = sum(is_ideal)
    # Path A: bottom-up DP over ideals: dp[I] = #extensions of subposet I
    dp = [0]*(1 << n)
    dp[0] = 1
    for mask in range(1 << n):
        if not is_ideal[mask] or dp[mask] == 0:
            continue
        # add any minimal element of complement
        for k in range(n):
            if (mask >> k) & 1: continue
            if pred[k] & ~mask == 0:
                nm = mask | (1 << k)
                dp[nm] += dp[mask]
    e = dp[full]
    # Path B: top-down recursion removing minimal elements (memoized on down-set complement mask)
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def rec(remaining):
        # remaining: bitmask of not-yet-placed elements, must be an upset
        if remaining == 0: return 1
        tot = 0
        r = remaining
        while r:
            lsb = r & (-r)
            k = lsb.bit_length() - 1
            if pred[k] & remaining == 0:  # k minimal in remaining
                tot += rec(remaining ^ (1 << k))
            r ^= lsb
        return tot
    eB = rec(full)
    assert e == eB, (e, eB)
    # comparability
    def le(a, b):
        return a == b or ((pred[b] >> a) & 1)
    pairs = []
    for x in range(n):
        for y in range(x+1, n):
            if not le(x, y) and not le(y, x):
                pairs.append((x, y))
    # forest test: each element covered by at most one element (each j in <=1 list)
    covercount = [0]*n
    for k, lst in enumerate(covers0):
        for j in lst:
            covercount[j-1] += 1
    is_forest = all(c <= 1 for c in covercount)
    hook = None
    if is_forest:
        # build tree parent (coverer) and children; hooks = subtree sizes
        parent = [-1]*n
        for k, lst in enumerate(covers0):
            for j in lst:
                parent[j-1] = k
        children = [[] for _ in range(n)]
        for j, p in enumerate(parent):
            if p >= 0: children[p].append(j)
        sys.setrecursionlimit(10000)
        def sz(k):
            s = 1
            for c in children[k]:
                s += sz(c)
            return s
        hooks = [sz(k) for k in range(n)]
        hook = math.factorial(n)
        for h in hooks:
            hook //= h
        assert hook == e, (covers0, hooks, hook, e)
    return {
        'n': n, 'e': e, 'nideals': nideals, 'npairs': len(pairs),
        'is_forest': is_forest, 'pred': pred, 'pairs': pairs,
    }

def sorting_probs(pred, pairs, e_full):
    """For each incomparable {x,y} compute e_xy = e(P + x<y) by ideal DP on augmented preds."""
    n = len(pred)
    full = (1 << n) - 1
    out = []
    for (x, y) in pairs:
        res = {}
        for (a, b) in ((x, y), (y, x)):
            aug = list(pred)
            # add relation a<b: pred'[b] |= pred[a] + {a}, propagate transitively
            add = (aug[a] | (1 << a))
            aug[b] |= add
            # closure: iterate
            for m in range(n):
                pm = aug[m]
                for k in range(n):
                    if (aug[k] >> m) & 1:
                        aug[k] |= pm
            # need full reclosure (loops until stable) - do Floyd style twice more
            changed = True
            while changed:
                changed = False
                for m in range(n):
                    pm = aug[m]
                    for k in range(n):
                        if (aug[k] >> m) & 1:
                            new = aug[k] | pm
                            if new != aug[k]:
                                aug[k] = new; changed = True
            # ideal DP
            dp = [0]*(1 << n)
            dp[0] = 1
            for mask in range(1 << n):
                if dp[mask] == 0: continue
                # check ideal
                mm = mask; ok = True
                while mm:
                    lsb = mm & (-mm); k = lsb.bit_length()-1
                    if aug[k] & ~mask: ok = False; break
                    mm ^= lsb
                if not ok: continue
                for k in range(n):
                    if (mask >> k) & 1: continue
                    if aug[k] & ~mask == 0:
                        dp[mask | (1 << k)] += dp[mask]
            res[(a, b)] = dp[full]
        exy = res[(x, y)]; eyx = res[(y, x)]
        assert exy + eyx == e_full, (exy, eyx, e_full)
        out.append((x, y, exy, eyx))
    return out

def run(nlo=1, nhi=8, datadir='data'):
    import pathlib
    rows = []   # (n, idx, covers_str, e, nideals, npairs, is_forest)
    agg = {}
    for n in range(nlo, nhi+1):
        lines = pathlib.Path(f'{datadir}/stdpsts{n}').read_bytes().splitlines()
        emax = -1; emax_id = None; emin = None; emin_id = None
        nforest = 0; nchains = 0
        worst_lop = None  # (minfrac, idx, x, y, exy, e) most lopsided pair
        best_delta = None # min over non-chain P of delta(P)
        best_delta_info = None
        all_balanced_ok = True
        nnonchain = 0
        for i, ln in enumerate(lines, start=1):
            covers0 = parse_childform(ln)
            assert len(covers0) == n
            # natural-labelling sanity: all covers j<=k (1-based j-1<k)
            for k, lst in enumerate(covers0):
                for j in lst:
                    assert 1 <= j <= n and j-1 < k, (n, i, covers0)
            r = analyze(covers0)
            if r['is_forest']: nforest += 1
            if r['npairs'] == 0:
                nchains += 1
                assert r['e'] == 1
            e = r['e']
            rows.append((n, i, ln.decode().strip(), e, r['nideals'], r['npairs'], r['is_forest']))
            if e > emax: emax, emax_id = e, i
            if emin is None or e < emin: emin, emin_id = e, i
            if r['pairs']:
                nnonchain += 1
                sp = sorting_probs(r['pred'], r['pairs'], e)
                # delta(P) = max over pairs of min(exy,eyx)/e
                dnum = -1; dinfo = None
                for (x, y, exy, eyx) in sp:
                    lo = min(exy, eyx)
                    # track globally most lopsided (min over pairs of lo/e)
                    fr = Fraction(lo, e)
                    if worst_lop is None or fr < worst_lop[0]:
                        worst_lop = (fr, i, x+1, y+1, lo, e)
                    if lo * 3 >= e:  # candidate balanced (>=1/3); track max
                        pass
                    if dnum < 0 or Fraction(lo, e) > dnum:
                        from fractions import Fraction as F
                        dnum = Fraction(lo, e); dinfo = (x+1, y+1, exy, eyx)
                if best_delta is None or dnum < best_delta:
                    best_delta = dnum; best_delta_info = (i, dinfo, e)
                if dnum < Fraction(1, 3):
                    all_balanced_ok = False
                    print(f'UNBALANCED n={n} id={i} delta={dnum} e={e}', flush=True)
        agg[n] = dict(nclasses=len(lines), emax=(emax, emax_id), emin=(emin, emin_id),
                      nforest=nforest, nchains=nchains, nnonchain=nnonchain,
                      worst_lop=tuple(worst_lop) if worst_lop else None,
                      best_delta=(str(best_delta), best_delta_info) if best_delta else None,
                      all_balanced=all_balanced_ok)
        print(f'n={n}: classes={len(lines)} emax={emax}@{emax_id} emin={emin}@{emin_id} '
              f'forest={nforest} chains={nchains} worst_lop={worst_lop} best_delta={best_delta}@{best_delta_info} balanced_ok={all_balanced_ok}', flush=True)
    return rows, agg

if __name__ == '__main__':
    import sys
    nlo = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    nhi = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    rows, agg = run(nlo, nhi)
    import csv
    with open(f'output/census_n{nlo}_{nhi}.csv', 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(['n', 'id', 'childform', 'e', 'nideals', 'nincomp_pairs', 'is_forest'])
        w.writerows(rows)
    with open(f'output/agg_n{nlo}_{nhi}.json', 'w') as f:
        json.dump(agg, f, indent=1, default=str)
    print('wrote outputs')
