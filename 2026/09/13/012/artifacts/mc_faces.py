"""Monte Carlo check of the periodic-layer cascade lemma and failure exponents.
Layer: 4D periodic grid (area A), below-layer fully infected, above-layer Bernoulli(p) static.
Distinct : cell needs >=1 infected among 8 in-layer neighbours (above ignored, same axis).
Standard: cell needs total >=2 among 10 (below gives 1, so in-layer + above >= 1).
Lemma predicts P(fail) = (1-p)^A [distinct] vs (1-p)^{2A} [standard];
i.e. -log P(fail)/(pA) -> 1 vs 2.
"""
import numpy as np, json, math

rng = np.random.default_rng(0)

def wilson(k, n, z=1.96):
    if n == 0:
        return 0.0, 1.0
    ph = k / n
    d = 1 + z * z / n
    c = ph + z * z / (2 * n)
    h = z * math.sqrt(ph * (1 - ph) / n + z * z / (4 * n * n))
    return max(0.0, (c - h) / d), min(1.0, (c + h) / d)

def run(shape, p, rule, T):
    cur = rng.random((T,) + tuple(shape)) < p
    above = rng.random((T,) + tuple(shape)) < p
    axes = list(range(1, len(shape) + 1))
    for _ in range(4 * sum(shape) + 4):
        cnt = np.zeros_like(cur, dtype=np.int16)
        for ax in axes:
            cnt += np.roll(cur, 1, axis=ax).astype(np.int16) + np.roll(cur, -1, axis=ax).astype(np.int16)
        if rule == "distinct":
            new = cur | (cnt >= 1)
        else:
            new = cur | ((cnt + above.astype(np.int16)) >= 1)
        if (new == cur).all():
            break
        cur = new
        if cur.all():
            break
    full = cur.reshape(T, -1).all(axis=1)
    pf = 1.0 - full.mean()
    lo, hi = wilson(int((~full).sum()), T)
    return pf, lo, hi

configs = [
    ((2, 2, 2, 2), 0.06, "distinct", 3000),
    ((2, 2, 2, 2), 0.03, "standard", 3000),
    ((3, 3, 3, 3), 0.03, "distinct", 2000),
    ((3, 3, 3, 3), 0.015, "standard", 2000),
    ((4, 4, 4, 4), 0.015, "distinct", 800),
    ((4, 4, 4, 4), 0.0075, "standard", 800),
]
res = []
for shape, p, rule, T in configs:
    A = int(np.prod(shape))
    pf, lo, hi = run(shape, p, rule, T)
    pred = (1 - p) ** A if rule == "distinct" else (1 - p) ** (2 * A)
    expo = (-math.log(pf) / (p * A)) if pf > 0 else float("inf")
    res.append({"shape": shape, "A": A, "p": p, "rule": rule, "T": T,
                "Pfail_mc": pf, "wilson": [lo, hi], "Pfail_predicted": pred,
                "exponent_ratio": expo})
    print(f"{rule:9s} A={A:4d} p={p:.4f} Pfail_mc={pf:.4f} [{lo:.4f},{hi:.4f}] "
          f"pred={pred:.4f} -logP/(pA)={expo:.3f}")

with open("output/artifacts/results_faces.json", "w") as f:
    json.dump(res, f, indent=2)
