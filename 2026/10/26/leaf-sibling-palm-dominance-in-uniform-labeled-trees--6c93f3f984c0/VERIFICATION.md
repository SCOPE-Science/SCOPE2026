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

The analytic deletion bijection, occupancy representation, one-step stochastic coupling, and asymptotic Taylor expansions prove the result for every integer \(n\ge4\). The finite checker `verify.py` enumerates every Prüfer word for \(4\le n\le8\), totaling 280388 trees, with counts recovered from actual adjacency lists. It verifies the full count-size-biased probability law, its moments, all stochastic survival tails, and the covariance identity with exact rational arithmetic. Additionally 497 finite sizes through \(n=500\) have their kernel inequality checked. All enumerated cases passed. Enumeration is not used as an infinite proof; it does not assert independence or any conditioned-on-\(C>0\) stochastic order. The historical overlap comparisons were based on accessible original sources, and older unindexed equivalents remain possible.
