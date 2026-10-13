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

The exact domain is an iid centered \(\mathbb R^d\)-valued random walk with finite nonzero second moment \(\tau=\mathbb E\|X_1\|^2\), return local time \(L_n=\sum_{k=1}^n\mathbf 1\{S_k=0\}\), and terminal quadratic energy \(\|S_n\|^2\).

The critical proof step is the conditional second moment
\[
\mathbb E[\|S_n\|^2\mid S_k=0]=(n-k)\tau,
\]
which follows because the post-\(k\) increments are independent of \(S_k\), centered, and have total second moment \((n-k)\tau\). Therefore
\[
\operatorname{Cov}(\mathbf 1\{S_k=0\},\|S_n\|^2)
=-k\tau\,\mathbb P(S_k=0).
\]
Summation is exact and contains no limiting argument.

For simple symmetric walk, `checker.py` exhaustively enumerates all sign paths for each length through \(18\), recomputes local time and terminal energy directly, and checks the covariance, local-time variance, endpoint-energy variance, and correlation formulas using exact rational arithmetic. It also checks the general theorem for a centered but nonsymmetric three-point increment law by exact weighted enumeration.

The all-\(n\) proof is symbolic. Finite enumeration is supplementary and is not used as evidence of an infinite statement.
