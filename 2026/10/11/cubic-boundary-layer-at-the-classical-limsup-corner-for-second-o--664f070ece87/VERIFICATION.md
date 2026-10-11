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

The source formula used for the new claim is
\[
\beta(a)=2a-2d+\sqrt{2d^2+\frac4{rs}-2},
\qquad
d=\frac1s-\frac1r,
\]
with spectral roots satisfying
\[
r^2=e^{ar},\qquad s^2=e^{-as}.
\]
The principal analytic solutions near \(a=0\) are
\[
r(a)=-\frac{2}{a}W_0\!\left(-\frac a2\right),
\qquad
s(a)=\frac{2}{a}W_0\!\left(\frac a2\right).
\]

`verify_series.py` replays the needed truncated-series identities with exact rational coefficients and returns `VERIFY_OK`. In particular it checks the spectral equations and the rational part of the boundary expansion through the orders needed for
\[
2d^2+\frac4{rs}-2=2-\frac{a^4}{6}+O(a^6).
\]
The remaining square-root expansion is the ordinary analytic identity
\[
\sqrt{2-\frac{a^4}{6}+O(a^6)}
=\sqrt2-\frac{\sqrt2}{24}a^4+O(a^6).
\]

The phase comparison uses only
\[
b(a)-\beta(a)=\left(\frac13-\kappa\right)a^3+o(a^3).
\]
For fixed \(\kappa\ne1/3\), this has a definite sign for sufficiently small positive \(a\). The source's necessity theorem applies on the upper side and its sharpness construction applies on the lower side.

Limits: no assertion is made at the exactly critical cubic coefficient without finer data, and no numerical sampling is used to justify the asymptotic statement.
