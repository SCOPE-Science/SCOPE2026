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

Run `python3 verify.py` with Python 3.9 or later, with no third-party dependencies. The program tests every partial transformation on stars with 2, 3, 4, and 5 leaves against the inverse-face definition, compares rank, nonregularity, and idempotent distributions with the closed formulas, and checks constructed generalized inverses for all classified regular maps. On the two- and three-leaf stars it additionally searches all pairs of continuous maps to independently verify the exact regularity criterion. The expected final output is `VERIFY_OK`.

The finite checks use a different direct face-test implementation, but are not exhaustive for unbounded `n`; the general case follows from the proof in `RESULT.md`. No independent audit has been performed.
