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

The proof is field-uniform. For \(d\ge3\), the multiplication tensor on \(\mathfrak m/\mathfrak m^2\) forces every automorphism to have monomial linear part. On a fixed coordinate branch, the annihilator of any valuation-one element of \(k[t]/(t^d)\) is exactly \(k t^{d-1}\), which forces all off-branch terms into the top degree. These two observations give the normal form and its converse directly.

The included `verify.py` exhaustively enumerates generator images over prime fields in six small cases. It checks the defining zero-product relations, invertibility on the cotangent space, the predicted normal-form restriction for \(d\ge3\), and the exact automorphism count. The saved `verify_output.txt` ends with `CHECK_OK`.

The finite computations do not prove the theorem for arbitrary fields or arbitrary prime powers; the algebraic argument in `RESULT.md` does. No independent audit has been performed.
