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

The analytic proof uses the exact polynomial reduction from arXiv:1803.02867v1. The critical steps are the simple vanishing
\[
r_\theta(k,1)=-\frac{km}{m+2}(\theta-\theta_c),
\]
the positive cubic coefficient
\[
r_{\theta_c}(k,3)=\frac{2^{2/m}(k-1)\left((k+1)(m+2)^2-6k\right)}{3(m+2)(m+4)},
\]
and the implicit-function reduction in \(w=z^2\).

`verify.py` reconstructs the source polynomial from its two finite sums. It checks the closed cubic coefficient using exact rational arithmetic after removing the common factor \(2^{2/m}\), then isolates the unique positive root for several admissible parameter pairs and confirms convergence of the normalized ratio \(z_0/\sqrt{\theta-\theta_c}\) to the claimed amplitude. A successful replay prints `VERIFY_OK`.

The finite replay is not an exhaustive proof over all \(k\) and \(n\). The infinite-family claim follows from the coefficient identities and the analytic implicit-function argument. The verification does not test other Gibbs-state classes or nonlocal critical observables.
