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

# Verification of the mathematical claim

The independent `check.py` program computes proper-colouring configurations, constructs the coordinate Fourier evaluation matrix, and compares the directly averaged complex Gram matrix against the exact conditional block formula. It verifies the predicted eigenvalue multiset, nullities, and sharp extrema on six cases, along with exact clique-core eigenvalue formulas and strict-conditioning and asymptotic numerics for 228 assertion groups. Execute with `python3 check.py` in an environment with NumPy. All checks passed during preparation of this package.

The theorem for all finite graphs and all admissible parameters is proved analytically in RESULT.md. Numerical checks are finite corroborations only; they neither exhaust infinite families nor independently validate the analytic proof. No independent mathematical audit has been performed. The source comparisons remain bounded; an earlier equivalent theorem in broader Potts-covariance literature is an unresolved possibility.
