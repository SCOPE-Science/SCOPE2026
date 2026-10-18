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

# Verification evidence and scope

Run `python verify_non_nested_rarefaction.py` with Python 3, using only the standard library.

The program fully enumerates species abundance-pair multisets of total census \(2\le N\le6\), quotients by species permutation and habitat exchange, and obtains class counts \(2,4,14,28,69\). For every profile and every feasible pair of habitat sample sizes, it compares exact hypergeometric expectations against independently averaged labeled-subset enumerations (1,462 values). It checks both consecutive-budget incompatibility and global reachability of nested optimal allocations. At census six there are exactly three globally nonnesting classes, one of which has a forced incompatible consecutive optimum at budgets two and three.

The program also checks the algebraic deficit expression and unique optima of the unbounded family for 117 finite parameter combinations. The general infinite family is proved analytically using the exact deficit and its strict inequality; the disjoint-species case is proved by diminishing marginal increments. Numeric experimentation is neither a proof of the infinite results nor a substitute for the exhaustive finite certificate.

Scientific limits: fixed known integer abundances, two habitats, independent uniform samples without replacement, equal unit costs, accurate species labels, unconditional expected union richness. This is not an independent audit or experimental ecological validation.
