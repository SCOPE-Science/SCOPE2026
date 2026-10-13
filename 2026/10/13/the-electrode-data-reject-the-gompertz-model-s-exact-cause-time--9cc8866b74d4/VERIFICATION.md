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
For latent cause-specific Gompertz hazards
\[
h_j(t)=\lambda_j e^{\theta t},
\]
the bundled checker verifies numerically that
\[
\frac{f_{T,J=j}(t)}{f_T(t)}
=
\frac{\lambda_j}{\lambda_1+\lambda_2}
\]
at multiple positive parameter values and times.

The checker then reconstructs the 45 failures and labels printed in the source electrode table. It uses doubled midranks so the tied observation is handled exactly with integer arithmetic.

A subset-sum dynamic program enumerates every possible 19-label assignment conditional on the 45 observed times. It verifies
\[
R_E=219,\qquad U=29,
\]
and counts
\[
44{,}812
\]
assignments at least as far from the null mean rank sum as observed, out of
\[
\binom{45}{19}=2{,}438{,}362{,}177{,}020.
\]

The exact two-sided conditional probability is therefore
\[
1.837790973889128\times10^{-8}.
\]
No fitted nuisance parameter or asymptotic approximation is used.
