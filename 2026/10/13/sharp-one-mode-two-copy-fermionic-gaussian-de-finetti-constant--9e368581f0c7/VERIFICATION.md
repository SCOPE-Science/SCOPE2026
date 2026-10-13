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

The proof reduces the problem to two scalar covariance-sector parameters \(u,v\in[-1,1]\). With \(h=(u-v)/(2n)\), the rotated two-copy Gaussian state and the product marginal commute, and the four diagonal probability differences are
\[
-h^2,\quad -h^2,\quad h+h^2,\quad -h+h^2.
\]
For \(|h|\le1/n\le1/2\), their absolute sum is exactly
\[
2|h|+2h^2.
\]
The exchangeability box implies \(|h|\le1/n\), and the expression is increasing in \(|h|\). This proves the exact maximum \(2/n+2/n^2\). Equality requires \(|u-v|=2\), hence opposite pure sector covariances.

The file `artifacts/verify.py` replays exact-rational checks of these identities and the bound on deterministic rational grids for \(2\le n\le64\). Its output must be `VERIFY_OK`. These checks do not certify the continuum or the infinite family; those are covered by the analytic argument.

Scientific limits: only the one-mode, two-copy retained marginal is resolved. No claim is made for \(k>2\), multiple modes per copy, non-Gaussian states, or other exchangeability symmetries.
