"""Exhaustive e2 image census on A_n (n=5,6,7).
Convention: perms as arrays p with (p*q)(i)=p[q[i]]; inv standard.
e2(x,y) = [[x,y],y], [a,b] = a^{-1} b^{-1} a b.
Output: per A-class image counts N1(g), class sizes, cycle types, split info.
Saves JSON + prints tables. Pure stdlib + numpy.
"""
import itertools, json, sys
import numpy as np

def all_even_perms(n):
    out = []
    for p in itertools.permutations(range(n)):
        # sign via inversion parity
        inv = 0
        for i in range(n):
            pi = p[i]
            for j in range(i+1, n):
                if pi > p[j]: inv += 1
        if inv % 2 == 0:
            out.append(p)
    return np.array(out, dtype=np.int64)

def compose(a, b):
    # (a*b)(i) = a[b[i]]; a: (...,n), b: (...,n)
    return a[..., b]

def invert(P):
    inv = np.empty_like(P)
    idx = np.arange(P.shape[-1])
    inv[..., P] = idx  # works if P 1-D? for 2-D need advanced indexing
    return inv

def invert2(P):
    N, n = P.shape
    inv = np.empty_like(P)
    rows = np.arange(N)[:, None]
    inv[rows, P] = np.arange(n)[None, :]
    return inv

def cycle_type(p):
    n = len(p); seen = [False]*n; lens = []
    for i in range(n):
        if not seen[i]:
            j = i; L = 0
            while not seen[j]:
                seen[j] = True; j = p[j]; L += 1
            lens.append(L)
    lens.sort(reverse=True)
    return tuple(lens)

def a_classes(P):
    # A-conjugacy orbits by brute force: conjugate each orbit rep by all of A_n
    N, n = P.shape
    Pinv = invert2(P)
    cls = np.full(N, -1, dtype=np.int64)
    ncls = 0
    for i in range(N):
        if cls[i] != -1: continue
        # orbit of P[i] under conjugation by all g in P: g P[i] g^{-1}
        g = P  # (N,n)
        gi = Pinv
        x = P[i]  # (n,)
        # g x g^{-1}: tmp = x[g^{-1}[k]] then g[tmp[k]]
        conj = g[np.arange(N)[:,None], x[gi]] if False else None
        xg = x[gi]          # (N,n): x after g^{-1}
        conj = g[np.arange(N)[:, None], xg]  # (N,n)
        # mark all orbit members
        seen = set(map(tuple, conj.tolist()))
        # map tuple->index
        lut = {tuple(P[j].tolist()): j for j in range(N)}
        for t in seen:
            cls[lut[t]] = ncls
        ncls += 1
    return cls, ncls

def e2_image_counts(P):
    N, n = P.shape
    Pinv = invert2(P)
    counts = np.zeros(N, dtype=np.int64)
    lut = {tuple(P[j].tolist()): j for j in range(N)}
    # loop over x, vectorize over y
    for i in range(N):
        x = P[i]; xi = Pinv[i]
        Y = P; Yi = Pinv
        # c = [x,y] = x^{-1} y^{-1} x y, per y
        # x^{-1} y^{-1}: xi[Yi___] -> (N,n)
        xiyi = xi[Yi]            # (N,n)
        xy = x[Yi]               # careful: x*y^{-1}? we need x^{-1} y^{-1} x y
        # step: t1 = xi compose Yi: t1[k]=xi[Yi[k]]
        t1 = xi[Yi]
        # t2 = t1 compose x: t2[k] = t1[x[k]]? No: (t1*x)(k)=t1[x[k]]
        t2 = t1[:, x]
        # c = t2 compose Y: c[k] = t2[Y[k]]
        c = t2[np.arange(N)[:, None], Y]
        ci = np.empty_like(c)
        rows = np.arange(N)[:, None]
        ci[rows, c] = np.arange(n)[None, :]
        # e2 = [c,y] = c^{-1} y^{-1} c y
        u1 = ci[rows, Yi] if False else None
        # (ci * Yi): (ci o Yi)[k] = ci[Yi[k]]
        v1 = ci[np.arange(N)[:, None], Yi] if False else None
        # let's just do gathers step by step:
        # w1 = ci o Yi : w1[k]=ci[Yi[k]]
        w1 = np.take_along_axis(ci, Yi, axis=1)
        # w2 = w1 o c : w2[k] = w1[c[k]]
        w2 = np.take_along_axis(w1, c, axis=1)
        # e2 = w2 o Y : e[k] = w2[Y[k]]
        e = np.take_along_axis(w2, Y, axis=1)
        for row in e.tolist():
            counts[lut[tuple(row)]] += 1
        if (i+1) % 500 == 0:
            print(f"  x {i+1}/{N}", flush=True)
    return counts

def main(ns=(5, 6, 7)):
    report = {}
    for n in ns:
        print(f"=== A_{n} ===", flush=True)
        P = all_even_perms(n)
        N = len(P)
        print(f"|A_{n}| = {N}", flush=True)
        cls, ncls = a_classes(P)
        print(f"A-classes: {ncls}", flush=True)
        counts = e2_image_counts(P)
        print(f"total pairs: {counts.sum()} (expect {N*N})", flush=True)
        assert counts.sum() == N*N
        table = []
        for c in range(ncls):
            idx = np.where(cls == c)[0]
            ct = cycle_type(P[idx[0]])
            table.append({"class": c, "size": int(len(idx)),
                          "cycle_type": list(ct),
                          "N1_per_elt": int(counts[idx[0]]),
                          "uniform": bool(np.all(counts[idx] == counts[idx[0]]))})
            print(f"  class {c}: size={len(idx)} ctype={ct} N1={counts[idx[0]]} uniform={np.all(counts[idx]==counts[idx[0]])}")
        missing = [t for t in table if t["N1_per_elt"] == 0]
        print(f"  missing classes: {len(missing)}", flush=True)
        report[str(n)] = {"N": N, "nclasses": ncls, "table": table,
                          "missing": missing}
    with open("output/artifacts/e2_census.json", "w") as f:
        json.dump(report, f, indent=1)
    print("saved output/artifacts/e2_census.json")

if __name__ == "__main__":
    main()
