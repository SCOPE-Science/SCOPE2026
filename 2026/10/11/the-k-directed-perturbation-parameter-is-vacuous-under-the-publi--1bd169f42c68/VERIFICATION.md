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

Let the source perturbation inequality be
\[
D(f,g)
\le
\lambda_1L(f,g)+\lambda_2G(f,g)+\gamma\|K^*f\|^2
\]
for every \(f,g\in H\).

For \(t>0\),
\[
D(f,tg)=tD(f,g),\qquad
L(f,tg)=tL(f,g),\qquad
G(f,tg)=tG(f,g).
\]
Therefore
\[
D(f,g)
\le
\lambda_1L(f,g)+\lambda_2G(f,g)
+\frac{\gamma}{t}\|K^*f\|^2.
\]
Letting \(t\to\infty\) proves the gamma-free inequality.

Set \(g=f\) and abbreviate
\[
X=\int_\Omega\|\Lambda_\omega f\|^2\,d\mu(\omega),
\qquad
Y=\int_\Omega\|\Gamma_\omega f\|^2\,d\mu(\omega).
\]
The triangle inequality and the gamma-free perturbation estimate give
\[
Y\le(1+\lambda_1)X+\lambda_2Y
\]
and
\[
X\le\lambda_1X+(1+\lambda_2)Y.
\]
Hence
\[
\frac{1-\lambda_1}{1+\lambda_2}X
\le Y\le
\frac{1+\lambda_1}{1-\lambda_2}X.
\]

For a one-point scalar family with \(K=I\), \(\Lambda=aI\), and \(\Gamma=bI\), the hypothesis reduces exactly to
\[
|a^2-b^2|
\le
\lambda_1a^2+\lambda_2b^2.
\]
Equality holds at each endpoint
\[
\frac{b^2}{a^2}
=
\frac{1-\lambda_1}{1+\lambda_2},
\qquad
\frac{b^2}{a^2}
=
\frac{1+\lambda_1}{1-\lambda_2},
\]
which verifies sharpness.

The primary PDF was inspected at Theorem 4.1 and its complete proof, including visual inspection of the theorem and lower-bound pages. No numerical experiment is used.
