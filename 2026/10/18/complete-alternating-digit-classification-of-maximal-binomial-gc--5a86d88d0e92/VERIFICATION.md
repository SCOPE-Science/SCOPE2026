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

# Exact finite checks

Execute `python verify.py` using only the Python standard library. This directly enumerates selected binomial coefficients through base-prime borrow counts, cross-checks an independent Legendre-factorial valuation expression, and verifies the two-unit opposite-parity criterion. Expected result: `VERIFY_OK prime_fields 8 rows 1372 selected_indices 174040 independent_legendre_checks 3515`. No finite computation certifies the quantified proof.
