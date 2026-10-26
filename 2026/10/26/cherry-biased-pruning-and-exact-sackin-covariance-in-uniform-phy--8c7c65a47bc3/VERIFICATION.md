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

# Reproducibility and limitations

Run `python3 verify.py` using standard Python (no third-party packages).

Observed result:

```
PASS: 8 exhaustive plane-tree sizes (2..9), 48 Palm-histogram bins; 11464 exhaustive labeled trees (2..7), 200 exact algebra recurrences.
```

The program independently enumerates ordered shapes and unordered leaf-labeled trees, compares exact mixed moments, checks every value in the cherry-size-biased Sackin probability-mass identity for the enumerated sizes, and verifies central-binomial coefficient recurrences and the exact sign test using rational arithmetic.

All finite calculations are finite checks only. The proof for unbounded tree size is the marked-cherry contraction bijection, the full-binary-tree generating-function derivation of the known mean, the exact algebraic reduction, and the strict ratio inequality. No numerical or program output certifies the infinite theorem on its own. Scientific limitations appear in `RESULT.md`.
