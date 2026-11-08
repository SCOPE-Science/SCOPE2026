---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

On event all edges sampled (complement exponentially small) convex hull perimeter replaces precisely each vertex incident boundary segments by the chord through closest incident edge samples, yielding exact defect F_α(x,y)=x+y−√(x²+y²−2xy cosα). Disjoint O(1/n) endpoint intervals show joint independent exponential gaps with rates λ_i=w_i/L_i by common avoidance probability (1−B/n)^n→e^(−B). Uniform exponential nearest-point bounds and exponential missing-edge failure give all fixed moments. Solving F_α(x,y)=z gives x_z(y)=z(y−z/2)/((1+cosα)y−z); splitting integration at √z yields P(F≤z)=((λ+μ)/(1+cosα))z+o(z). Vertices use disjoint limiting endpoint exponentials, so independent m-fold convolution gives factor 1/m!. For regular m-gon maximize ∏(w_(i−1)+w_i) under ∑w=1 via AM–GM, with equality linear recurrence w_i=w_(i−2); odd m uniform unique, even m positive alternating family. Independent geometric chord inversion and equality products checked; full limit follows analytic proof.

## originality

PASS

Best-knowledge PASS: Reitzner–Schütt–Werner boundary polytopes study missing volume and face counts; Prochno–Schütt–Sonnleitner–Werner study Hausdorff max error. Shared Poisson endpoint asymptotics do not imply a sum of nonlinear chord-perimeter shortcuts and this exact small-ball coefficient or parity of risk-optimal sampling. Related smooth-ellipse minimax and regular-polygon Gumbel results optimize different losses.

## value

PASS

Perimeter error is a natural geometric reconstruction loss, and its exceptionally accurate tail and optimal edge allocation answer a motivated design problem distinct from mean or Hausdorff accuracy. Odd/even nonunique optimum is a sharp structural phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
