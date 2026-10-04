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
The analytic verification has four load-bearing checks.

First, for \(k\) vertices of a regular simplex, summing the cap inequalities and applying Cauchy--Schwarz gives
\[
\cos\theta\le\sqrt{\frac{n-k+1}{kn}},
\]
and the normalized vertex sum attains equality. This gives the triple and quadruple onset angles.

Second, for three vertices,
\[
G=\frac{n+1}{n}I-\frac1nJ,
\]
with
\[
G^{-1}=\frac n{n+1}I+\frac n{(n+1)(n-2)}J
\]
and
\[
\det G=\left(\frac{n+1}{n}\right)^2\frac{n-2}{n}.
\]
These identities give the quadratic form and Jacobian in the exact triple-intersection integral.

Third, the onset rescaling gives the exact identity
\[
1-q_n(t)=2\sqrt{\frac n{3(n-2)}}\,d\left(3-\sum y_i\right)-d^2q_n(y-\mathbf1).
\]
For \(n\ge5\), the density exponent is nonnegative, so dominated convergence applies on the limiting simplex.

Fourth,
\[
\int_{\Delta_3}\left(3-\sum y_i\right)^{(n-5)/2}dy=3^{(n+1)/2}\frac{\Gamma((n-3)/2)}{\Gamma((n+3)/2)},
\]
which yields the stated coefficient. The accompanying checker verifies the exact matrix and threshold identities and the exponent/beta arithmetic. The \(n=4\) onset asymptotic is not asserted.
