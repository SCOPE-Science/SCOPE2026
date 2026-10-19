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

# Reproducible mathematical checks

Run `python verify.py` with `sympy>=1.12` installed. The program checks the original pairwise vector-field derivatives at the critical disease-free point, quasi-static and true center-graph coefficients through quadratic order, reduced prevalence coefficients through cubic order, logarithmic coefficients and their strictly positive rational gap. It checks the exact degree-three and degree-four examples and the polynomial sign threshold.

The proof in `RESULT.md` is necessary for the asserted asymptotic limit: finite symbolic series and numerical trajectories alone do not establish infinite-time convergence. The analytic argument uses the standard smooth center-manifold and implicit-function theorems, exponential transverse contraction, and integrability of the reciprocal remainder. Numerical integration at degrees three, four and six was also carried out as a consistency check but does not constitute the proof.

The theorem applies locally to strictly positive prevalence in the deterministic pair-closed system and is not a statement about stochastic extinction on a finite contact graph. Independent scientific validation is not included.
