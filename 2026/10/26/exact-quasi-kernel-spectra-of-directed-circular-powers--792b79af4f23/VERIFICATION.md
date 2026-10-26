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

The source program `verify_quasi.py` (Python 3 standard library) independently builds the directed circular power, directed reachability within two arcs, and exact independent vertex subsets. For all 90 parameter pairs with \(3\le n\le14\) and \(1\le k<n\), it compares directly enumerated cardinality counts with a separate inclusion-exclusion computation. Run `python3 verify_quasi.py`. Actual observed result: `VERIFY_OK exhaustive_circulant_cases=90`.

This is finite computational validation only. The unrestricted theorem is supported by the complete clockwise-gap proof in `RESULT.md`. It has not undergone an independent mathematical audit, and broad historical-priority verification is incomplete.
