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

# Verification notes

The exact theorem is proved by the four pointed rank-two extension types in `RESULT.md`; no finite cutoff is asserted as a substitute for this proof. The rank-three signature checker enumerates each first choice, every second choice (including equality), and every permitted third-choice equality/adjacency pattern, retaining all actual existence responses. It found six distinct representative theories and confirmed the stable class for complete trees of branching 2–5 and heights 3–5 where the graph contained at most 390 vertices. It also checked two-vertex domination for the height-two boundary.

The independently organized local-pattern program computes graph distances and checks the formula for all four third-vertex adjacency patterns after each ordered distinct pair in six trees, and checks all four predicted first-vertex categories. Both programs are standalone Python 3 source files included with the result, and the exact successful stdout from each is supplied.

Run from this package directory:

```
python3 verify_full_tree_rank3.py
python3 check_tree_pair_profiles.py
```

The programs use no third-party dependencies. The rank-four twin-sentence observation is established combinatorially, not a claim of complete rank-four equivalence. No expert, independent, or externally certified verification is claimed.
