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

For an \(m\)-dimensional ball \(c+rB_2^m\), put
\[
x-c=se,
\qquad
0\le s<r.
\]
The boundary equation in direction \(u\) is
\[
\rho^2+2s(e\cdot u)\rho+s^2-r^2=0.
\]
Its positive root is
\[
\rho
=
-s(e\cdot u)
+
\sqrt{r^2-s^2+s^2(e\cdot u)^2}.
\]
The packaged symbolic check substitutes this root back into the quadratic exactly.

Spherical symmetry cancels the first term. The remaining integrand is
\[
q_s(u)
=
\sqrt{r^2-s^2\bigl(1-(e\cdot u)^2\bigr)}.
\]
If
\[
0\le s_1<s_2<r,
\]
then
\[
q_{s_2}(u)\le q_{s_1}(u)
\]
for every \(u\), with strict inequality whenever
\[
|e\cdot u|<1.
\]
For \(m\ge2\), the exceptional polar set has spherical measure zero, giving strict integral monotonicity.

For an affine hyperplane \(H=c_H+L\) with \(c_H\perp L\),
\[
B_R^d\cap H
=
c_H+\sqrt{R^2-\lVert c_H\rVert^2}\,B_L.
\]
For every \(x=c_H+v\in H\),
\[
\lVert x\rVert^2
=
\lVert c_H\rVert^2+\lVert v\rVert^2,
\]
so section eccentricity and ambient eccentricity have exactly the same ordering.

The checker additionally performs numerical quadrature only as a regression test. Those finite calculations are not used to establish the universal claim.

In dimension \(1\), the radial integral is
\[
(r-s)+(r+s)=2r,
\]
so strict eccentricity monotonicity fails. This is why the affine-section theorem is stated for ambient dimension \(d\ge3\).
