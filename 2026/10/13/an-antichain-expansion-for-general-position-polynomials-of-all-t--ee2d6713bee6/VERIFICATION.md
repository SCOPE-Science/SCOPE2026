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

# Finite reproducibility and proof scope

Run `python3 verify.py` from this directory (Python 3 standard library only). The two independently coded polynomial algorithms are compared against a third direct BFS shortest-path subset census. The verifier enumerates all Prüfer-labeled trees of orders 1 through 6 and separately tests randomized trees of orders 7 through 10, different roots, distinct numeric vertex weights, cubic coefficients through vertex-deletion components, and a published broom-tree polynomial.

Captured output:

```text
ORDER 1 checked
ORDER 2 checked
ORDER 3 checked
ORDER 4 checked
ORDER 5 checked
ORDER 6 checked
ORDER 7 checked
ORDER 8 checked
ORDER 9 checked
ORDER 10 checked
VERIFIED: trees 1692 unweighted_subsets 166590 root_rechecks 3384 weighted_evaluations 110 broom_formulas 49
```

There were 1,692 tested trees, 166,590 unweighted subset tests, 3,384 further root evaluations, 110 independent vertex-weight evaluations and 49 broom-family comparisons. These are bounded tests and do not certify all trees. The mathematical proof in RESULT.md is the infinite-family justification; no independent audit has occurred.
