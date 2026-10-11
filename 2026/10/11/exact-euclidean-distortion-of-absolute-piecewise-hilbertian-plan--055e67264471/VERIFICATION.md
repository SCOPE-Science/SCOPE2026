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

The verification is analytic. For an arbitrary positive-definite quadratic pullback, averaging over the four coordinate sign changes preserves the lower and upper norm-comparison inequalities and removes every off-diagonal term. Thus the global Banach--Mazur optimization reduces to diagonal forms.

For a diagonal pullback, the ratio of squared norms is the Rayleigh quotient of a \(2\times2\) symmetric matrix with nonnegative off-diagonal entry. Its quadrant maximum is the larger eigenvalue and its quadrant minimum is the smaller diagonal endpoint. After scale normalization, the squared distortion is
\[
D_r(z)=\frac{z+1+\sqrt{(z-1)^2+4r^2z}}2,\qquad z\ge1.
\]
The claimed lower bound follows because either \(2r-(z-1)\le0\), or both sides may be squared and
\[
(z-1)^2+4r^2z-\bigl(2r-(z-1)\bigr)^2=4r(r+1)(z-1)\ge0.
\]
The pullback \(a x^2+c y^2\) attains equality, since weighted arithmetic--geometric mean bounds its norm ratio between \(1\) and \(1+b/\sqrt{ac}\).

Boundary checks: \(b=0\) gives a Hilbert norm and distance \(1\); \(b=\sqrt{ac}\) gives a weighted \(\ell_1^2\) norm and squared distance \(2\). The two-dimensional Cesàro parameter choice reproduces the known value \(1+1/\sqrt5\).

No computation is required for the proof. No independent audit has been performed.
