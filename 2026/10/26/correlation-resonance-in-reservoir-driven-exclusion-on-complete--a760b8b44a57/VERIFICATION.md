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

# Verification protocol

Execute `python verify_reservoir_bipartite.py` with Python 3. The only dependency is the standard library. An independently built finite-state occupancy-count generator for the injection, extraction, and exchange dynamics is solved by rational Gauss–Jordan elimination (not by reusing the stationary covariance derivation). Twenty-seven parameterized stationary systems provide 135 exact mean/covariance comparisons. Twenty-seven optimizer perturbation inequalities and six asymptotic checks give 168 checks overall.

Recorded execution: `PASS: 168 independent exact-rational, optimization, and asymptotic checks`.

These finite computations do not establish all-size optimality. That follows from the strict negativity of the derivative of the explicit scalar critical-point function in RESULT.md. The thermodynamic coefficient follows from a rational large-size limit. Publication priority remains subject to future independent literature assessment.
