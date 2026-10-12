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

The analytic calculation uses the exact identity
\[
X=e^{Y/k},
\qquad
\mathbb E e^{tY}=\Gamma(1+t),
\]
where \(e^Y\) is unit exponential. Expanding \(\log\Gamma(1+t)\) through cubic order gives the reflected-Gumbel mean, variance, and third cumulant. These determine
\[
\frac1r\log(m_r-s_r)
=
-\gamma-\frac{\pi}{\sqrt6}
+\frac{\sqrt6\,\zeta(3)}{\pi}r
+O(r^2)
\]
and
\[
\frac1r\log(m_r+s_r)
=
-\gamma+\frac{\pi}{\sqrt6}
-\frac{\sqrt6\,\zeta(3)}{\pi}r
+O(r^2),
\]
with \(r=1/k\). Taylor expansion of the reflected-Gumbel CDF at these two fixed limiting endpoints gives the claimed central-mass expansion.

The standalone script `verify_weibull_gumbel_endpoint.py` directly evaluates the exact Weibull mean, variance and CDF at several large shapes and compares them with the first-order formula. Its replayed output is:

`VERIFY_OK Cinf=0.723751267519710 A=0.375466930347350 scaled_k1000=0.374582858306976`

The numerical checks are finite regression tests only. They do not certify the asymptotic remainder or replace the analytic proof. The theorem is limited to the ordinary one-dimensional Weibull family and the large-shape regime.
