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

Execute `python verify.py` using Python 3 and no third-party dependencies. The program enumerates all increasingly labeled rooted trees through six vertices; checks every function from each tree to each reflexive fan of sizes three, four and five worlds (that is, two, three, and four maxima); and tests the forth/back requirements from transitive descendant sets. Separate enumerators count valid leaf colorings and recurrence values. Assertions cover the root-degree threshold, exact star-equality classification, unique ternary vertex formula and the collision of two nonisomorphic full-binary trees with four leaves.

Recorded exact output is in `verification_output.json`. The expected status is `ALL_CHECKS_PASS`. 462 independent direct function-enumeration comparisons, 462 branching-threshold comparisons, 134 sharp-extremizer checks and 55 ternary-depth formula checks passed.

These finite tests are consistency evidence only. They neither establish novelty nor prove universal quantification; the mathematical proof appears in RESULT.md. No separate scientific auditing entity has certified this result.
