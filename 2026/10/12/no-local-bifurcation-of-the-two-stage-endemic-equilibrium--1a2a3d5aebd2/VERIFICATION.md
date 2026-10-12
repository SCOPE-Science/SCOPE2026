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

The bundled `verify.py` uses only Python 3 standard-library functionality and exact integer multivariate-polynomial arithmetic. It reconstructs the four-by-four endemic Jacobian symbolically from the primitive positive parameters, computes the determinant of \(zI-J^*\) by all 24 permutations, and confirms the displayed characteristic-polynomial identity.

It then extracts \(A_1,A_2,A_3,A_4\) and forms
\[
\Delta_2=A_1A_2-A_3,
\qquad
\Delta_3=A_1A_2A_3-A_3^2-A_1^2A_4.
\]
Every expanded coefficient is checked to be a positive integer. The reviewed run reports 5, 13, 23, 20, 36, and 331 monomials respectively for \(A_1,A_2,A_3,A_4,\Delta_2,\Delta_3\); the minimum coefficient is 1 in every case. The third determinant has maximum coefficient 58.

These checks establish a finite exact polynomial identity and coefficient-sign certificate. They do not constitute an independent audit and do not prove global asymptotic stability, behavior for three or more infectious stages, or any statement for models with additional transmission routes.
