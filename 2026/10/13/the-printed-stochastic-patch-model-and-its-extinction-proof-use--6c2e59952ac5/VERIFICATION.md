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
The bundled checker verifies the two variance minimizations exactly.

For independent Brownian drivers it checks
\[
\min_{0\le p\le1}
\left[
\sigma_1^2p^2+\sigma_2^2(1-p)^2
\right]
=
\frac{\sigma_1^2\sigma_2^2}
{\sigma_1^2+\sigma_2^2}.
\]

For the common positive Brownian loading printed in the model it checks
\[
\min_{0\le p\le1}
\left[
\sigma_1p+\sigma_2(1-p)
\right]^2
=
\min\{\sigma_1^2,\sigma_2^2\}.
\]

For
\[
r=\frac38,
\qquad
\sigma_1=\sigma_2=1,
\]
it verifies
\[
\Lambda=\frac34,
\qquad
v_{\mathrm{ind}}=\frac12,
\qquad
v_{\mathrm{com}}=1.
\]
Thus
\[
\Lambda>v_{\mathrm{ind}}
\]
but
\[
\Lambda<v_{\mathrm{com}}.
\]

The proof of exponential extinction in the witness is analytic and uses the exact common-noise total-population equation together with
\[
B_1(t)/t\to0
\]
almost surely.
