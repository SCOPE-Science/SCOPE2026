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

# Reproducible checks

Execute the standard-library-only `check_kneser.py` with Python 3.11 or later:

```sh
python check_kneser.py
```

A successful run ends with `KNESER_DIAMETER_THREE_NEGATIVE_TYPE_CERTIFICATE_OK`. The script constructs all vertices and relevant orbital matrix actions for three small instances, independently verifies Kneser graph distances by breadth-first search, checks rational inequalities over 173 family parameters, and computes high-precision critical roots and competing harmonic signs for eight selected parameters.

These are supplementary finite checks. The proof in `RESULT.md` establishes the infinite family using exact Johnson eigenvalue formulas and elementary uniform analytic estimates; exhaustive testing over all \(k\ge8\) is neither claimed nor needed. The source comparisons are literature-bounded, and no independent external validation has been performed.
