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

The proof was checked in four independent steps.

1. **Forward formulas.** In chord coordinates \(0<u<v<L\), the normalized derivative magnitudes are
\[
x=\frac1u-\frac1v=\frac{v-u}{uv},
\qquad
y=\frac1{L-v}-\frac1{L-u}
=\frac{v-u}{(L-u)(L-v)}.
\]
These are the translated form of the published signed-coordinate formulas.

2. **Existence for arbitrary positive data.** With
\[
m=\frac{u+v}{2},
\qquad
r=\frac{v-u}{2},
\]
the data equations imply
\[
m=\sqrt{r^2+\frac{2r}{x}},
\qquad
L-m=\sqrt{r^2+\frac{2r}{y}}.
\]
For any \(x,y>0\), the sum of the two right-hand sides is strictly increasing from \(0\) to infinity as \(r\) runs from \(0\) to infinity, so it equals \(L\) once and only once. Each square root is larger than \(r\), which proves \(0<u<v<L\).

3. **Uniqueness.** The scalar root \(r\) is unique, after which \(m\), \(u\), and \(v\) are uniquely determined. This proves bijectivity without invoking the prior uniqueness theorem.

4. **Jacobian.** Direct differentiation simplifies to
\[
\det D(x,y)
=
-\frac{L(v-u)\bigl(L(u+v)-2uv\bigr)}
{u^2v^2(L-u)^2(L-v)^2}.
\]
Since
\[
L(u+v)-2uv=u(L-v)+v(L-u)>0,
\]
the determinant is strictly negative throughout the domain. The analytic inverse-function theorem therefore gives local analytic inverses, and uniqueness patches them into a global real-analytic inverse.

A separate numerical stress check over positive data spanning twelve orders of magnitude reproduced the input data after inversion and always returned an interior ordered pair of endpoints. This computation is corroborative only; the proof above is exact.
