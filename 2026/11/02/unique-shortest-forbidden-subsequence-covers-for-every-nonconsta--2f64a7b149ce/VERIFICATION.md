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

Run `python3 verify.py` in a directory containing this document's companion file. It uses Python's standard library and enumerates the permitted target language directly, without calling the proof's formulas to decide whether an individual target occurs in its proposed cover.

For each binary forbidden word of length three and each target length \(3\le k\le12\), the checker tests the exact proposed host for forbidden-pattern avoidance and for scattered containment of every permitted length-\(k\) target. These loops perform 65,472 individual target checks. In a logically separate breadth-first enumeration of candidate hosts through their greedy-subsequence progress vectors, for \(3\le k\le7\), it verifies all 40 shortest lengths and the fact that each has exactly one optimum. The two unary forbidden classes are extra controls, not part of the new theorem. Expected terminal output: `VERIFY_OK coverage_instances 65472 BFS_instances 40`.

The machine checks do not establish the result beyond their finite ranges; the infinite proof in `RESULT.md` provides the critical run decomposition, lower bounds, construction and exhaustive target cases. The script and its results are not an independent mathematical audit.
