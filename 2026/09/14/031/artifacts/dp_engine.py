"""Exact transfer-matrix DP for bond-percolation LR crossing on [0,n]x[0,n] vertex box.

State: connectivity partition of the active frontier + per-block (touches-left,
touches-right) flags accumulated over all members ever in the block (including
retired vertices). A block with both flags = an L-R connection exists; its
weight is absorbed into `crossed` (which is also multiplied by (a+b) every
step to account for the free future edges). Weights are exact integers:
probability at p=a/(a+b) = crossed / (a+b)^E.
"""
import argparse


def build(n, order="row"):
    N = n + 1

    def vid(x, y):
        return y * N + x

    edges = []
    if order == "row":
        for y in range(N):
            for x in range(N):
                if x < n:
                    edges.append((vid(x, y), vid(x + 1, y)))
                if y < n:
                    edges.append((vid(x, y), vid(x, y + 1)))
    elif order == "col":
        for x in range(N):
            for y in range(N):
                if y < n:
                    edges.append((vid(x, y), vid(x, y + 1)))
                if x < n:
                    edges.append((vid(x, y), vid(x + 1, y)))
    else:
        raise ValueError(order)
    E = len(edges)
    assert E == 2 * n * N, (E, n)
    inc = {v: [] for v in range(N * N)}
    for i, (u, v) in enumerate(edges):
        inc[u].append(i)
        inc[v].append(i)
    first = {v: min(l) for v, l in inc.items()}
    last = {v: max(l) for v, l in inc.items()}
    active = []
    for i in range(E):
        s = [v for v in range(N * N) if first[v] <= i and last[v] > i]
        s.sort()
        active.append(s)
    return N, n, edges, active


def precompute(N, n, edges, active):
    E = len(edges)
    XR = lambda v: (v % N) == n
    X0 = lambda v: (v % N) == 0
    plan = []
    prevkeep = []
    prevset = set()
    for i, (u, v) in enumerate(edges):
        act = active[i]
        actset = set(act)
        W = sorted(prevset | {u, v})
        pos = {w: k for k, w in enumerate(W)}
        iu, iv = pos[u], pos[v]
        w_old = [(-1) for _ in W]
        w_init = [None] * len(W)
        prevkeeppos = {w: k for k, w in enumerate(prevkeep)}
        for k, w in enumerate(W):
            if w in prevkeeppos:
                w_old[k] = prevkeeppos[w]
            else:
                w_init[k] = (X0(w), XR(w))
        keep = [k for k, w in enumerate(W) if w in actset]
        plan.append((W, w_old, w_init, keep, iu, iv))
        prevkeep = [w for w in W if w in actset]
        prevset = actset
    return plan


def _canon(lab, flagL, flagR, keep):
    newid = {}
    nl = []
    for k in keep:
        l = lab[k]
        if l not in newid:
            newid[l] = len(newid)
        nl.append(newid[l])
    nf = [None] * len(newid)
    for l, j in newid.items():
        nf[j] = (flagL[l], flagR[l])
    return (tuple(nl), tuple(nf))


def solve(n, a, b, order="row", verbose=False):
    N, n, edges, active = build(n, order)
    plan = precompute(N, n, edges, active)
    # dp: {(labels, ((L,R),...)): weight}; labels/flags indexed by block id
    dp = {((), ()): 1}
    crossed = 0
    maxstates = 0
    for step, (W, w_old, w_init, keep, iu, iv) in enumerate(plan):
        nW = len(W)
        crossed = crossed * (a + b)
        dp2 = {}
        for (labels, flags), wgt in dp.items():
            lab = [0] * nW
            fL = {}
            fR = {}
            nm = (max(labels) + 1) if labels else 0
            for k in range(nW):
                o = w_old[k]
                if o >= 0:
                    lab[k] = labels[o]
                    fL[k] = flags[labels[o]][0]
                    fR[k] = flags[labels[o]][1]
                else:
                    lab[k] = nm
                    nm += 1
                    fL[k], fR[k] = w_init[k]

            # closed branch: blocks unchanged
            def block_flags(lab, fL, fR):
                bL, bR = {}, {}
                for k in range(nW):
                    l = lab[k]
                    bL[l] = bL.get(l, False) or fL[k]
                    bR[l] = bR.get(l, False) or fR[k]
                return bL, bR

            bL, bR = block_flags(lab, fL, fR)
            hit_c = any(bL[l] and bR[l] for l in bL)
            if hit_c:
                crossed += wgt * b
            else:
                key_c = _canon(lab, bL, bR, keep)
                dp2[key_c] = dp2.get(key_c, 0) + wgt * b
            # open branch: merge lv into lu
            lu, lv = lab[iu], lab[iv]
            lab2 = [lu if t == lv else t for t in lab]
            bL2, bR2 = block_flags(lab2, fL, fR)
            hit_o = any(bL2[l] and bR2[l] for l in bL2)
            if hit_o:
                crossed += wgt * a
            else:
                key_o = _canon(lab2, bL2, bR2, keep)
                dp2[key_o] = dp2.get(key_o, 0) + wgt * a
        dp = dp2
        if len(dp) > maxstates:
            maxstates = len(dp)
        if verbose and (step % 20 == 0):
            print(f"  edge {step}/{len(plan)} states={len(dp)}", flush=True)
    uncrossed = sum(dp.values())
    total = crossed + uncrossed
    return {"crossed": crossed, "uncrossed": uncrossed, "total": total,
            "E": len(edges), "maxstates": maxstates, "nstates_final": len(dp)}


def brute(n, a, b):
    """Exhaustive enumeration (for small n only). Returns crossed weight."""
    N = n + 1

    def vid(x, y):
        return y * N + x

    edges = []
    for y in range(N):
        for x in range(n):
            edges.append((vid(x, y), vid(x + 1, y)))
    for y in range(n):
        for x in range(N):
            edges.append((vid(x, y), vid(x, y + 1)))
    E = len(edges)
    crossed = 0
    for mask in range(1 << E):
        parent = list(range(N * N))

        def find(q):
            while parent[q] != q:
                parent[q] = parent[parent[q]]
                q = parent[q]
            return q

        k = 0
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                k += 1
                ru, rv = find(u), find(v)
                if ru != rv:
                    parent[ru] = rv
        L = {find(vid(0, y)) for y in range(N)}
        hit = any(find(vid(n, y)) in L for y in range(N))
        w = (a ** k) * (b ** (E - k))
        if hit:
            crossed += w
    return crossed, E


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=8)
    ap.add_argument("--a", type=int, default=101)
    ap.add_argument("--b", type=int, default=99)
    ap.add_argument("--order", default="row")
    ap.add_argument("--brute", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    if args.brute:
        c, E = brute(args.n, args.a, args.b)
        print(f"brute n={args.n} a={args.a} b={args.b} E={E} crossed={c}")
        return
    r = solve(args.n, args.a, args.b, args.order, args.verbose)
    E = r["E"]
    print(f"dp n={args.n} order={args.order} a={args.a} b={args.b} E={E}")
    print(f"crossed={r['crossed']}")
    print(f"uncrossed={r['uncrossed']}")
    print(f"total={r['total']}")
    print(f"checksum (a+b)^E match: {r['total'] == (args.a + args.b) ** E}")
    print(f"maxstates={r['maxstates']} finalstates={r['nstates_final']}")
    from fractions import Fraction
    print(f"P = {Fraction(r['crossed'], (args.a + args.b) ** E)} ~= {r['crossed'] / ((args.a + args.b) ** E):.10f}")


if __name__ == "__main__":
    main()
