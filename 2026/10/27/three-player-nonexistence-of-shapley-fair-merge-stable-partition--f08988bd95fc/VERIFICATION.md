---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n=0 or 1 the natural partition works. For n=2, if the merge surplus is nonpositive the singleton partition works; if positive each player's Shapley gain over the singleton is exactly half that surplus. For n=3, independent exact subset-weight calculations (python3 /workspace/checks/check124.py, record 1) gave singleton payoffs (2,2,0), pair payoffs (5/2,5/2), (1,-1), (1,-1), and grand payoffs (19/6,19/6,-1/3). Both fair partitions have a strict gain of 1 from a merge; the other three are unfair. The split phase does nothing at {12,3} and the unique legal merge takes it to {123}, strictly lowering the vector from (0,5) to (-1/3,6). At {123} the residual {12} is fair, so the next composite returns to {123}; in separate split and merge steps this is a two-cycle. No tie or update-order assumption is needed here. Zhu–Han's primary §§3.1–3.3 use this operator and Lemma 3 asserts the disputed conclusion under nonnegative singleton values. Theorem 2 conditions on monotonicity separately and is not refuted. Coalition values here are all nonnegative but not monotone.

## originality

PASS

The best-supported distinct result is the minimal three-player failure of SFMS, with all coalition values nonnegative, and the consequent explicit refutation of monotonicity for the exact Zhu–Han composite. The definition, operators and proposed potential themselves are prior material.

## value

PASS

This is a sharp failure boundary for an existing proposed solution concept and a counterexample to a concrete convergence argument, not just a generic cycling example. The all-nonnegative witness isolates the missing control on fairness at a strict surplus merger even with no negative coalition worth.

The dated certificate retains the supplied scientific assessment, sources and limitations.
