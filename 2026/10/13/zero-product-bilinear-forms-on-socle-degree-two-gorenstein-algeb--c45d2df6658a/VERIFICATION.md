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

Run `python3 verify.py` using Python 3 in the package directory; no third-party modules or data downloads are required. The script constructs the multiplication table on \(\mathbb F_p1\oplus\mathbb F_p^d\oplus\mathbb F_pz\) with dot-product multiplication, enumerates **all** zero-product pairs for \((p,d)=(2,2),(3,2),(2,3)\), performs modular Gaussian elimination, and checks the normal-form, symmetric, factorization, and invertible-matrix dimensions/counts. Expected last line: `VERIFY_OK`.

Finite tests verify only those three prime-field cases and do not establish the result for other finite fields or arbitrary fields. Generality and the sharp exception at \(q=2\) follow from the algebraic proof and determinant identity in RESULT.md. There has been no independent audit or independent validation.
