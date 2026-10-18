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

# Computational verification and proof boundaries

The included standard-library `verify.py` is the only program needed. Invoke `python verify.py` in a directory containing this file. It uses exact rational arithmetic to enumerate all \((n-1)^{n-1}\) assignments of independent candidate parents for each \(2\le n\le8\), without invoking the proved covariance expressions in its forest generator. For each sampled forest it computes the number of components, every undirected degree class, and the number of zero-outdegree vertices. It then compares these exact empirical covariances against the formulas in RESULT.md.

Additional exact-rational assertions for \(3\le n\le70\) verify the degree-one factorization, the complete sign diagram and conservation of total vertex count. Floating-point asymptotic checks at \(n\in\{201,501,1001,5001\}\) compare with the two analytic constants. The result is `VERIFY_OK exact/numeric assertions 2614`. Finite checks corroborate but do not replace the published-sampler reduction, exact conditional-covariance identities, termwise sign proof or analytic Riemann-sum limits. No independent mathematical audit has been conducted.
