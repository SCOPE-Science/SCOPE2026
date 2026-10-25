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

# Verification of the local containment law

The analytical proof in RESULT.md establishes the theorem under the stated assumptions. The included `verify_boundary_absorption.py` requires Python 3, NumPy and SciPy. Execute `python verify_boundary_absorption.py` in the directory containing that file. The five diagnostics independently compare the exact semicircle-anchor integral with the known three-point circular dilogarithm, test the predicted fixed-sample logarithmic coefficients, incorporate exact ellipse arclength and curvature normalization, verify nonuniform circular density effects, and compare the integral to direct randomized polygon containment using oriented edge halfplanes. All checks passed on the packaged program prior to delivery.

These finite tests cannot establish an asymptotic theorem or historical priority. The proof's critical analytic ingredients are the unique-halfcircle-anchor identity, a local normal-chord expansion, the logarithmic integral on the outgoing boundary arc and the integrability of the returning arc for \(n\ge3\). The exact circular three-point identity is used solely as a known benchmark.
