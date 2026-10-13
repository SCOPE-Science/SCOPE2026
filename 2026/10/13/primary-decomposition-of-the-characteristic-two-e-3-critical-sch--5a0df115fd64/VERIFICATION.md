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

The exact replay is `verify.py`, with recorded output in `verification_output.txt`. It uses only Python's standard library and performs arithmetic over \(\mathbf F_2\).

The replay checks that the fourth partial derivative and \(e_3\) reduce to zero modulo the first three partial derivatives, constructs the four stated primary ideals, verifies containment of the gradient ideal in each one, computes their successive intersections by elimination, and confirms equality with the original gradient ideal. The output terminates with `VERIFY_OK`.

The checker certifies the finite ideal identities used in the proof. It does not prove the cited general theorems of Xie; those are invoked only in the stated specialization to deduce height, complete-intersection degree, and the structural interpretation of the four generic multiplicities. No independent audit has been performed.
