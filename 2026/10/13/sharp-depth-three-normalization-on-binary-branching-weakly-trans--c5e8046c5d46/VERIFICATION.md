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

# Verification of the sharp depth-three reduction

Run from the directory containing the artifact:

```
python3 verify_depth3.py
```

The script requires only Python 3 with standard-library `itertools` and `collections`. It first enumerates every labeled directed graph on one, two, and three worlds, including loops, then filters by outdegree at most two and the exact universal weak-transitivity test. It groups under every world permutation, asserts that all labeled graphs have a canonical representative, and independently checks the resulting labeled and unlabeled counts. For every ordered representative pair and every set partition of at most six worlds, it computes atomic-color-and-successor depth signatures through depth four, asserting that the depth-three equality partition equals the depth-four equality partition. It checks a sharpness witness directly.

Replayed output:

```
PASS: all 320315 paired-frame/atom-partition cases stabilize by depth 3
Labeled admissible frames: {1: 2, 2: 16, 3: 159}
Unlabeled representatives: {1: 2, 2: 10, 3: 37}
Refinements in cases: depth 1 = 291034, depth 2 = 27989, depth 3 = 68
Sharp witness: depth 2-equivalent but Diamond^3 top separates
```

**What this establishes.** Each pointed generated model on the target frame class has at most three worlds, and every pair of atomic truth-vector assignments has one of the enumerated equality patterns. The exhaustive finite checks therefore cover infinitely many larger frames by a mathematical reduction, not by extrapolating sample data. Stability at step four forces stability at every later step by determinism of the signature recurrence. Standard characteristic formulas turn this stability into the asserted syntactic normalization.

**Limits.** A code run is not independent expert review. The conclusion relies on the correctness of the local-frame reduction, on the set-partition representation of atom vectors, on the complete finite loops, and on the standard characteristic-formula argument. No result about modal formula length or other modalities is being checked.
