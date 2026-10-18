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
# Reproduction

Run `python3 artifacts/verify.py` from the package root using Python 3; it has no external dependencies. The program checks exact polynomial identities for the three renewal-mass deficits, exact equality of the cumulative-coordinate form, its three terminal specializations, 8,854 closed-simplex rational-grid evaluations, and three exact sharpness witnesses with coefficients above \(2\). It prints `VERIFY_OK` upon success.

The argument for all real increment probabilities is the explicit decomposition into nonnegative polynomial terms in `RESULT.md`, not an extrapolation from the grid. The reduction of the global renewal minimum to the first three masses is also proved by the renewal recursion in that document. The coefficient-sharpness argument works for every real \(\alpha>2\) by taking sufficiently small positive \(t\); finite tests only illustrate it.

No independent audit or independent validation has been performed.
