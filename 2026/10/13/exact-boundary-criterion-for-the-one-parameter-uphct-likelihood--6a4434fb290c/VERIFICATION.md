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
With \(\delta=1/\gamma\), the parameter-dependent UPHCT likelihood is
\[
L(\delta)
=
(1+\delta)^\nu
(1+\delta s^*)^{-R^*}
\prod_i(1+\delta x_i)^{-(2+R_i)}.
\]
Its log-derivative is
\[
D(\delta)
=
\frac{\nu}{1+\delta}
-
\frac{R^*s^*}{1+\delta s^*}
-
\sum_i\frac{(2+R_i)x_i}{1+\delta x_i}.
\]
For \(0<y\le1\),
\[
\frac{y}{1+\delta y}\ge\frac{y}{1+\delta},
\]
so
\[
D(\delta)\le
\frac{\nu-R^*s^*-\sum_i(2+R_i)x_i}{1+\delta}.
\]
This proves nonexistence of a finite MLE on the boundary side. On the opposite side, \(D(0)>0\), while \(D(\delta)<0\) eventually and \(L(\delta)\to0\), proving finite existence.

The included checker verifies equality of the original and reciprocal-parameter likelihoods up to data-only factors, the complete-data criterion \(\bar X<1/2\), and an explicit censored boundary example.
