---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n≥2 the simple chords correspond to edges of the endpoint boundary cycle C_{2n}. The count of disjoint marked k-edge sets is (2n/(2n-k))*binomial(2n-k,k); conditional on all marked short chords, their crossings are zero and the residual matching is uniform on 2(n-k) endpoints. Summing ordered marked k-tuples gives E[(S_n)_k z^{X_n}]=a_{n,k}F_{n-k}(z) as a polynomial identity. Expanding u^{S_n} gives all fixed-S strata. The explicit bound 0≤a_{n,k}≤2 permits dominated convergence for characteristic functions; fixed-k variance normalization and known crossing CLT prove independent Pois(1) and Gaussian limits. Reconstructed exact boundary edge counts and exhaustively re-enumerated all perfect matchings for n=2,3,4,5 (3,15,105,945) to check every factorial transfer; enumeration is corroborative only.

## originality

PASS

Best-of-knowledge PASS for the exact joint bivariate probability-generating transfer and the joint independent mixed-scale limit, not for known marginal Poisson/normal laws or known covariance.

## value

PASS

Short boundary chords are local isolated structures and crossing number is a natural global statistic of uniform chord diagrams. Exact conditional crossing distributions for every short-chord count, especially zero-short-chord diagrams, and proof of local/global asymptotic independence are useful natural joint invariants not supplied by separate marginals or covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
