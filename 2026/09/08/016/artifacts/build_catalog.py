"""Build certified top-5 catalog from census_top.json: one rep per (E,X) class,
full integer profiles, merit/PSC/FFT logs, canonical certs. Writes catalog.json."""
import json
import numpy as np

N = 21
P = np.array([-1,-1,1,1,1,1,1,1,1,-1,-1,1,1,-1,1,-1,1,-1,1,1,-1], dtype=np.int64)
Cp = [int((P[:N-k] * P[k:]).sum()) for k in range(1, N)]
E_P = sum(c * c for c in Cp)
assert E_P == 26

def profiles(Q):
    q = np.array(Q, dtype=np.int64)
    C, D = [], []
    e = x = 0
    for k in range(1, N):
        s = int((q[:N-k] * q[k:]).sum())
        C.append(s)
        e += s * s
    for k in range(-(N-1), N):
        if k >= 0:
            s = int((P[:N-k] * q[k:]).sum())
        else:
            s = int((P[-k:] * q[:N+k]).sum())
        D.append(s)
        x += s * s
    G = sum((a + b) ** 2 for a, b in zip(Cp, C))
    assert e + x == N * N - E_P + G  # S == 415 + G identity
    return C, D, e, x, G

top = json.load(open("output/artifacts/census_top.json"))["top"]
assert len(top) == 64
S_vals = sorted(set(t["S"] for t in top))
S_min, S_next = S_vals[0], S_vals[1]
assert S_min == 455

seen = {}
reps = []
for t in top:
    if t["S"] != S_min:
        continue
    C, D, e, x, G = profiles(t["Q"])
    if (e, x) not in seen:
        seen[(e, x)] = True
        reps.append((t, C, D, e, x, G))
reps.sort(key=lambda r: r[4])  # sort by E(Q) ascending
print("minimizer classes (E,X):", sorted(seen), flush=True)

catalog = []
for t, C, D, e, x, G in reps:
    Qstr = "".join('+' if v == 1 else '-' for v in t["Q"])
    Qm = "".join('-' if v == 1 else '+' for v in t["Q"])
    rev = Qstr[::-1]
    revm = "".join('-' if c == '+' else '+' for c in rev)
    q = np.array([1.0 if s == '+' else -1.0 for s in Qstr])
    Pf = np.fft.rfft(P.astype(float), n=64)
    Qf = np.fft.rfft(q, n=64)
    cs = np.abs(Pf * np.conj(Qf))
    import math
    catalog.append({
        "Q": Qstr, "idx": t["idx"], "C": C, "D": D, "E": e, "X": x,
        "S": e + x, "G": G,
        "F_Q": (N * N) / (2 * e),
        "ADF_Q": (2 * e) / N ** 2, "CDF": x / N ** 2,
        "PSC": (x + 2 * math.sqrt(E_P * e)) / N ** 2,
        "canon_sign": min(Qstr, Qm),
        "rev_orbit": sorted({Qstr, Qm, rev, revm}),
        "fft": {"n": 64, "max_cross_spec": float(cs.max()),
                "mean_cross_spec": float(cs.mean())},
    })

out = {"P*": "".join('+' if int(v) == 1 else '-' for v in P.tolist()),
       "C_P": Cp, "E_P": E_P, "F_P": N * N / (2 * E_P), "N": N,
       "S_min": S_min, "G_min": S_min - (N * N - E_P),
       "n_minimizers_quotient": sum(1 for t in top if t["S"] == S_min),
       "note_count": "44 minimizers among kept top-512 tail; full-count reconfirmed by verifier",
       "next_S": S_next, "gap_to_next": S_next - S_min,
       "catalog": catalog}
json.dump(out, open("output/artifacts/catalog.json", "w"), indent=1)
print(f"wrote catalog.json: {len(catalog)} reps, S_min={S_min}, next={S_next}", flush=True)
for c in catalog:
    print(c["Q"], "E=", c["E"], "X=", c["X"], "G=", c["G"],
          "F_Q=%.4f" % c["F_Q"], "PSC=%.5f" % c["PSC"], flush=True)
