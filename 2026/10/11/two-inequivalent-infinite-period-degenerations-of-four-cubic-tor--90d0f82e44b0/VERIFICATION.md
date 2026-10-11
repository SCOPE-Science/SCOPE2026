---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The exact torus invariance statement is the polynomial identity \(\dot F=(\lambda+\eta z)zF\), for \(F=(x^2+y^2-a^2)^2+z^2-1\). The proof in RESULT.md computes the globally defined angular flow with original physical time, integrates a negatively oriented return circuit, and proves the exact trigonometric partial-fraction identity. The minimal period is established by strictly monotone longitudinal winding for \(\lambda>\eta\).

Run `python3 checker.py` using Python 3.9 or later and the standard library. The script independently evaluates polynomial invariance at off-torus points, composite-Simpson period quadratures, the integrated holonomy exponent, and two limiting parameter scales. Successful output is `CHECK_OK`. Its finite evaluations are checks, not a substitute for the analytic equalities or uniform limiting claims.

The relative Floquet multiplier pertains to a one-dimensional section within the invariant torus. The ambient normal multiplier, robustness to arbitrary perturbations, and complete literature priority have not been established. Independent audit has not been performed.
