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

# Reproducibility

Run `python verify.py` with Python 3 (standard library only) from the directory containing this file. A completed run produced `PASS: 280391 labelled trees; 264 exact rational moment/count/phase comparisons`. The program enumerates all Prüfer sequences for each size 3 to 8 and computes path sets and leaf counts without relying on the rooted-forest extension argument.

The analytic argument in RESULT.md, not this finite enumeration, establishes the result for all allowed sizes and factorial orders. A standalone independent audit has not been performed. The verified scope excludes nonuniform trees and the separate two-vertex degenerate case.
