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

Let
\[
2<p<\infty
\]
and assume
\[
h(F,F')=\sigma_p(F).
\]
The fresh theorem and monotonicity give
\[
h(F,F')
\le
\sigma_2(F)
\le
\sigma_p(F),
\]
so all three quantities are equal.

Let \(c_p\) minimize \(\sigma_p\), and put
\[
r_j=|z_j-c_p|.
\]
Then
\[
\sigma_2(F)
\le
\left(
\frac1n\sum r_j^2
\right)^{1/2}
\le
\left(
\frac1n\sum r_j^p
\right)^{1/p}
=
\sigma_p(F).
\]
Both inequalities are therefore equalities.

For normalized finite power means and
\[
p>2,
\]
equality between the second and \(p\)-th means occurs exactly when all entries are equal. Hence
\[
r_1=\cdots=r_n=R.
\]

If
\[
R=0,
\]
all roots coincide and the polynomial already has the required translated-power form.

If
\[
R>0,
\]
the affine change
\[
z=c_p+Rw
\]
puts every zero on the unit circle and changes the Hausdorff distance to
\[
1.
\]
Some zero attains that distance. Rotating it to \(1\) puts the normalized polynomial exactly under Rubinstein's boundary theorem, which forces a scalar multiple of
\[
w^n-1.
\]
Undoing the transformations gives
\[
F(z)=A(z-c)^n-B.
\]

Conversely, a polynomial of this form has either one repeated root or a regular \(n\)-gon of roots and a unique critical point at its center. Strict convexity and rotational symmetry make that center the \(p\)-variance minimizer, so
\[
h(F,F')=\sigma_p(F).
\]

No numerical or finite-computation step enters the proof.
