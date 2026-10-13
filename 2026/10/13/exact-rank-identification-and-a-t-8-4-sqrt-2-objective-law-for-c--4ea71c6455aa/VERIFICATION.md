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

The primary source formulas used here are the quadratic-growth radius, efficient-rank update, thresholding map, ERSO-FW update, and the two allowed step policies. On the stated centered quadratic, the proof reduces them to one exact scalar coordinate.

`artifacts/verify_centered_erso.py` was executed from the packaged artifact path and returned `VERIFY_OK`. It checks the specialized general burn-in constants, the first two source-simple-step iterates, the exact rank-two threshold at the third oracle call, the full-rank oracle recurrence, forward invariance of the rank-two region, finite-horizon gamma-product identities, and the exact-line-search root.

The checker is supporting evidence. The all-iteration rank statement follows analytically from the invariant inequality, and the asymptotic exponent follows from the proved product formula and the standard gamma-ratio asymptotic.
