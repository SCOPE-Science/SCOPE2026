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

The bundled `verify_crossratio_divisor.py` performs exact symbolic checks with no floating-point arithmetic.

It reconstructs the four-collinear determinant
\[
F=
\det
\begin{pmatrix}
v_1z_1&v_2z_2&v_3z_3&v_4z_4\\
v_1y_1&v_2y_2&v_3y_3&v_4y_4\\
z_1&z_2&z_3&z_4\\
y_1&y_2&y_3&y_4
\end{pmatrix},
\]
checks the bracket expansion, substitutes \(z_i=t_i y_i\), and verifies that the quotient by \(y_1y_2y_3y_4\) is exactly the stated cross-ratio numerator.

It then substitutes the symbolic projective orbit
\[
[z_i:y_i]=[av_i+b:cv_i+d]
\]
and verifies identically that \(F=0\).

For the affine quadratic equation \(D\), it computes the Hessian \(H\), verifies the common-shift kernel vector, and proves symbolically that every principal \(3\times3\) minor is
\[
2\prod_{1\le i<j\le4}(v_j-v_i).
\]
It also verifies \(D=\tfrac12t^THt\) and \(\nabla D=Ht\). A rational specialization \((v_1,v_2,v_3,v_4)=(0,1,2,3)\) checks rank three, the one-dimensional common-shift kernel, diagonal singular points, and a smooth non-diagonal orbit point.

A successful replay prints `VERIFY_OK`.

The verifier does not by itself prove the global chart argument, irreducibility, normality, or the use of the published vanishing-ideal theorem; those are supplied in `RESULT.md`.
