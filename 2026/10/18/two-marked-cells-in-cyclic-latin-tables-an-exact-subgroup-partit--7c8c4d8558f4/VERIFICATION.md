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

The theorem is proved in `RESULT.md`; the finite checks are corroborating tests, not a substitute for the all-order equitability and automorphism-group arguments.

Execute from the directory containing this file using Python 3 and the standard library:

```
python verify/direct_refinement.py
python verify/equitability_and_orbits.py
python verify/autotopism_independent.py
```

The first program computes actual iterative, relation-wise colour signatures for each input and tests exact equality of whole stable partitions with the subgroup-coordinate prediction. The second program separately calculates all relation-wise neighbour-count vectors and direct modular-unit orbits. The third program independently enumerates arbitrary row/column/symbol permutations for all group tables of orders two through five, rather than assuming the affine automorphism formula.

Recorded standard outputs appear in the accompanying `.stdout` files and are subject to exact-byte embedding integrity checks. All three scripts completed without error during preparation. Finite enumeration is not claimed to prove the unrestricted \(n\)-quantified theorem. No independent scientific audit has been performed.
