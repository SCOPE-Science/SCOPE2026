---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

From row-stochastic P^2=J and PJ=J it follows JP=J, so P is doubly stochastic. A deterministic row leads to a uniform row at its target but that contradicts the target column sum, including the self-loop case. Thus all rows have support at least 2; in n<=3 every pair overlaps, giving Dobrushin delta(P)<1. Compactness of the exact-square kernel set yields a uniform max rho_n<1; successive Dobrushin contractions cover every arbitrary switching sequence, law and time. For n=4 forward/reverse two-bit shifts P,Q=P^T satisfy P^2=Q^2=J, but PQ is a nonuniform idempotent preserving a bit. Blending with J by epsilon preserves exact squares; (P_e Q_e)^m=J+(1-e)^(2m)(PQ-J) and corresponding odd products. Rows are supported equally on two states, giving exactly TV=(1-e)^t/2 and maximal relative error=(1-e)^t, including endpoints and both phases. Independent 120 rational checks reproduce these formulas; all-real proof is analytic.

## originality

PASS

Qualified PASS: general SIA/scrambling and square-zero centered operator products are known, but no inspected earlier theorem derives the sharp n=3/n=4 exact-square stochastic threshold plus the closed positive-perturbation rate. Reversibility-based dynamic mixing results are inapplicable to the nonreversible witness. Earlier stochastic-product theory gives tools, not the specific boundary and exact profile.

## value

PASS

Exact static mixing in two steps is a very strong and natural hypothesis. The theorem sharply determines the smallest dimension where arbitrary switching can defeat it and supplies explicit positive kernels with arbitrarily slow switched convergence, distinguishing homogeneous and inhomogeneous mixing. The complete all-time/epsilon quantitative boundary is substantive, not just a generic nilpotent example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
