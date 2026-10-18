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

# Verification

Execute the included standalone Python file with `python check.py`; it requires only the standard library. On the reviewed program, the observed final line was: `PASS: 58566 independently implemented moment, coupling, rank and simulation checks.` Exact-Fraction checks cover the four atom probabilities, the second moment, admissible couplings, positive-semidefinite covariance comparisons and all ray-rank failure probabilities for small row counts. The script independently checks the constants for precision-two binary endpoints and compares large row samples to the derived population Gram.

The algebraic proof covers every admissible coupling and every row count in the stated scope. Simulations or numerical tests do not establish an almost-sure limit or replace exact rank counting. The sample-size limit assumes independent rows with a fixed coupling. No independently performed audit or external formal certification is claimed.
