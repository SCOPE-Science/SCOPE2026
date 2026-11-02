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

The exact rational checker `verification.py` is standalone and uses only Python's standard library. Running `python3 verification.py` checks the coefficient recurrences through depth eight with fixed leaf caps, the leading-configuration lower bound, the explicit finite-radius upper bound, and the exponential support-weight gap for combinatorially exhaustive small cases. The captured run is `verification_output.txt`.

All tests operate at finite radii. The proof for arbitrary radius and each fixed order is the explicit generating-function recurrence and support-set comparison in RESULT.md. The finite-tree limiting interpretation relies on standard critical Galton–Watson local convergence and is *not* a uniform radius/size approximation. No independent validation or outside certificate was performed.
