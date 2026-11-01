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

# Verification evidence and scope

The proof is symbolic. Its critical steps are the ordered-coordinate support formula, the complete signed-subset halfspace representation, the one-peaked partial-sum-over-square-root lemma proved using log-concavity and Bernoulli's inequality, and direct facet-dimensionality arguments. All necessary definitions and boundary cases are in `RESULT.md`.

`checks/verify.py` uses only the Python standard library. It was run from the actual embedded program's bytes after construction. The observed pass output consists of 5,040 support formula comparisons, 1,113,626 exact-integer squared-distance inequalities, and 11,026 correct endpoint-phase classifications, with \(3\le k\le n\le150\) for the latter two groups. Each of these tests is finite and cannot by itself establish the quantified all-integer theorem. No independent mathematical audit has been performed.
