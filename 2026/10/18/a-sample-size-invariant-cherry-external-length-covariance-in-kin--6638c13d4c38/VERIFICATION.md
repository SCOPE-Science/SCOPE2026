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

# Reproduction and limits

Run the standalone Python standard-library script `python verify_covariance.py`. It performs exact-fraction dynamic programming on the pair-merger process, independently accumulating expected external lengths and cherry counts without inserting the proposed cross-covariance into the program. It verifies all sample sizes \(4\le n\le23\), the known cherry variances, and every intermediate-stage covariance for \(4\le n\le13\). The expected output ends in `PASS` followed by `STAGE_PROFILE_PASS`.

The proof in `RESULT.md` establishes the whole unbounded integer range: it derives the singleton factorial moments, the two-singleton cherry survival probability, a mixed-moment recursion with verified closed-form solution, and the exact finite summation. Fraction arithmetic rules out rounding error in the computational checks; finite comparisons alone do not prove the theorem. The asymptotic correlation also uses published formulas for marginal variances.

No independent audit has been performed. Uninspected portions of potentially related older literature remain an originality risk.
