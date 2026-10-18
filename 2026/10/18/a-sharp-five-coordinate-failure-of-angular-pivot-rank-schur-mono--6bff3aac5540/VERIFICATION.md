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

Run `python CHECK.py` using Python 3 and only the standard library. All exact checks use `fractions.Fraction` and exhaustive finite permutations/subsets, never floating tolerances.

The program executed successfully on the included source, reporting 520 generic capacity profiles and 750 direct greedy-optimality versus vertex-maximization checks. It checks subset-sum tails, reversal symmetry, vertex normal-cone angles, all six five-capacity laws, the explicit majorization counterexample, both variances, and the low-dimensional dominant/non-dominant classification. Each explicit five-capacity example is nonresonant because the capacities are even but the central level is odd.

Analytical proof of the infinite claims appears in `RESULT.md`, not in the finite checker. No simulation certifies novelty; primary-literature comparison and remaining bibliographic risk are described in `REVIEW.md` and `AUDIT.json`. Independent audit is not performed.
