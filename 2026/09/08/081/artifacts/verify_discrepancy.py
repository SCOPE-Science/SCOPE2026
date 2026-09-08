#!/usr/bin/env python3
"""Exact star-discrepancy table for Fibonacci lattices F_5..F_12 (stdlib only).

Method (exact integer arithmetic):
  Lattice m: N = F_m, generator g = F_{m-1}; points (k/N, {(k*g mod N)/N}).
  Both coordinates lie on (1/N)Z, so with a,b in 1..N and C = point count in
  the anchored box, deviation = |C - a*b/N| / N = |C*N - a*b| / N^2.
  The sup over all anchored boxes is attained on this (N+1)^2 grid considering
  both closed [0,a/N]x[0,b/N] and half-open [0,a/N)x[0,b/N) boxes
  (volume varies continuously while the count is locally constant).
  All counts via 2D prefix sums; cross-checked by an independent O(N^3) brute
  force over point-defined boxes. Discrepancy reported as exact reduced
  fraction bestnum/N^2.

Also (exact integer logs):
  * dual-lattice / spectral-test witness: shortest nonzero h with h1+h2*g=0 mod N
    (these are exactly the frequencies with Weyl sum |S(h)| = 1);
  * three-distance gap census for the golden-ratio rotation at N = F_m;
  * Kronecker-sequence rows (float ranks with asserted separation margins).

Exits nonzero on any failed internal check. Prints VERIFY_OK on success.
"""
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))

def fib_list(n):
    F = [None, 1, 1]
    while len(F) <= n:
        F.append(F[-1] + F[-2])
    return F

def star_disc_fib_prefix(N, g):
    occ = [[0] * N for _ in range(N)]
    for k in range(N):
        occ[k][(k * g) % N] += 1
    S = [[0] * N for _ in range(N)]
    for a in range(N):
        run = 0
        for b in range(N):
            run += occ[a][b]
            S[a][b] = run + (S[a - 1][b] if a > 0 else 0)

    def C(a, b):
        if a < 0 or b < 0:
            return 0
        return S[min(a, N - 1)][min(b, N - 1)]

    best = -1
    wit = None
    for a in range(0, N + 1):
        for b in range(0, N + 1):
            for typ, Cv in (("closed", C(a, b)), ("open", C(a - 1, b - 1)),
                             ("mixed1", C(a, b - 1)), ("mixed2", C(a - 1, b))):
                num = abs(Cv * N - a * b)
                if num > best:
                    best = num
                    wit = (a, b, typ, Cv)
    return best, wit

def star_disc_fib_bruteforce(N, g):
    pts = [(k, (k * g) % N) for k in range(N)]
    xs = sorted(set(p[0] for p in pts))
    ys = sorted(set(p[1] for p in pts))
    best = -1
    wit = None
    for a in xs + [N]:
        for b in ys + [N]:
            nc = sum(1 for (x, y) in pts if x <= a and y <= b)
            no = sum(1 for (x, y) in pts if x < a and y < b)
            nm1 = sum(1 for (x, y) in pts if x <= a and y < b)
            nm2 = sum(1 for (x, y) in pts if x < a and y <= b)
            for typ, Cv in (("closed", nc), ("open", no),
                            ("mixed1", nm1), ("mixed2", nm2)):
                num = abs(Cv * N - a * b)
                if num > best:
                    best = num
                    wit = (a, b, typ, Cv)
    return best, wit

def spectral_witness(N, g, H):
    """Shortest nonzero dual vector (exact), plus dual hits in ||h||_inf <= H."""
    best = None
    hits = []
    for h1 in range(-N, N + 1):
        for h2 in range(-N, N + 1):
            if h1 == 0 and h2 == 0:
                continue
            if (h1 + h2 * g) % N == 0:
                n2 = h1 * h1 + h2 * h2
                if best is None or n2 < best[0]:
                    best = (n2, (h1, h2))
                if max(abs(h1), abs(h2)) <= H:
                    hits.append((h1, h2))
    return best, hits

def three_distance_census(N, alpha):
    pts = sorted(((k * alpha) % 1.0) for k in range(N))
    gaps = [pts[i + 1] - pts[i] for i in range(N - 1)] + [pts[0] + 1.0 - pts[-1]]
    assert abs(sum(gaps) - 1.0) < 1e-9, "gaps must sum to 1"
    clusters = []
    for v in sorted(gaps):
        for c in clusters:
            if abs(v - c[0]) < 1e-9:
                c[1] += 1
                break
        else:
            clusters.append([v, 1])
    assert len(clusters) <= 3, "three-distance theorem violated!"
    assert sum(c[1] for c in clusters) == N
    return sorted((v, c) for v, c in clusters)

