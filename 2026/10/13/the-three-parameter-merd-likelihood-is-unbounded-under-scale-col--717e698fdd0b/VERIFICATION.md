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
For a sample with minimum \(m\), let
\[
y_i=x_i-m
\]
and
\[
S(\sigma)
=
\sum_i
\left(
\sqrt{1+y_i/\sigma}-1
\right).
\]
If the minimum has multiplicity \(k\) and at least one \(y_i>0\), then
\[
S(\sigma)
=
C\sigma^{-1/2}+O(1),
\qquad
C=\sum_{y_i>0}\sqrt{y_i}>0.
\]
Substitution into the source's profile log-likelihood gives
\[
\ell_p(\sigma)
=
-\frac{k}{2}\log\sigma+O(1).
\]
Hence the full likelihood is unbounded along
\[
\tau=m,
\qquad
\sigma\downarrow0,
\qquad
\lambda=n/S(\sigma).
\]

The bundled checker verifies the profile formula against the direct joint log-likelihood. For a unique minimum, decade-to-decade increments approach \((1/2)\log10\); for two tied minima they approach \(\log10\). It also verifies \(\widehat\lambda(\sigma)/\sqrt{\sigma}\to n/C\).
