---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification methodology

The proof obtains the associator and commutant constraints directly from the basis products. For even order \(n=2m\), the opposite-index coefficients combine into pair sums. The right nucleus requires not only constant pair sums, but invariance of the resulting polynomial under doubling exponents. Doubling permutes the even exponents exactly when \(m\) is odd. Otherwise the coefficient at exponent 2 forces the constant pair sum to vanish. Intersection with the parity-constant left nucleus then gives the claimed characteristic switch. The commutant test combines period dividing three with even support and implies the zero commutant.

The accompanying `verify.py` imposes the defining identities on generic coefficient vectors and computes their ranks by modular elimination. Its even-order portion tests \(n=2,4,\ldots,14\) over characteristics 2, 3 and 5 and checks the indicated basis and product assertions; the script's odd-order tests are supplementary comparisons, not within the theorem. Execute `python3 verify.py`; the expected last line is `ALL_NUCLEUS_CHECKS_OK`. The finite tests do not prove the all-field result; that follows from the coefficient proof in `RESULT.md`.