def star_disc_kronecker(N, alpha, beta):
    xs = [((k * alpha) % 1.0) for k in range(N)]
    ys = [((k * beta) % 1.0) for k in range(N)]
    sx, sy = sorted(xs), sorted(ys)
    mgx = min(sx[i + 1] - sx[i] for i in range(N - 1))
    mgy = min(sy[i + 1] - sy[i] for i in range(N - 1))
    assert mgx > 1e-9 and mgy > 1e-9, "coordinate separation too small for float ranks"
    ox = sorted(range(N), key=lambda i: xs[i])
    oy = sorted(range(N), key=lambda i: ys[i])
    rx, ry = [0] * N, [0] * N
    for r, i in enumerate(ox):
        rx[i] = r
    for r, i in enumerate(oy):
        ry[i] = r
    best = -1.0
    wit = None
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            for (cx, sgnx) in ((a - 1, 0), (a - 2, 1)):
                # closed side if sgnx=0 (coordinate sx[a-1]), open side if sgnx=1
                vx = sx[a - 1] if sgnx == 0 else (sx[a - 2] if a - 2 >= 0 else None)
                for (cy, sgny) in ((b - 1, 0), (b - 2, 1)):
                    vy = sy[b - 1] if sgny == 0 else (sy[b - 2] if b - 2 >= 0 else None)
                    if vx is None or vy is None:
                        continue
                    vol = vx * vy
                    px = (lambda i: rx[i] <= a - 1) if sgnx == 0 else (lambda i: rx[i] < a - 1)
                    py = (lambda i: ry[i] <= b - 1) if sgny == 0 else (lambda i: ry[i] < b - 1)
                    Cv = sum(1 for i in range(N) if px(i) and py(i))
                    typ = ("closed" if sgnx == 0 else "open") + "/" + \
                          ("closed" if sgny == 0 else "open")
                    d = abs(Cv / N - vol)
                    if d > best:
                        best = d
                        wit = (vx, vy, typ, Cv)
    return best, wit, mgx, mgy

def main():
    F = fib_list(12)
    assert [F[m] for m in range(5, 13)] == [5, 8, 13, 21, 34, 55, 89, 144]
    PHI_INV = (math.sqrt(5.0) - 1.0) / 2.0
    SQRT2M1 = math.sqrt(2.0) - 1.0
    H = 12
    lines = []
    lines.append("EXACT STAR-DISCREPANCY TABLE: Fibonacci lattices F_m, m=5..12")
    lines.append("lattice: N=F_m, generator g=F_{m-1}, points (k/N, {(k*g mod N)/N})")
    lines.append("")
    fib_rows = []
    for m in range(5, 13):
        N, g = F[m], F[m - 1]
        b1, w1 = star_disc_fib_prefix(N, g)
        b2, w2 = star_disc_fib_bruteforce(N, g)
        assert b1 == b2, f"prefix/bruteforce mismatch at N={N}: {b1} vs {b2}"
        dd = math.gcd(b1, N * N)
        frac = f"{b1 // dd}/{N * N // dd}"
        dec = b1 / (N * N)
        spec, hits = spectral_witness(N, g, H)
        # Fourier diagnostic Q_H = sum_{0<||h||<=H} |S(h)|/r(h); |S| is 1 on dual hits else 0
        q = sum(1.0 / (max(1, abs(h1)) * max(1, abs(h2))) for (h1, h2) in hits)
        a, b, typ, Cv = w1
        lines.append(
            f"m={m}: N={N} g={g} D*num={b1} D*={frac} = {dec:.10f} "
            f"extremal box a={a}/N b={b}/N ({typ}, count={Cv}) "
            f"spectral h*={spec[1]} |h*|^2={spec[0]} dualhits(H={H})={len(hits)} Q_H={q:.6f}"
        )
        fib_rows.append({"m": m, "N": N, "g": g, "num": b1,
                         "frac": frac, "dec": dec, "wit": w1,
                         "spec_h": spec[1], "spec_n2": spec[0],
                         "dualhits": len(hits), "Q_H": q})
    lines.append("")
    lines.append("THREE-DISTANCE CENSUS: golden-ratio rotation alpha=(sqrt5-1)/2, N=F_m")
    td_rows = []
    for m in range(5, 13):
        N = F[m]
        cl = three_distance_census(N, PHI_INV)
        s = " + ".join(f"{c}x{round(v, 12)}" for v, c in cl)
        ming = min(v for v, c in cl)
        lines.append(f"N={N}: {len(cl)} distinct gap(s): {s} | N*mingap={N * ming:.10f}")
        td_rows.append({"N": N, "ngaps": len(cl),
                        "gaps": [(v, c) for v, c in cl], "Nmingap": N * ming})
    lines.append("")
    lines.append("KRONECKER ROWS: v=(phi^-1, sqrt2-1), first N points ({k a},{k b})")
    kr_rows = []
    for m in range(5, 13):
        N = F[m]
        d, w, mgx, mgy = star_disc_kronecker(N, PHI_INV, SQRT2M1)
        lines.append(
            f"N={N}: D*={d:.10f} (float; rank margins {mgx:.3e},{mgy:.3e}) "
            f"extremal x={w[0]:.10f} y={w[1]:.10f} ({w[2]}, count={w[3]})"
        )
        kr_rows.append({"N": N, "Dstar": d, "wit": w, "margins": (mgx, mgy)})
    lines.append("")
    lines.append("VERIFY_OK")
    out = "\n".join(lines) + "\n"
    print(out, end="")
    with open(os.path.join(HERE, "run_log.txt"), "w") as f:
        f.write(out)
    import json as J
    with open(os.path.join(HERE, "table.json"), "w") as f:
        J.dump({"fib": fib_rows, "threedist": td_rows, "kronecker": kr_rows}, f, indent=1)

if __name__ == "__main__":
    main()
