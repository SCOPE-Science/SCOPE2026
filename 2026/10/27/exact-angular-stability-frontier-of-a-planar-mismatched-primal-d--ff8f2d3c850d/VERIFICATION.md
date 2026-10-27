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
# Verification record

The main result is established by the exact characteristic polynomial and degree-two Schur stability argument in `RESULT.md`. The reproducible `verify.py` checks the complex trace and determinant, the symbolic Schur margin and positivity identity, exact factorizations of the transition endpoints, and the monotonicity derivative. It independently constructs the real four-dimensional iteration for multiple positive step sizes and 37 angles per step and checks the spectral-radius classification and direct recurrence agreement; the test suite reports the number of successful checks when executed.

Run `python verify.py` after installing the packages specified in `requirements.txt`. The program uses fixed deterministic test inputs and contains no external network operations. Finite tests do not certify the infinite-parameter theorem; the analytic proof supplies that justification.

Limitations: this work has not undergone independent audit or validation; its conclusions do not extend automatically to unequal primal/dual steps, alternate extrapolation, nonlinear proximals, arbitrary surrogate operators, finite precision, or nonzero forcing.
