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

The symbolic proof in `RESULT.md` establishes the universal classification using exact prime-reciprocal bounds, integrality of the denominator logarithmic derivative, and elementary arithmetic-derivative identities. The standalone Python 3 checker `checks/arithmetic_derivative_check.py` uses exact rational arithmetic and integer factorization up to 120000 to corroborate supporting identities and local case distinctions.

Execution command: `python3 checks/arithmetic_derivative_check.py`

Observed result: `VERIFY_OK squarefree_positive_surpluses 558 four-prime_positive_surpluses 557 search_limit 120000`.

The finite computation is not an infinite proof and does not certify primality of any large value of \(q^q-30\). Existence and infinitude of the prime-value family remain unproved here. The 2026 sufficient construction is credited and is not claimed as original.
