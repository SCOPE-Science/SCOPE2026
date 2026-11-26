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

The pair-only word is uniformly distributed and the event of no second discovery through j counts the two monochromatic prefixes (restrict to j>=1). Pascal's identity gives the nonnegative difference in survival numerators C(a-1,j-1)-C(b,j-1). A quantile coupling of the second discovery times followed by the correct conditional words preserves both marginals. A common independent pair/rest interleaving and identical sequence of other individuals then order every prefix at once; uniform labeling within species recovers the full uniform permutations. At fixed m and j only one-to-two pair richness can change, so the event at threshold r changes only when the other-species richness is r-2, giving the displayed W kernel. The exact expectation follows by subtracting the two affected absence probabilities; its numerator is strictly positive precisely when 1<=m-1<=N-b-1. This includes the stated m=0 and full-census conventions. For integral majorization, sort both profiles, transfer from the first surplus to the first subsequent deficit (at least two apart in abundance), and resort. Prefix inequalities persist and the sum of squared abundances decreases, so a finite chain reaches the target. Conditional gluing of the adjacent whole-curve couplings is valid on these finite path spaces. The read-only checker uses exact DP/subset counts and binary words to corroborate finite cases, not to prove the path theorem.

## originality

PASS

One-size hypergeometric richness, mean rarefaction, and majorization under iid sampling are background. The supported distinct result is finite-census ordered whole paths with exact upper-tail gains, not the classical expectation formula or a PMF single-crossing claim.

## value

PASS

Whole-path order controls all richness discovery times in the same joint experiment. The one-transfer construction even confines the simultaneous path difference to 0 or 1, and the exact gain localizes how a one-unit balancing changes threshold probabilities. This is more informative than comparing means or separate one-size samples, while staying within uniform finite-census sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
