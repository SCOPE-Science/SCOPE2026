---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Matrix-tree theorem for a fixed root set of size c yields c n^{n-c-1} rooted forests and the truncated-Poisson cycle distribution. Deleting j specified pendant vertices gives c(n-j)^{n-c-1} surviving attachments, which agrees for all j with avoidance of j specified boxes after n-c-1 uniform throws. For c=n, pure cycle L=0. Conditional mean m(1-1/n)^{m-1} strictly increases with m=n-c (for supported m), producing negative covariance via the independent-copy identity. Conditional occupancy martingale decomposition yields vacancy CLT variance (e-2)/e^2, uniformly for c=O(sqrt n); n-C is Poisson(n) conditioned below n-3, hence C/sqrt n -> |N|. The quadratic mean response (1-x^2)/(2e), bounded uniformly integrably, gives -1/(e sqrt(2pi)) covariance limit. Direct independent complete n-edge graph census n=3..6 checked exact conditional factorial moments. General assertions proved analytically, finite enumeration corroborative.

## originality

PASS

Qualified PASS for the exact conditional vacancy law and combined first-order independence / nonzero second-order mixed covariance. Existing unicyclic tables determine cycle-length marginal, and other prior papers treat evolving multigraph component sizes or Laplacian coefficient extremality, not the bivariate conditional statistic. Specialized conditioned random-graph theory remains a meaningful priority risk.

## value

PASS

Cycle length and number of leaves are canonical unicyclic graph statistics; their exact joint dependence is a motivated structural probability question. A sharp second-order covariance survives an independent limiting pair, revealing nontrivial finite-size dependence not visible in marginal laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
