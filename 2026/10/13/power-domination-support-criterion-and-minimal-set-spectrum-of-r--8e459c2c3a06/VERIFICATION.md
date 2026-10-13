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

The proof of the all-set and inclusion-minimal-set classification is symbolic and covers all integers \(m,n\ge2\); no finite computation is required for its validity. The independently coded finite check reconstructs graph adjacency and repeatedly applies the ordinary power-domination rule, without using the row/column support criterion to decide membership.

From a directory containing the companion file, execute `python3 verify.py`. It checks all \(107{,}654\) nonempty subsets across ten boards: all \(2\le m,n\le4\), plus \((m,n)=(3,5)\), compares power-domination membership, classifies each inclusion-minimal set, tests formulas for their numbers, and checks full cardinality polynomials by coefficientwise direct enumeration. Expected closing line:

`VERIFY_OK subset_checks 107654 power_sets 107194 minimal_sets 694 boards 2..4 plus 3x5 coefficient_cases 10`

This is finite verification only. It is not an independent audit and does not establish novelty. There is no extrapolation from finite cases; the general statements follow from the structural proof in `RESULT.md`.
