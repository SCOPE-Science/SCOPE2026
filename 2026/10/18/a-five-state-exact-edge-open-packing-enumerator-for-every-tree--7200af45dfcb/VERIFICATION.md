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

# Verification and reproducibility

Run `python3 verify.py` with a Python 3 standard-library interpreter. The program builds each graph from its Prüfer sequence, constructs all pairs of distinct selected edges, checks third-edge conflicts using the original definition, and compares the count at each cardinality to the independent five-state recurrence implementation. There is no external dependency.

Observed output (also in `verification_output.txt`):

```
VERIFICATION_OK labeled_trees=18249 edge_subsets=1119263 random_larger_trees=860
```

All 18,249 labeled trees on 1–7 vertices were covered and every one of their 1,119,263 selected-edge subsets was examined. A further 860 deterministic pseudorandom trees of orders 8–50 received polynomial-degree and nonnegativity sanity checks. The output was reproduced from the provided standalone code. These are finite tests only: the general theorem and operation bound follow from the proof in `RESULT.md`. The tests do not establish literature priority, unrestricted behavior by extrapolation, or any independent audit.
