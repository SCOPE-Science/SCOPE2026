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

Run `python3 CHECK.py` with a standard Python 3 installation. It checks every coefficient by the original double character sum and independently evaluates the quadratic-fiber expression for prime fields of order 3, 5, 7 and 11 and quadratic extension fields of order 9 and 25. It checks the predicted norm and fiber cardinality histogram with floating-point tolerance \(2\cdot10^{-8}\). The checker prints `CHECK_OK cubic_fold_prime_and_quadratic_extension_fields` on success.

The complete proof uses finite-field character orthogonality, square-root multiplicity, trace-fiber counts, a geometric cosine sum and the sharp convolution sign choice. The tests do not establish the theorem for arbitrarily large fields; numerical cancellation is not exact symbolic arithmetic. No independent audit has been performed.
