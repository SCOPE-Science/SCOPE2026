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
The mathematical proof is given in RESULT.md. The package contains `verify.py`, a standalone standard-library script. The exhaustive enumeration covers the opposite-arrow two-cycle quiver truncated at lengths two and three over the prime fields of orders two and three and checks each commuting-idempotent pair against the full-unit centralizer index. The same runs verify total pair and singleton counts. A separate three-element-chain incidence algebra is enumerated at both field orders, and Potts sum and subset forms are compared.

Run `python3 verify.py` and require `COMMUTING_IDEMPOTENT_POTTS_OK`. Exhaustive finite tests do not establish the all-parameter theorem; the symbolic proof handles general algebras, characteristics, and tuple arities. Source-comparison limitations are stated in the review. No independent audit has been performed.
