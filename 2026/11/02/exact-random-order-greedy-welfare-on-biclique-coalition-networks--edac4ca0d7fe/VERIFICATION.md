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

The precise greedy algorithm uses a strict positive-gain rule and earliest-created-coalition tie-breaking. For every arrival word, it has exactly one mixed coalition after the first cross-part arrival; all later vertices join that coalition. This proves the finite law without relying on simulation.

`CHECK.py` was executed using Python 3 and passed 7,418 arrival-word tests, 316,646 fully labeled arrival-order tests, exact-rational full-law and mean comparisons for all part sizes through 8, and exact star-law comparisons through 24. The independent rational expressions are checked against direct arrival-order simulations, not just against equivalent code versions of the same recurrence.

The \(\operatorname{Beta}(a,1)\) limit and balanced-part convergence are mathematical consequences of the stated order-statistic and expectation arguments; finite tests do not certify those limits. Only the uniform complete-bipartite graph and designated tie-break are covered. An independent external audit has not been performed.
