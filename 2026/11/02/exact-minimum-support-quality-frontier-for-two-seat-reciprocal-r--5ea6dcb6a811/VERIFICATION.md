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

# Verification performed

The complete standalone `verify.py` in this package was executed with Python 3 and exact integer and rational arithmetic. Observed output:

```text
VERIFY_OK exhaustive_profiles=434161 quality_optimal_profiles=433063 equality_profiles=112746 exact_canonical_pairs=870
```

The checker implements the strict rJR blocking criterion, exhaustively examines specified small approval profiles and quality grids, tests the guaranteed ratio, checks a single-replacement repair from a top-quality pair, and evaluates exact sharpness on canonical three-candidate elections across a parameter range. Small-profile enumeration is not an exhaustive proof for arbitrary voter populations or real qualities; the algebraic proof in RESULT.md covers those cases. The checker also exercises previously known boundary examples, without treating them as a new contribution.

No independent scientific audit has been performed.
