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

The file `verify_adjacent.py` was executed from the completed finding's standalone checker. It independently constructs every adjacent unequal-swap edge and a maximum matching to compare the exact independence cardinality against the analytical answer; it also checks all fixed-composition parity counts. The recorded output was:

```
ADJ_SWAP_VERIFY_OK cases=22 vertices=6689 parikh_profiles=309 formula_and_maximum_matching=True
```

Tested domains: binary lengths 1–10, ternary lengths 1–7, quaternary lengths 1–5. The mathematical proof does not depend on any finite enumeration; no independent audit has been performed.
