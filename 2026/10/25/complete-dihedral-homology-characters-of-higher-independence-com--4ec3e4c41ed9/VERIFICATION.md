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

The standalone, standard-library-only script `check_characters.py` was executed from the actual source artifact with the command `python3 check_characters.py`, producing:

```text
PASS 1200 exact signed fixed-face character comparisons
PASS 18 independent modular simplicial boundary calculations
example 2 6 rotations [1, -1, 1, -1, 1, -1] reflection types [-1, 1]
example 2 8 rotations [3, 1, -1, 1, 3, 1, -1, 1] reflection types [1, 1]
example 3 10 rotations [4, 1, -1, 1, -1, -4, -1, 1, -1, 1] reflection types [0, 0]
```

The script's direct orbit enumerator does not call either character formula to compute its comparison trace. Its modular chain complex independently verifies small finite-dimensional homology groups over \(\mathbb F_{101}\). The all-parameter claim rests on the proof in `RESULT.md` and the previously established integral sphere-wedge theorem, not on finite enumeration. No independent external audit was performed. The claimed representations are rational, not integral lattices.
