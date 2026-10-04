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

The proof is analytic. The exact determinant is a finite trigonometric polynomial, so its Taylor remainder after division by \(k^3\) is uniform in the Bloch phases on the compact torus.

Critical checks reconstructed from the determinant:

1. The cubic coefficient is
\[
abc-2(a+b+c)-2\bigl(a\cos(\theta_2-\theta_1)+b\cos\theta_2+c\cos\theta_1\bigr),
\]
which is the negative of the coefficient displayed in Eq. (22) of arXiv:2409.03538v1 and therefore has the same zero set.

2. At the upper critical scale, the fifth-order coefficient at \((\theta_1,\theta_2)=(0,0)\) reduces to
\[
\frac{e_1-12e_3}{12e_3^2}>0
\]
under \(XY+XZ+YZ=1/4\), where \(X=a^{-1}\), \(Y=b^{-1}\), \(Z=c^{-1}\). Positivity follows from \((X+Y+Z)(XY+XZ+YZ)\ge9XYZ\).

3. At the lower reciprocal-nontriangle critical scale, after taking \(a\) as the shortest edge and using \(bc=4\), the fifth-order coefficient at \((\pi,\pi)\) is
\[
\frac{a}{3}\bigl(b^2+c^2+3a(b+c)\bigr)>0.
\]

4. At the lower reciprocal-triangle critical scale, with \(e_1=X+Y+Z\), \(e_3=XYZ\), the fifth-order coefficient at a minimizing phase is
\[
\frac{(e_1-6e_3)(e_1^2+1)}{6e_3^2}>0.
\]
Writing \(X=p+q\), \(Y=q+r\), \(Z=r+p\) and using the critical relation \(4(pq+pr+qr)=1\) yields \(e_1-6e_3=(p+q+r)/2+6pqr>0\).

5. For the equilateral shape, the formulas give \(s_-=\sqrt3\) and \(s_+=2\sqrt3\), matching the primary source's independently derived special case.

`verify.py` evaluates the exact determinant for representative shapes on both sides of the critical scales and checks the algebraic scale and width identities. Its output is corroborative; finite sampling is not used to prove the infinite-dimensional spectral statement.
