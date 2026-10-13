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

The proof is analytic. The accompanying checker performs an independent exhaustive replay over every random-recursive-tree parent sequence for \(2\le n\le10\).

There are exactly
\[\sum_{m=1}^{9}m!=409113\]
trees in that replay.

For each tree, the checker constructs every depth from the parent array, counts leaves by outdegree, computes total path length, and computes the sum of depths over leaves.

Using exact rational arithmetic, it verifies \(\mathbb E L_n=n/2\), \(\mathbb E P_n=nH_{n-1}-(n-1)\), \(\mathbb E Q_n=\frac n2H_{n-1}-\frac{n-2}{4}\), \(\operatorname{Cov}(L_n,P_n)=-(n-2)/4\), and, for \(n\ge3\), \(\operatorname{Var}(L_n)=n/12\) together with the exact least-squares slope.

The enumeration is supplementary and does not establish the all-\(n\) theorem. The universal proof is the growth recurrence in `RESULT.md`.

Independent audit has not been performed.

Exact replay result: `VERIFY_OK sizes=9 trees=409113 first_moment_checks=27 covariance_checks=9 leaf_variance_checks=8 slope_checks=8`.
