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

# Reproducibility

The standalone `verify.py` uses Python 3.9 or later with no third-party dependencies. Run `python verify.py` beside this file. It enumerates all subsets on each crown graph with 3–8 matched pairs using the actual open adjacency lists, tests domination and pairwise distinct exterior signatures, and builds a complete bivariate coefficient table. It independently expands the claimed four-state expression and checks both tables coefficient by coefficient. It also checks the exact minimum and total counts and the complete-bipartite baseline.

Observed totals for n=3..8: 36, 149, 588, 2103, 7178, 23913. Corresponding optimum counts: 14, 56, 30, 120, 350, 896. All tested cases passed. The combinatorial proof in `RESULT.md` establishes the infinite-range assertion; finite tests do not. No independent audit has been performed.
