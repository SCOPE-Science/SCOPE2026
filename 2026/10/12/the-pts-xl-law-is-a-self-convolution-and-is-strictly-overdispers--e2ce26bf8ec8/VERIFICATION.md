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
The checker symbolically verifies
\[
G_{PTS}(z)=G_{PXL}(z)^2.
\]

It also compares the source PTS-XL PMF against the discrete convolution of two PXL PMFs for multiple positive parameter values and count values.

For the source dispersion index it verifies
\[
DI(\theta)-1
=
\frac{\theta^4+4\theta^3+8\theta^2+8\theta+2}
{\theta(1+\theta)^2(\theta^2+2\theta+2)}.
\]
Every factor in the denominator is positive for \(\theta>0\), and the numerator has strictly positive coefficients.

Finally, it verifies the large-\(\theta\) limits
\[
\theta\{DI(\theta)-1\}\to1
\]
and
\[
\theta E[N]\to2.
\]

The numerical PMF checks supplement the analytic convolution proof.
