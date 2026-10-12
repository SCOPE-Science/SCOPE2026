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

# Reproducibility and limits

Run `python3 verify_coalescent.py` in a standard Python 3 environment; no external packages or downloads are needed. The test independently propagates the exact rational probability of each partition under uniformly chosen binary mergers for \(2\le n\le8\), then compares coalescent-stage counts with the theorem's binomial formula. It evaluates the covariance from the independently enumerated counts, all legal signed finite differences, the two endpoint covariances, and both deterministic consistency identities. The exact portion produces 140 passed assertions, with the status line `EXACT_OK`.

The program also compares \(n\operatorname{Cov}(H_n,L_{n,r})\) against the continuum profile at five fraction values for \(n=500,1000,2000\). These finite approximations are sanity checks only; they do not establish a limit or inequality for all \(n\). General correctness relies on the published exact lineage-size identity and its independent-time consequence, Pascal's rule and summable dominated convergence, as reconstructed in `RESULT.md`. No independent audit has been performed.
