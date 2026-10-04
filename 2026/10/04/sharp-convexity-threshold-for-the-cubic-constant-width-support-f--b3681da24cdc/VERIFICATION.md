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

The final claim was re-derived symbolically from the curvature-radius operator.

For \(F(x,y,z)=xyz\), the Euclidean Hessian is
\[
D^2F=
\begin{pmatrix}
0&z&y\\
z&0&x\\
y&x&0
\end{pmatrix}.
\]
On \(u^\perp\), the perturbation operator is
\[
A=(D^2F)|_{u^\perp}-2xyz\,I.
\]
Its exact tangent trace and determinant are
\[
\operatorname{tr}A=-10xyz
\]
and
\[
\det A=16x^2y^2z^2+4(x^2y^2+y^2z^2+z^2x^2)-1.
\]
The resulting eigenvalues and the simplex reduction in the proof yield
\[
\sup_{u\in S^2}\|A(u)\|_{\mathrm{op}}=\frac{4\sqrt{6}}{9}.
\]

At \(u=(2,1,1)/\sqrt{6}\) and \(v=(0,1,-1)/\sqrt{2}\), direct substitution gives
\[
A(u)v=-\frac{4\sqrt{6}}{9}v,
\]
so the threshold cannot be improved.

The proof also checks boundary cases, radical-zero cases, and all interior stationary points. No numerical sampling is used to infer the global maximum.

The scientific limitation is that this verification concerns only the cubic family \(h_{\alpha,\beta}\) in three dimensions.
