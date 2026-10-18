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

# Reproduction of finite checks

Run `python3 verify.py` in the same directory as these files. It requires the Python 3 standard library only.

The independent enumerator first assigns every singleton one of the nonempty output sets and extends the assignment by union. It discards maps not preserving the unit and then tests the defining material-implication identity on **every** ordered pair of nonempty inputs. It separately enumerates pointed functions satisfying the classification, calculates each output image cardinality and idempotence, and compares both data sets with the derived Stirling/binomial closed formulas.

Verified exact outputs:

| Ground set size | All endomorphisms | Idempotent endomorphisms | Image-rank multiplicities |
| --- | ---: | ---: | --- |
| 2 | 7 | 4 | 1:1, 2:4, 3:2 |
| 3 | 43 | 14 | 1:1, 2:18, 4:18, 7:6 |
| 4 | 393 | 64 | 1:1, 2:56, 4:216, 8:96, 15:24 |

The program ends with `VERIFY_OK` when all comparisons agree. These are **finite diagnostics only**; general correctness depends on the symbolic proof in `RESULT.md`. No automated formal proof or external audit is claimed.
