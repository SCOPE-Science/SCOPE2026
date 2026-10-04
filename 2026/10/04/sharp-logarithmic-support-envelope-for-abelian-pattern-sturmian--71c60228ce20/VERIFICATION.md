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

The proof was checked symbolically from the definitions.

1. For each integer \(N\ge0\), the finite induced graph on left and right labels \(0,\ldots,N\) has \(2N+2\) vertices and at most \(2N+1\) edges because it is a forest.
2. For every \(d\le N\) in the support, exactly \(d+1\) of those edges have endpoint-label sum \(d\). Different sums give different edges. Hence \(\sum_{d\le N}(d+1)\le2N+1\).
3. Setting \(N=d_n\) gives \(d_n\ge\sum_{j<n}(d_j+1)\). With \(a_j=d_j+1\), induction gives \(a_n\ge2^n\), hence \(d_n\ge2^n-1\).
4. If \(k=|D\cap[0,N]|\), then \(2^{k-1}-1\le d_{k-1}\le N\), yielding \(k\le1+\lfloor\log_2(N+1)\rfloor\).
5. For \(D_*=\{2^n-1:n\ge0\}\), one has \(d_{{n+1}}=2d_n+1>2d_n\). The checked sufficient-gap proposition in arXiv:2609.28059v1 therefore makes \(\Gamma_{D_*}\) a forest, and the checked incidence-forest characterization makes its characteristic word Abelian pattern Sturmian.

No finite experiment is used to infer an infinite statement. The external theorem inputs are limited to the two cited results from arXiv:2609.28059v1; the edge count, recurrence, induction and inversion are elementary and complete.
