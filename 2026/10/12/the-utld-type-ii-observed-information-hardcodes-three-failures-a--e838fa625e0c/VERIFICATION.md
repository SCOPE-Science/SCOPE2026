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
z=x_r(2-x_r),
\qquad
q=z^\alpha,
\qquad
L=\log z.
\]
The Type-II log-likelihood terms with nonzero second derivative are
\[
r\log\alpha
+
(n-r)\log(1-z^\alpha).
\]
Therefore
\[
\ell''(\alpha)
=
-\frac{r}{\alpha^2}
-
(n-r)\frac{qL^2}{(1-q)^2}.
\]

The source's displayed expression is
\[
H_{\mathrm{pub}}
=
\frac{
q\{6-\alpha^2(n-3)L^2\}
-3(q^2+1)
}{
(q-1)^2
}.
\]
The included checker verifies that
\[
H_{\mathrm{pub}}
=
\alpha^2\ell''(\alpha)
\]
when \(r=3\), and that it fails to track the true Hessian as \(r\) changes.

At
\[
(n,r,\alpha,x_r)=(10,3,1/2,1/2),
\]
the correct inverse observed information is
\[
0.02503017846873498\ldots,
\]
while literal inversion of the source display gives
\[
0.10012071387493991\ldots.
\]

The checker also differentiates the actual likelihood numerically at several admissible points and confirms the corrected closed form.
