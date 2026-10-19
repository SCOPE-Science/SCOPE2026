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

Run `python3 transvection_checker.py` in Python 3. The checker enumerates genuine rank-one square-zero matrices, forms the products of two corresponding transvections, and distinguishes conjugacy types via traces and ranks of the shifted product and its square. Output ends in `ALL_EXACT_CHECKS_PASSED 9`. Exhaustive checks are over the prime fields with dimension-field pairs `(2,2),(2,3),(2,5),(3,2),(3,3),(3,5),(4,2),(4,3),(5,2)`; for six of these all ordered pairs were independently counted. The proof itself supplies the uniform arbitrary-prime-power argument. The finite runs do not constitute an infinite-field or all-dimension exhaustive certificate.
