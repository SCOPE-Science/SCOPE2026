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

# Verification and reproducibility

The package includes standalone \(\texttt{verify.py}\), using only the Python 3 standard library. It builds each quadratic extension directly as a polynomial quotient over its prime field; tests that each chosen quotient really is a field; enumerates every input in the extension; computes the target by Frobenius trace and norm; verifies zero fibers, prescribed variance, cubic-residue-class constancy, and the asserted exact image size. For \(q=4\), it also tests the precise two nonzero represented multiplicities.

Exact enumeration covered ten base-field orders \(2,3,4,5,7,8,9,11,13,16\), totaling 794 extension-field elements. Successful execution yielded \(\texttt{VERIFY_OK cases=10 inputs=794}\). These results support the algebraic proof for these finite cases only. The general proof uses character orthogonality and classical Gauss–Jacobi identities, not the enumeration.

No independent mathematical audit or independent validation has been performed.
