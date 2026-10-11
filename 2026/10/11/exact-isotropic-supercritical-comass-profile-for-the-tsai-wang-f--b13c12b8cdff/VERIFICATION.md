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

For equal singular values \(\lambda\), the primary graph-plane formula reduces to
\[
\Theta(\Gamma_B)
=
(1+\lambda^2)^{r/2}
\frac{a+d\,\operatorname{tr}B}
{\sqrt{\det(I+B^TB)}},
\]
where
\[
a=\frac{1-(r-1)\lambda^2}{1+\lambda^2},
\qquad
d=\frac{\lambda}{1+\lambda^2}.
\]

If \(b_i=\tan\theta_i\) are the singular values of \(B\), the trace inequality reduces the absolute value to the scalar objective
\[
H=
q\prod_i\cos\theta_i
+
d\sum_i\sin\theta_i\prod_{j\ne i}\cos\theta_j,
\qquad
q=|a|.
\]
For a pair \(\alpha=u+v\), \(\beta=u-v\), holding all other angles fixed,
\[
H(u,u)-H(u+v,u-v)=Q\sin^2v\ge0.
\]
Thus all singular values may be equalized without decreasing the objective.

The resulting one-variable function is
\[
h(t)
=
(1+\lambda^2)^{r/2}
\frac{q+rdt}{(1+t^2)^{r/2}}.
\]
Its derivative has the sign of
\[
d-qt-(r-1)dt^2.
\]

When
\[
(r-1)\lambda^2\le1,
\]
the unique nonnegative root is \(t=\lambda\), and \(h(\lambda)=1\).

When
\[
(r-1)\lambda^2>1,
\]
the unique positive root is
\[
t=\frac1{(r-1)\lambda}.
\]
Substitution gives
\[
h(t)
=
\frac{(r-1)^{r-1}\lambda^r(1+\lambda^2)^{(r-2)/2}}
{\bigl(1+(r-1)^2\lambda^2\bigr)^{(r-2)/2}}.
\]
Taking \(B=-tI_r\) gives equality in the trace estimate and hence attains this value.

The bundled checker verifies these identities symbolically, checks continuity at the sharp boundary, and verifies the \(r=3\) specialization.

No finite numerical search is used to establish the global maximum.
