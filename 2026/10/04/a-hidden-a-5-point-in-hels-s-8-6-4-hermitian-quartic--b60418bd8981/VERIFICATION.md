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

The exact verifier in `artifacts/verify.py` reconstructs the printed Hermitian matrix and its determinant. It checks the affine gradient Gröbner basis, the infinity factorization, all eight singular points, and matrix rank \(2\) at each point. It computes local Hessian determinants for the seven \(A_1\) points.

At \(D=[0:1:0:0]\), it makes the stated local coordinate change, verifies the nondegenerate two-variable quadratic block, solves the formal critical section through the order needed for the first split term, and checks that the one-variable remainder begins with \(w^6/17\). This is the certificate used for the \(A_5\) classification.

The verifier also checks the characteristic polynomials at all six real rank-two points and the polynomial restrictions defining the three singular trisecant lines. It uses exact symbolic arithmetic in SymPy; no floating-point decision is used for the singularity classification. Running `python artifacts/verify.py` must print `VERIFY_OK`.

The literature comparison is not mechanically certified by the script. It is based on inspection of arXiv:2007.01121 and the recorded database searches. The claim is restricted to the printed matrix and does not classify alternative representations or deformations.
