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

# Verification details

Run `python verify_extreme_phase.py` with Python 3 and `mpmath`. The program checks an exact residue expansion against independent quadrature of the reset-position distribution, the critical conditional odds for parameters on either side of the inversion, and the pole and active-fraction coefficient near the loss-of-stationarity threshold. Actual observed terminal marker: `ALL_CHECKS_PASS`.

These finite-precision checks corroborate formulas for selected parameters; the proofs of all-parameter thresholds and nonexistence of a stationary probability at infinite invariant holding mean use the analytic tail and Markov-renewal arguments in RESULT.md. The embedded code has no external source or project dependencies apart from the stated mathematics library.
