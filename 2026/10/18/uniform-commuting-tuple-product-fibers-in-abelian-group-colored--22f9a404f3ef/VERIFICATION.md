---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Use the vector of block ranks of a point in the r factors. Row-major and column-major products disagree exactly when two rank pairs cross strictly, because their intersection blocks then occur in opposite order. Consequently pairwise commutation makes all occurring rank vectors comparable coordinatewise, and their order is the lexicographic order of the iterated product. Each factor is a consecutive merging of the fixed product blocks. Conversely such mergings commute, and their product is the target iff every adjacency carries at least one cut. For abelian colors the order of multiplication on an intersection does not matter. Over a fixed cut pattern, the first output color leaves r−1 free labels; each next color leaves |S|−1 free new labels and uniquely determines the remaining new one. This verifies the weighted product, independent of block sizes or color choices. Summing over g^m m! times Stirling(n,m) targets verifies the EGF as a formal series and the total. The cases r=1, m=1 and g=1 give respectively u₁^m, the single group-product constraint, and uncolored cut masks. Independently generated small fibers, including C₄ and C₂×C₂ at n=2, corroborate the proof; the separate bounded checker is /workspace/branches/141f4ed3-ef6a-4545-ad36-27affc9748a8/independent_ordered_partition_check.py. The uploaded checker was inspected, not rerun.

## originality

PASS

The identical monoid and uncolored face/refinement structure are known. The g=1, r=2 total is numerically covered with its Stirling formula. Neither the closest primary results inspected nor the closest indexed product-fiber analogue accounts for the actual target colors and the joint block counts of arbitrary commuting tuples in this monoid. The distinct claim is the colored, prescribed-element, simultaneous enumeration.

## value

PASS

The target-conditioned joint polynomial is a natural exact invariant of the colored monoid. It gives the full joint block-count distribution, not just pair totals, and shows that dependence on target block sizes, labels and abelian group type disappears. The factorization explains precisely which data the statistic retains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
