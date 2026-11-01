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

# Verification

Analytic proof: `RESULT.md` provides the full positive-equilibrium reduction, establishes exact equivalence with the original four-dimensional system, proves strict global monotonicity of the parameter curve, and checks both endpoint cases. In particular, the high-bias patch-survival threshold is determined by the true maximal permitted asymmetry, not by extrapolating numerical observations.

Reproducibility: run `python3 check.py` with standard Python 3. The complete expected stdout is in `check_output.txt`. This script exercises 72 explicitly generated positive equilibrium states, comparing all four original ODE residuals to numerical tolerance, and checks monotonic samples and the onset expansion. These are finite tests. All-parameter claims, infinite-bias limits, and the absence of hidden equilibria are analytic results, not computational certificates.

The cross-source priority comparison is limited by broad possible results on nonlinear graph equilibria and a contextual source for which the full text was unavailable. Independent audit has not been conducted.
