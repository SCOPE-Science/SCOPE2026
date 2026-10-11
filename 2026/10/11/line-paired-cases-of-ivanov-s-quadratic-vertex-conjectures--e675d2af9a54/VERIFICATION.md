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

For the line-paired containment theorem, polarity gives
\[
K^\circ=
\left\{
\sum_i t_iw_i:
-\frac1{\beta_i}\le t_i\le\frac1{\alpha_i}
\right\}
\subseteq B^d.
\]
Choosing endpoint coordinates with zero mean gives the exact identity
\[
\mathbb E\left\|\sum_iT_iw_i\right\|^2
=
\sum_i\frac{\|w_i\|^2}{\alpha_i\beta_i}
\le1.
\]
Since \(\|w_i\|\ge1\), the entire proof reduces to
\[
\sum_i\frac1{\alpha_i\beta_i}\le1.
\]
The two stated bounds then follow from AM--GM and Cauchy--Schwarz. Equality forces every intermediate inequality to be an equality, yielding the regular cross-polytope.

For a line-paired tight frame, the square matrix with columns
\[
\sqrt{a_i^2+b_i^2}\,u_i
\]
is orthogonal. Thus the polar is an orthogonal box. Its Gaussian vertex distribution is uniform over orthants, and
\[
A_\gamma(C)=D+m\otimes m
\succeq D,
\]
where the diagonal entries of \(D\) are
\[
\frac14\left(\frac1{a_i}+\frac1{b_i}\right)^2.
\]
Operator monotonicity of the positive square root and \(a_i^2+b_i^2=1\) give the claimed trace bound.

The bundled checker uses exact rational arithmetic to replay the endpoint-moment identity, the scalar inequalities on many rational instances satisfying the derived reciprocal-product condition, the equality configuration, and the tight-frame scalar estimate on rational Pythagorean pairs. These finite checks are supplementary and are not used as proof of the all-dimensional theorem.
