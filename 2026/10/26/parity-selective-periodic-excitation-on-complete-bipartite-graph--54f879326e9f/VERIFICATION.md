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

The complete proof uses a backward-in-time necessity for excitation events, the resulting period-two restriction on the two partwise excitation indicators, and exact one-vertex two-step return maps. The proof is valid for all integers \(q\ge3\) and \(a,b\ge1\); no finite experiment is used as a substitute for this quantification.

`verify_gh_multicolor.py` reconstructs the entire deterministic successor graph on each tested parameter triple, identifies cycles without imposing an expected period, and compares every recurrent configuration and its least period against the formula. `CHECKS.txt` is the direct output of running the checker, including its aggregate tested state count. The checker additionally tests the scalar forced-return cycles for \(3\le q\le64\) and explicit alternating-wave witnesses for \(7\le q\le15\).

Finite checks do not prove untested graph sizes or colors. No independent audit, formal proof assistant, or external certification is represented.
