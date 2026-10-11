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
The packaged `verify.py` uses only the Python standard library and exact rational arithmetic.

It verifies the circulant determinant identity
\[
\det A
=
(a+b+c)
\left(
a^2+b^2+c^2-ab-bc-ca
\right),
\]
and its squared-difference factorization.

It verifies that the unique solution of the stationary mean equations is
\[
M_1=M_2=M_3=\frac{\mu}{a+b+c}
\]
when the interaction coefficients are not all equal.

It verifies the pointwise residual formula
\[
Q_i-(\mu-aX_i)=-r_i,
\]
the abstract orthogonal variance and covariance decomposition, and
\[
r_1+r_2+r_3=3\mu-(a+b+c)S.
\]

At
\[
(\mu,a,b,c)
=
\left(
1,1,\frac{11}{20},\frac32
\right),
\]
it verifies
\[
M_i=\frac{20}{61},
\qquad
\mathbb E[S]=\frac{60}{61}.
\]

The conditional-expectation step is an analytic cutoff argument in `RESULT.md`; no finite trajectory experiment is used as proof.
