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
For positive retained posterior target values \(g_i\) and \(h>0\), the corrected sample LINEX estimator is
\[
-\frac1h\log\!\left(\frac1M\sum_i e^{-h g_i}\right),
\]
while the source's Eq. (4.11) prints
\[
-\frac1h\log\!\left(\frac1M\sum_i e^{+h g_i}\right).
\]

The bundled checker verifies on several positive draw sequences that the printed expression is negative and the corrected expression is positive.

For the source simulation truth \(\alpha=1.3\), every negative estimate has squared error greater than \(1.69\). The published informative-prior LINEX MSE \(0.0032\) is therefore incompatible with literal use of Eq. (4.11).

The check is algebraic and does not depend on unavailable implementation code.
