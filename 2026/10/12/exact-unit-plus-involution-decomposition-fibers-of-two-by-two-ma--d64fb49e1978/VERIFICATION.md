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

# Reproducibility and verification

Run `python3 verify.py` using only Python 3 standard library. The program represents prime fields arithmetically and represents \(\mathbb F_9\) as \(\mathbb F_3[\theta]/(\theta^2+1)\). It directly enumerates every \(2\times2\) matrix and every involution in each field, evaluates whether their difference is a unit, and compares that fiber size with the asserted trace–determinant formula. It separately verifies the number of all involutions, the second-minimum extremizer characterization, and the number of extremizers. Expected terminal line: `VERIFY_OK`.

The test fields have cardinalities \(3,5,7,11,9\) and together contain \(24,309\) prescribed matrices. The mathematical proof does not use exhaustive testing to infer an infinite-field-family theorem. Characteristic two and larger matrix orders are outside the claim. The historical novelty comparison is not an independent assessment.
