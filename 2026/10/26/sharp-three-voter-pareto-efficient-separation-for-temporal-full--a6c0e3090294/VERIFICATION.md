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

The three triggers and the FJR and EJR+ quantifiers match the cited definitions. In the witness voter 3's maximum satisfaction fixes every chosen candidate; group {1,2} violates only the cohesion equality trigger for target one. It has no common approved candidate, and its singleton subgroups have cohesion entitlement zero. FJR has benchmark zero for those singletons (pick an empty-approval round at full horizon); for the pair, a one-round choice cannot satisfy both, and for the full horizon the two identical first rounds witness benchmark zero. With two voters, a non-maximal supporter count is Pareto-dominated roundwise, so the grand-coalition score is maximal; singleton FJR+ triggers are covered by EJR+. For three voters and at most two rounds, singleton triggers cannot occur; pair triggers require two unanimous pair rounds, hence EJR+ protects target one; a grand-coalition violation would require all-zero satisfaction at target one or two unanimous rounds at target two, both inconsistent with Pareto efficiency and the trigger. For one candidate the maximal total support equals actual total satisfaction on every group. Independent witness evaluation and 1056 reduced profile/outcome checks agree (python /workspace/independent_checks.py 2). The short-domain replay reduces arbitrary candidate sets to maximal supporter masks: dropping smaller masks preserves common-approval availability, per-round support maxima and Pareto comparisons, and no Pareto-efficient outcome chooses such a smaller mask.

## originality

PASS

The qualitative Pareto-efficient separation is prior. The distinct result is the sharp three-voter obstruction with the simultaneous short-horizon/candidate minima, plus the underlying universal Pareto-efficient EJR+ implication at smaller sizes.

## value

PASS

This locates exactly where the qualitative strengthening becomes observable under Pareto efficiency in the standard permissive model. The small witness isolates cohesion equality, and the arbitrary-horizon two-voter implication explains why an even smaller electorate cannot separate the axioms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
