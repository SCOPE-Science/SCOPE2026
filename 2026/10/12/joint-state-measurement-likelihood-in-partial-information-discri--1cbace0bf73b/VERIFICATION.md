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

The analytic proof is primary. `artifacts/verify.py` uses exact rational arithmetic on the feasible commuting-qubit slice.

It verifies \(s(1/2,1/2)=1/2\), the mixed curvature \(\partial_{pq}\log s=4\), the calibration curvature \(-4\), and the restricted Hessian \(\begin{pmatrix}-4&4\\4&0\end{pmatrix}\) with determinant \(-16\) and trace \(-4\). A negative determinant proves one positive and one negative eigenvalue.

The executed package path returned:

`VERIFY_OK H=[[-4,4],[4,0]] determinant=-16 trace=-4 eigenvalues=-2+-2sqrt(5)`

This script does not establish any claim about the iteration's global landscape beyond the exact local curvature obstruction. The proof in `RESULT.md` supplies the all-symbolic argument.
