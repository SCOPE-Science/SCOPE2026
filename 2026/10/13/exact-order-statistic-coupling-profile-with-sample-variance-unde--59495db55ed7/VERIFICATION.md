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

The theorem is proved analytically for every \(n\ge2\) and every \(1\le k\le n\).

`checker.py` uses two exact-rational routes. The first expands order statistics in uniform Dirichlet spacings and computes the required cubic mixed moments directly for all \(2\le n\le12\). The second reconstructs the conditional mean of the sample variance from the two conditional uniform groups and combines it with beta moments for every rank through \(n=1000\).

The checker verifies the covariance, the two marginal variances, the correlation-squared identity, reflection antisymmetry
\[
\operatorname{Cov}(X_{(n+1-k)},S^2)
=
-\operatorname{Cov}(X_{(k)},S^2),
\]
and exact median zero when \(n\) is odd.

The bounded computations are consistency checks only; the universal quantifiers come from the symbolic proof.
