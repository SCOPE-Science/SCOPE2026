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

For a unit-base cone of height \(t\), the proof uses
\[
m=\pi+t-\arctan t,
\qquad
s=1+\sqrt{1+t^2},
\qquad
q^2=m^2-4s.
\]
With
\[
x=\frac{t}{\sqrt{1+t^2}},
\]
one has \(m'=x^2\), \(s'=x\), and
\[
q'=\frac{mx^2-2x}{q}.
\]
Writing \(A=m^3-6ms+8t\) and \(B=q^3\), exact expansion gives
\[
A'=\frac32\bigl((mx)^2+(qx)^2\bigr)-6mx+8,
\qquad
B'=3qx(mx-2).
\]
Completing squares yields
\[
A'\pm B'
=
2+\frac32\bigl(x(m\pm q)-2\bigr)^2>0.
\]
This is the universal monotonicity certificate; no finite sampling is used to infer it.

The packaged checker then certifies the endpoint signs using rational interval arithmetic. It encloses \(\pi\) between \(333/106\) and \(355/113\), encloses square roots by exact integer-square comparisons, and propagates all four sign computations with rational endpoints. The certified signs are
\[
\Psi_+(1)<0<\Psi_+(\sqrt3),
\]
\[
\Psi_-\!\left(\tan\frac{2\pi}{5}\right)<0<
\Psi_-\!\left(\tan\frac{5\pi}{12}\right).
\]
Together with strict monotonicity, these certify existence and uniqueness of the two transitions.

Ordinary bisection is used only to print the supplemental decimal approximations of the unique zeros. It is not part of the infinite proof.

Limits: the verification concerns the right circular cone family and the classical three-dimensional Steiner polynomial only.
