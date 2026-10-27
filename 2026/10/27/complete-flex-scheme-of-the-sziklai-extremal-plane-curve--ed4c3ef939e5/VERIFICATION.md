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

# Reproducibility
Execute `python3 verify.py` alongside this file. The program uses only the standard library; it constructs a sparse ternary homogeneous polynomial, computes its first and second derivatives, forms the six-term determinant, and verifies exact polynomial agreement in the prime fields. It checks \(q=3,5,7,9,11,13,25,27\) and prints `VERIFY_OK` on success.

The exact general proof in `RESULT.md` establishes the identity and divisor for every odd prime power; the eight sample evaluations are only redundant controls. The tangent-line intersection identities, field-of-definition argument, and absence of further flexes are verified analytically. Finite sampling is not claimed to prove these universal assertions. The relevant 2012 historical article was not available in full text; independent review remains unperformed.
