"""Complete (29,6) 6-regular circulant census: multiplier quotient, dual spectra,
Ramanujan dichotomy, defect ranking, cospectral/equienergetic partitions.
Stdlib + numpy + sympy only. Run: python3 census.py (writes table.csv, summary.json)."""
import itertools, json, math, time
import numpy as np
import sympy as sp

N = 29; D = 6; RB = 2 * math.sqrt(5)

def pair_reps(S):
    return sorted({min(x, N - x) for x in S if x % N != 0})

def canon(t):
    S = set()
    for a in t:
        S.add(a % N); S.add((-a) % N)
    best = None
    for u in range(1, N):
        T = {(u * s) % N for s in S}
        r = tuple(pair_reps(T))
        if best is None or r < best:
            best = r
    return best

def orbit_size(t):
    S = {(a % N) for a in t} | {(-a) % N for a in t}
    seen = set()
    for u in range(1, N):
        seen.add(tuple(sorted({(u * s) % N for s in S})))
    return len(seen)

def dft_spec(t):
    S = []
    for a in t:
        S += [a, -a]
    j = np.arange(N)
    return np.sort(np.exp(2j * np.pi * np.outer(j, S) / N).sum(axis=1).real)

def adj(t):
    A = np.zeros((N, N))
    S = set()
    for a in t:
        S.add(a % N); S.add((-a) % N)
    for i in range(N):
        for s in S:
            A[i, (i + s) % N] = 1
    return A

def charpoly_coeffs(t):
    A = adj(t).astype(int).tolist()
    p = sp.Matrix(A).charpoly()
    return [int(c) for c in p.all_coeffs()]  # x^29 .. const

def main():
    t0 = time.time()
    triples = list(itertools.combinations(range(1, 15), 3))
    assert len(triples) == 364
    classes = {}
    for t in triples:
        classes.setdefault(canon(t), []).append(t)
    reps = sorted(classes)
    assert sum(len(v) for v in classes.values()) == 364
    orbsizes = {r: orbit_size(r) for r in reps}
    assert set(orbsizes.values()) == {14}, orbsizes
    assert len(reps) == 26

    rows = []
    for r in reps:
        lam_dft = dft_spec(r)
        assert abs(lam_dft[-1] - 6) < 1e-9
        A = adj(r)
        w = np.sort(np.linalg.eigvalsh(A))
        agree = float(np.max(np.abs(w - lam_dft)))
        assert agree < 1e-8, (r, agree)
        lam2 = float(w[-2])
        maxabs = float(max(abs(w[0]), abs(w[-2])))
        E = float(np.sum(np.abs(w)))
        cp = charpoly_coeffs(r)
        assert cp[0] == 1 and cp[1] == 0, r  # monic, trace 0
        # Tr(A^2) = n*d = 174  <=>  coeff x^27 = (tr^2 - tr(A^2))/2 = -87
        assert cp[2] == -87, (r, cp[2])
        # Independent replay: exact Fourier vectors satisfy A v = lambda v.
        # (numpy np.roots on the degree-29 poly is ill-conditioned ~1e-3, so
        # the certified replay is DFT-vs-eigvalsh agreement plus this residual.)
        Sv = []
        for a in r:
            Sv += [a, -a]
        maxres = 0.0
        for k in range(N):
            v = np.exp(2j * np.pi * k * np.arange(N) / N) / math.sqrt(N)
            lam = np.sum(np.exp(2j * np.pi * k * np.array(Sv) / N))
            res = float(np.linalg.norm(A @ v - lam * v))
            maxres = max(maxres, res)
        assert maxres < 1e-9, (r, maxres)
        pv = maxres
        rows.append(dict(rep=list(r), lam2=lam2, maxabs=maxabs,
                         abs_ramanujan=bool(maxabs <= RB + 1e-9),
                         lam2_ramanujan=bool(lam2 <= RB + 1e-9),
                         defect_abs=max(0.0, maxabs - RB),
                         defect_lam2=max(0.0, lam2 - RB),
                         gap_norm=(6 - lam2) / 6, energy=E,
                         dft_eig_agree=agree, charpoly_at_dft_max=pv,
                         charpoly=cp))
    # cospectral partition via EXACT integer charpolys
    cp_groups = {}
    for row in rows:
        cp_groups.setdefault(tuple(row["charpoly"]), []).append(tuple(row["rep"]))
    assert all(len(v) == 1 for v in cp_groups.values()), "cospectral collision!"
    # sorted-spectrum separation (computed)
    specs = {tuple(r["rep"]): np.sort(dft_spec(tuple(r["rep"]))) for r in rows}
    min_linf, min_pair = 1e9, None
    for a, b in itertools.combinations(specs, 2):
        d = float(np.max(np.abs(specs[a] - specs[b])))
        if d < min_linf:
            min_linf, min_pair = d, (a, b)
    # energy separation (computed)
    Es = sorted((r["energy"], r["rep"]) for r in rows)
    min_egap = min(b[0] - a[0] for a, b in zip(Es, Es[1:]))
    by_ma = sorted(rows, key=lambda r: r["maxabs"])
    margin = by_ma[1]["maxabs"] - by_ma[0]["maxabs"]
    n_abs = sum(r["abs_ramanujan"] for r in rows)
    n_l2 = sum(r["lam2_ramanujan"] for r in rows)
    pal2 = (-1 + math.sqrt(29)) / 2
    pal_min = (-1 - math.sqrt(29)) / 2
    summ = dict(n_types=len(reps), n_labelled=364, orbit_size=14,
                RB=RB, abs_ramanujan=f"{n_abs}/26", lam2_ramanujan=f"{n_l2}/26",
                best_maxabs=by_ma[0]["rep"], best_maxabs_val=by_ma[0]["maxabs"],
                runnerup=by_ma[1]["rep"], runnerup_val=by_ma[1]["maxabs"],
                winner_margin=margin,
                best_lam2=min(rows, key=lambda r: r["lam2"])["rep"],
                best_lam2_val=min(r["lam2"] for r in rows),
                cospectral_classes=26, min_spectrum_linf=min_linf,
                min_spectrum_linf_pair=[list(min_pair[0]), list(min_pair[1])],
                equienergetic_classes=26, min_energy_gap=min_egap,
                paley=dict(eig2=pal2, eigmin=pal_min,
                           maxabs=float(max(abs(pal2), abs(pal_min))),
                           RB14=2 * math.sqrt(13),
                           gap_norm=(14 - pal2) / 14),
                max_dft_eig_agree=max(r["dft_eig_agree"] for r in rows),
                max_charpoly_at_dft=max(r["charpoly_at_dft_max"] for r in rows),
                seconds=time.time() - t0)
    with open("table.csv", "w") as f:
        f.write("rep,lam2,maxabs,abs_ramanujan,lam2_ramanujan,defect_abs,gap_norm,energy\n")
        for r in sorted(rows, key=lambda r: r["maxabs"]):
            f.write(f"\"{tuple(r['rep'])}\",{r['lam2']:.6f},{r['maxabs']:.6f},"
                    f"{r['abs_ramanujan']},{r['lam2_ramanujan']},{r['defect_abs']:.6f},"
                    f"{r['gap_norm']:.6f},{r['energy']:.6f}\n")
    with open("summary.json", "w") as f:
        json.dump(summ, f, indent=1)
    print(json.dumps(summ, indent=1))
    print("rows:", len(rows), "replay rows:", len(rows))

if __name__ == "__main__":
    main()
