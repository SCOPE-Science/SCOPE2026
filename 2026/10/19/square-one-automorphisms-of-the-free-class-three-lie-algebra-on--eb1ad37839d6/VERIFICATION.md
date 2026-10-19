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

# Reproduction

Run `python square_one_check.py` with Python 3 and no third-party dependencies. It independently enumerates all automorphisms from their generator images over prime fields of orders two and three, then checks all permissible square-one linear blocks and all lifts over the degree-two extension field of order four. Full \(5\times5\) matrix squaring is used for the elementwise test.

Expected output:

```
q 2 total 40 expected 40 distinct fibers [0, 8, 16]
q 3 total 334 expected 334 distinct fibers [0, 1, 9, 27]
q 4 total 1216 expected 1216 distinct fibers [64, 256]
```

The symbolic proof in `RESULT.md` is required to establish the theorem for every prime power; finite enumeration alone does not prove an infinite family. No independent mathematical audit has been performed.
