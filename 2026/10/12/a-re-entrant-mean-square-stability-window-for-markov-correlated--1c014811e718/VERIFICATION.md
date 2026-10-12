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

`verify.py` uses SymPy exact rational arithmetic to check the two update matrices; the six-dimensional second-moment transfer determinant; the three-dimensional one-delay moment resolvent; the renewal-mass cubic; the rational positive-definite Lyapunov certificate at independent delays; and selected root-sign brackets. It enumerates all \(2^t\) delay histories exactly through finite horizons and compares them with the transfer update, the first-zero renewal recurrence, and the last-zero decomposition.

Run: `python verify.py` after installing `requirements.txt` (SymPy 1.13 or newer). All checks passed in the supplied package. The infinite-horizon dichotomy is established by the renewal argument in `RESULT.md`, not by finite enumeration. No independent audit has been performed.
