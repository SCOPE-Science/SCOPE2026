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

The analytic proof has four critical components.

1. If \(\rho_{ij}\ge0\), covariance of nondecreasing transforms of a bivariate Gaussian pair is nonnegative. This follows by conditioning one coordinate on the other and applying the scalar covariance identity for two increasing functions.

2. If \(\rho_{ij}<0\), Hermite expansion gives
\[
|\operatorname{Cov}(T_i,T_j)|
\le
|\rho_{ij}|\|T_i\|_2\|T_j\|_2,
\]
hence
\[
\operatorname{Cov}(T_i,T_j)
\ge
\rho_{ij}\|T_i\|_2\|T_j\|_2.
\]

3. Because the negative edges are disjoint, each two-coordinate block satisfies
\[
s_i^2+s_j^2+2\rho_{ij}s_is_j
\ge
(1+\rho_*)(s_i^2+s_j^2).
\]
Linear transforms on a most-negative pair attain equality in the infimum.

4. The matrix constant obeys the same block lower bound, and equality in its infimum is approached by sending all weights outside a most-negative pair to zero.

The standalone script `verify.py` checks the block inequality and finite-Hermite maximal-correlation inequality in exact rational arithmetic, and checks a singular rank-two example with
\[
\cos\theta=\frac35,\qquad
\sin\theta=\frac45.
\]
For that example,
\[
\det R_\theta=0,\qquad
\beta(\mu)=\alpha(R_\theta)=\frac15.
\]

Expected successful terminal line:
`VERIFY_OK block_cases=1764 hermite_cases=192 singular_beta=1/5`.

These finite calculations are reproducibility checks only and do not replace the all-dimensional proof.
