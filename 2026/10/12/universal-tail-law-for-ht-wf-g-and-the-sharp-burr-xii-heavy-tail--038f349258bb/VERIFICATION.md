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
For baseline survival \(s\to0\),
\[
s\left[s^{-(1-s)}-1\right]
=
e^{s\log s}-s
\to1.
\]
Thus
\[
A=\left[s^{-G}-1\right]^\alpha
\sim s^{-\alpha}.
\]
The exact generated survival is
\[
S=
\left[
\frac{e^{-A}}{\lambda+(1-\lambda)e^{-A}}
\right]^\lambda,
\]
so
\[
-\log S
=
\lambda A
+
\lambda\log\!\left(\lambda+(1-\lambda)e^{-A}\right)
\sim
\lambda s^{-\alpha}.
\]

For Burr XII, \(s=(1+x^\beta)^{-k}\), giving
\[
-\log S\sim\lambda x^{\alpha\beta k}.
\]
The heavy-tail trichotomy follows by comparing \(p x-\lambda x^{\alpha\beta k}\) for fixed \(p>0\). The quantile law follows by monotone asymptotic inversion.

For Weibull survival \(s=e^{-c x^\omega}\),
\[
-\log S\sim\lambda e^{\alpha c x^\omega}.
\]

The bundled checker evaluates the exact formula only as a numerical consistency test. The infinite-domain conclusions are the analytic consequences above. No statement is made about the critical exponential moment exactly at \(t=\lambda\).
