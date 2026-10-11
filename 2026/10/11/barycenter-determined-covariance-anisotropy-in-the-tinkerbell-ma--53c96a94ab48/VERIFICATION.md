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

It verifies the stationary raw-moment reductions
\[
\mathbb E[x^2-y^2]=(1-a)u-bv
\]
and
\[
2\mathbb E[xy]=-cu+(1-d)v,
\]
then checks their conversion to
\[
p-r=A(u,v),
\qquad
2q=B(u,v).
\]

It verifies the exact covariance spectral identities
\[
(\lambda_+-\lambda_-)^2=(p-r)^2+4q^2
\]
and
\[
4\det\Sigma
=
(\operatorname{tr}\Sigma)^2-
\left((p-r)^2+4q^2\right).
\]

For
\[
(a,b,c,d)
=
\left(
\frac9{10},
-\frac{6013}{10000},
2,
\frac12
\right),
\]
it verifies the exact coefficient specialization used in `RESULT.md`.

The stored output in `verification_output.txt` is `VERIFY_OK`.

The invariant-measure step is an analytic use of stationarity, and the covariance bound is exact positive-semidefinite matrix algebra; neither is inferred from finite orbit sampling.
