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

# Verification

Run `python verify_edge_degree.py` using standard Python 3. The verifier enumerates labeled subsets of the \(ab\) possible cross-edges of the correct cardinality and independently tests acyclicity/connectedness. It constructs exact rational joint distributions, partitions by membership of the marked edge, and verifies against the two theoretical binomial and mixture laws.

The executed checker printed:

```
EXACT_PASS K_{2,2} 4 spanning trees
EXACT_PASS K_{2,3} 12 spanning trees
EXACT_PASS K_{2,4} 32 spanning trees
EXACT_PASS K_{3,2} 12 spanning trees
EXACT_PASS K_{3,3} 81 spanning trees
EXACT_PASS K_{3,4} 432 spanning trees
EXACT_PASS K_{4,2} 32 spanning trees
EXACT_PASS K_{4,3} 432 spanning trees
EXACT_PASS K_{4,4} 4096 spanning trees
VERIFY_OK 5133 labeled spanning trees in nine parameter pairs
```

The infinitely many larger parameter cases and limiting correlation are established by the written matrix-tree/electrical and binomial proof, not by finite enumeration. No independent audit was performed.
