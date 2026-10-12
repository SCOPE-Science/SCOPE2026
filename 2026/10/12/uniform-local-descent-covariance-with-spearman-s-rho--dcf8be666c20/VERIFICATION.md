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

The proof is analytic for every \(n\ge2\).

`checker.py` exhaustively enumerates every permutation for \(2\le n\le9\). For each adjacent position it checks
\[
\operatorname{Cov}(I_i,D_n)=\frac{n+1}{6},
\qquad
\operatorname{Cov}(I_i,R_n)=-\frac1{n(n-1)},
\]
as well as both conditional means of \(R_n\). It also checks the global covariances, the descent-count variance, the Spearman variance, and the correlation-squared formula.

A second exact-rational loop through \(n=500\) evaluates the maximum and minimum of every uniformly chosen two-element subset in closed finite sums and reconstructs the position-independent conditional shift of the rank inner product.

The finite computations are supplementary. No bounded enumeration is used to justify the universal statement.
