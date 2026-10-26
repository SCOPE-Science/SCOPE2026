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

The proof of the geometry and cycle-spanning statement is in RESULT.md. The standalone `verify.py` reproduces the Hermitian point and adjacency computations over \(\mathbb F_4\) without external software. Execute `python verify.py` using Python 3. It checks \(165\) distinct normalized isotropic points, valency \(36\), the common-neighbor parameters \((\lambda,\mu)=(3,9)\), and Frobenius traces. The polynomial identity \(A^2=27I-6A+9J\) determines the exact spectrum, and the geometric argument identifies it with the intersection matrix. The finite calculation is exhaustive for this finite polar space; it is not used in place of the geometric intersection or adjunction proof. Independent auditing of the result has not been performed.
