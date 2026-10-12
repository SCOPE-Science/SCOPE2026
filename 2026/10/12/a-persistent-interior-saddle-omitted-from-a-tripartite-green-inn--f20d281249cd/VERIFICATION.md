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

At the explicit parameter vector,
\[
g_x=2yz-\frac12,\qquad
g_y=2x+z-\frac32,\qquad
g_z=2x+y-\frac32,
\]
and all three vanish at \((1/2,1/2,1/2)\).

The bracket derivative is
\[
M=\begin{pmatrix}0&1&1\\2&0&1\\2&1&0\end{pmatrix},
\qquad \det M=4.
\]
The full Jacobian is \(J=M/4\), with characteristic polynomial
\[
\lambda^3-\frac{5}{16}\lambda-\frac{1}{16}
=
\left(\lambda+\frac14\right)
\left(\lambda^2-\frac14\lambda-\frac14\right),
\]
and eigenvalues
\[
-\frac14,\qquad
\frac{1-\sqrt{17}}8,\qquad
\frac{1+\sqrt{17}}8.
\]

The bundled `verification/verify.py` checks these identities with rational arithmetic and the Python standard library. Persistence follows analytically from the implicit-function theorem. No claim is made about the source's calibration or a global basin boundary.
