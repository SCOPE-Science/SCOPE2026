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

The proof was checked by two routes. First, direct Dirichlet moment algebra gives the closed variance of latent Gini–Simpson diversity and the adjacent/disjoint edge covariances used in the transition-count variance. Second, `checker.py` performs exact rational enumeration of the Pólya predictive law for \(m\in\{2,3,4\}\), \(lpha\in\{1/2,1,3/2\}\), and \(2\le n\le6\). For each complete sequence it also evaluates the posterior mean of the latent diversity, allowing an exact check of the mixed moment rather than only marginal moments.

The checker reports 45 parameter cases and 20,007 sequence states, verifying normalization, mean transition count, transition-count variance, and mixed transition–diversity covariance. These finite checks are consistency tests only; the proof establishes the formulas for every \(m\ge2\), \(lpha>0\), and \(n\ge2\).

The originality comparison inspected the full multicolor Pólya-run paper and compared the statement against the closest accessible exchangeable-run record and prior published claims. A complete copy of the separate 2008 Statistics & Probability Letters paper was not available in the open sources checked, so it is retained as a residual literature risk.
