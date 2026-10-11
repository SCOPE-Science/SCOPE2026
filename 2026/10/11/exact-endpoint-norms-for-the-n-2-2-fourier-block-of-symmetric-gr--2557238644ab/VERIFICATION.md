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

Running `python3 verify.py` with Python 3 and the standard library prints:

```
VERIFY_OK exact_character_classes=28622 permutation_objects=46224 n=4..30
```

The verifier re-counts all conjugacy classes of \(S_n\) for \(4\le n\le30\), checks their integer cardinalities, the zero character average, unit character second moment, exact negative support, and the equality of the character-total-variation and associated-derangement formulas as rational numbers. It additionally enumerates all permutations for \(4\le n\le8\) and tests the cycle criterion independently. The computation does not prove any statement for untested \(n\), nor does it substitute for the character-theoretic and combinatorial arguments in the proof. There is no independent audit.
