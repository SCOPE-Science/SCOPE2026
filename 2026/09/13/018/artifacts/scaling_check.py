"""Reproducible scaling check for the single-cap concentration counterexample.

Discrete disjoint-tube model (exact closed form, no Monte Carlo):
  N parallel disjoint tubes, each meeting L grid balls; per-ball L^6 mass b=1.
  F = phi_T0 + delta * sum_{j>=1} phi_Tj,  delta^6 = 1/(N-1).
  Y = balls of T0  =>  M = L, W = N*L, mean multiplicity on Y = 1.
  LHS^6 = L ; global mass = L*(1+(N-1)*delta^6) = 2L ;
  RHS^6 = (M/W)*global = 2L/N ; ratio LHS/RHS = (N/2)^{1/6}.
With N ~ R^{3/2} (all parallel R^{-1/2}-tubes crossing B_R in R^{3+1}),
ratio ~ R^{1/4}, defeating C_eps R^eps for any eps < 1/4.

Run from the lane root:  python3 output/artifacts/scaling_check.py
Writes: output/artifacts/scaling_check_results.json
"""
import math
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "scaling_check_results.json")

rows = []
e = 4
while True:
    R = 2 ** e
    if R > 2 ** 20:
        break
    N = int(round(R ** 1.5))
    L = max(1, int(round(R ** 0.5)))
    e += 2
    if N < 2:
        continue
    delta = (N - 1) ** (-1.0 / 6.0)
    lhs6 = float(L)
    tot6 = float(L) * (1.0 + (N - 1) * delta ** 6)  # == 2L
    M, W = L, N * L
    rhs6 = (M / W) * tot6
    ratio = (lhs6 / rhs6) ** (1.0 / 6.0)
    closed = (N / 2.0) ** (1.0 / 6.0)
    assert abs(ratio - closed) / closed < 1e-9
    rows.append({"R": R, "N": N, "L": L, "ratio": ratio,
                 "R_pow_quarter": R ** 0.25,
                 "ratio_over_R_pow_eighth": ratio / R ** 0.125})

print(f"{'R':>8} {'N':>10} {'L':>5} {'ratio':>9} {'R^1/4':>9} {'ratio/R^1/8':>12}")
for r in rows:
    print(f"{r['R']:>8} {r['N']:>10} {r['L']:>5} "
          f"{r['ratio']:>9.3f} {r['R_pow_quarter']:>9.3f} "
          f"{r['ratio_over_R_pow_eighth']:>12.3f}")

xs = [math.log(r["R"]) for r in rows]
ys = [math.log(r["ratio"]) for r in rows]
n = len(xs)
mx, my = sum(xs) / n, sum(ys) / n
slope = (sum((x - mx) * (y - my) for x, y in zip(xs, ys))
         / sum((x - mx) ** 2 for x in xs))
print(f"\nlog-log slope = {slope:.4f} (theory 0.2500)")
mono = all(b["ratio_over_R_pow_eighth"] > a["ratio_over_R_pow_eighth"]
           for a, b in zip(rows, rows[1:]))
print(f"monotone growth of ratio/R^(1/8): {mono}")

with open(OUT, "w") as f:
    json.dump({"rows": rows, "loglog_slope": slope}, f, indent=2)
print(f"wrote {OUT}")
