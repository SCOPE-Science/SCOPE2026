---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

At singular κ set μ=cf(κ) and choose increasing positive branch heights κ_i cofinal in κ. On level κ_j take the nodes from branches κ_i for i>j. Such nodes exist, the set of levels is unbounded, and each tail has size μ. For any j<k, a branch indexed by i>k meets both levels; comparison respects levels and two predecessors of a common node are comparable in the fan. The inherited relation therefore satisfies the subsystem axioms. The successor μ⁺ is regular in ZFC, so μ<κ singular implies μ⁺<κ. For nonexistence of a well-pruned subtree, every positive-level node is confined to its single bounded chain even in the induced subtree order (a subtree of one bounded chain still has order type less than κ). Any subtree of height κ contains a nonroot node. As a sharpness check, fewer than μ nodes on any fixed positive subsystem level would use fewer than μ branch heights, bounded in κ, and prevent comparisons with sufficiently high selected levels. The proof uses no computation. Its conclusion is about preserving the stated width convention at singular height, not about the existence of a different singular-height theorem.

## originality

PASS

Credit Adkisson for the fan, the definitions, the regular-height obstruction and the regular-height pruning theorem; bounded cones follow directly from the old fan. The distinct content is the cofinality-width subsystem and consequently the failure of the same narrowness condition to force pruning at singular height. The closest inspected text does not cover this construction; this is not a claim of absolute priority.

## value

PASS

The same natural test object at regular and singular height isolates exactly why the width hypothesis ceases to enforce pruning: the least width for a subsystem is cofinality, which satisfies the narrowness inequality at singular height. This gives a uniform counterexample to a specific hypothesis deletion in a structural theorem, rather than an arbitrary cardinal example. It does not settle possible replacement hypotheses or two-cardinal cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
