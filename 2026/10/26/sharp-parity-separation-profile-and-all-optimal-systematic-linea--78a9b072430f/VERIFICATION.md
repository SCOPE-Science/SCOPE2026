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

The elementary reduction of code distances to distinct sum-free check columns is proved in `RESULT.md`; the all-dimensional upper bound invokes the published Davydov--Tombak structural theorem as quoted in Reiher (2025). No finite computation is taken as an infinite proof.

Reproduction from the packaged `verify.py` uses only Python's standard library: `python3 verify.py`. Exhaustive searches in check dimensions three, four, and five give maximum column counts 1, 5, and 11 with 1, 1, and 6 labeled optimum sets, respectively. Constructive column sets in dimensions five through nine and every message difference in the maximizing dimension-three through dimension-five examples are checked. The expected terminal line is `VERIFY_OK` and the captured execution is in `verify_output.txt`.

Unverified extensions: nonsystematic or nonlinear encoders, other target functions or distance thresholds, and direct reproduction of the historical Davydov--Tombak theorem. The source-comparison record notes relevant papers whose full text could not be obtained.
