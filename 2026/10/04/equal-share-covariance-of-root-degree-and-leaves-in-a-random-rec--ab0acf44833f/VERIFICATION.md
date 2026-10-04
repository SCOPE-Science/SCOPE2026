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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

It exhaustively enumerates every recursive-tree parent sequence through \(n=9\). For each tree it reconstructs root degree, total leaves, every root-attachment indicator, and every labeled leaf indicator.

It verifies the local formula
\[
\operatorname{Cov}(D_n,Y_i)=\frac{n-i}{(n-1)^2},
\]
the equal-share formula
\[
\operatorname{Cov}(A_j,L_n)=\frac1{2(n-1)}
\]
for all \(j\ge3\), and the total covariance.

It also verifies exact means and variances and the correlation identity. A separate recursion check confirms \(\operatorname{Var}(L_n)=n/12\) for a large range of \(n\).

Finite replay is supplementary. The all-\(n\) theorem is the independent-parent and leaf-survival calculation in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK trees_checked=46233 labeled_leaf_cov_checks=72 attachment_leaf_cov_checks=36 global_cov_checks=8 marginal_checks=32 recursion_checks=996 correlation_checks=7`.
