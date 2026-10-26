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

# Verification record

The standalone, standard-library program `verify.py` computes \(K_4\)-freeness of every candidate two-point labelled extension directly from its full edge list, independent of the paper's intersection condition. It compares the direct count against the general triangle-free-neighborhood expression and, where bipartite, against the weighted independence-polynomial expression.

The script also builds independent-clone blowups, enumerates their independent subsets directly, evaluates at exact rational activities, and reconstructs the original independent-set count by Lagrange interpolation. All calculations are exact integers or `fractions.Fraction`, with no floating-point tolerances.

Run `python3 verify.py` in the directory containing this file. The packaged `verify.log` records the actual output:

```
GENERAL_K4_FREE_PAIRS 75
BIPARTITE_PAIRS 52
INTERPOLATION_INSTANCES 51
ALL_TESTS_PASS
```

The test range comprises every labelled \(K_4\)-free simple graph through four vertices and every bipartite labelled input through four vertices for the interpolation checks. These finite experiments corroborate but do not replace the proof covering all finite bipartite parameter graphs. No independent audit or external validation has been performed.
