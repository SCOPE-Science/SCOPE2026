---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For real z≥1 the leaf diagonal is invertible; the characteristic Schur factor z−a−Σ b_i c_i x_i y_i/(z−d_i) is increasing and diverges. Its sign at 1 decides whether there is a real eigenvalue >1, equivalent to supercriticality by nonnegativity even when some directions vanish. For fixed r=1−xy, the least spoke cost is min(p,q)r: (1−x)+(1−y)≥1−xy, with equality by attenuating only a cheaper direction. The linear budget binds, and an exchange orders reductions by cost per unit threshold mass, with at most one partial reduction in a greedy solution, not necessarily in every tied optimum. In the reciprocal problem the strictly concave separable penalized objective gives the claimed clipped t and a unique optimum; at least one term must be unclipped at H<W, on the strictly decreasing part of the multiplier curve. Every t>0. For paired equal prices, inserting the feasible t=√(1−r) gives the upper factor two, and the identical-spoke family gives exactly 2/(1+√u); unequal prices (1,M) at u=1/4 give 2(M+1)/3. Independent exact tests (python3 /workspace/reproduce_reviews.py 3) enumerate directed budget vertices and certify reciprocal points on two heterogeneous examples, including clipping (H=21/64, t=(1/4,1/8,1), costs 123/64 and 19/4). The frozen checker uses exact fractions for determinants and the directional cost, but floating bisection/tolerances for reciprocal examples, not exact rational certificates for that part; the proof and exact arithmetic examples settle those claims. This is an initial spectral threshold, not a final-size or extinction theorem.

## originality

PASS

The supported distinct result is the combined sharp classification of the two positive-linear-cost control classes and their price on heterogeneous weighted stars. Schur complements, spectral resource allocation, fractional knapsack and box-constrained quadratic optima are not claimed as new. The closest exact reciprocal-mixing and star-dose results have different objectives and controls and do not give the price comparison.

## value

PASS

The comparison answers a natural modeling question about changing the admissible controls under the same cost and threshold, not just evaluating a particular star. It determines when a greedy optimum can concentrate all intervention on a few directions, why reciprocity necessarily leaves every spoke with positive transmission factors, and how paired cost symmetry changes the sharp worst-case loss from unbounded to two. These are testable benchmarks for the specified matrix model, not claims about empirical intervention outcomes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
