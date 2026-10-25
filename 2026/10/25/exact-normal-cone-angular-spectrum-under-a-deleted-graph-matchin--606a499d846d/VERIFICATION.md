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

# Verification evidence

Run the included standalone program `python VERIFY.py` using Python's standard library. It exhaustively enumerates rank permutations for all \(4\le n\le8\) and all matching sizes, with exact rational probabilities, including the equiprobable extreme-gap competition. Observed output:

```
EXACT_ANGLE_PASS cases=19 permutations=225072 edge_checks=304 symbolic_n_max=300
```

It additionally verifies the exact angle normalization and class multiplicities for dimensions from four through 300. Gaussian spacing reflection, reduction to two feasible extreme competitors, and the proof for arbitrary dimension are established analytically in `RESULT.md`, not by the finite enumeration. No independent mathematical audit has been conducted.
