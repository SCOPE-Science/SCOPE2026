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

# Verification scope
Run `python verify.py` with Python 3.10 or later. No dependencies outside the standard library are needed. The checker constructs two-coordinate rectangle implications directly from word pairs, repeatedly applies those implications until fixed point, identifies Hamming-connected components, verifies that each component is a coordinate box, and compares closure with greedy box merges. For small cases it also checks every smaller-size generator fails and searches for optimal-size generators. It prints `VERIFY_OK` only if every assertion completes.

Actual verified output:
```
PASS (2, 2) points 4 tested_sets 16 minimum_generator 2 witness (0, 3)
PASS (2, 3) points 6 tested_sets 64 minimum_generator 3 witness (0, 1, 5)
PASS (3, 3) points 9 tested_sets 512 minimum_generator 3 witness (0, 4, 8)
PASS (2, 2, 2) points 8 tested_sets 256 minimum_generator 3 witness (0, 1, 6)
PASS (2, 3, 2) points 12 tested_sets 4096 minimum_generator 3 witness (0, 3, 10)
PASS (2, 2, 2, 2) points 16 tested_sets 65536 minimum_generator 3 witness (0, 3, 12)
PASS (3, 3, 3) points 27 tested_sets 800 minimum_generator 4 witness (0, 4, 11, 24)
PASS (3, 2, 4) points 24 tested_sets 800 minimum_generator 4 witness (0, 5, 10, 19)
PASS (2, 2, 2, 2, 2) points 32 tested_sets 800 minimum_generator 4 witness None
VERIFY_OK exact_closure=PASS canonical_boxes=PASS merging=PASS generator_lower_upper=PASS
```
The final `witness None` means that exhaustive witness search was intentionally disabled for the 32-point product; it does not report a negative mathematical result. The constructive proof in RESULT.md supplies a witness for all sizes. The 70,480 exhaustively checked subsets concern products of at most sixteen words; there are 2,400 additional deterministic samples on three larger products. The exact all-parameter theorem is proved mathematically, not inferred from these tests. No external audit has been performed.
