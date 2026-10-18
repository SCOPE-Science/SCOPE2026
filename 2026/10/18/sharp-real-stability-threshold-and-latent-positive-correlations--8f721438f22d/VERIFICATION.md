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

The accompanying `verify.py` constructs the full three-bit generator from the process definition and tests the explicit rational stationary mass vector against all exact balance equations. It verifies total probability one, derives each of the three Rayleigh differences and their common discriminant, and checks both signs of the field-induced covariance. In a separate 16-state calculation it solves the stationary four-site chains with two rational input ratios and checks their first-three-site marginals.

The arbitrary-parameter and arbitrary-chain conclusions rest on the algebraic proof in `RESULT.md`, not on a finite enumeration. Python with SymPy is sufficient to reproduce the calculations. No independent audit or independent mathematical validation is claimed.
