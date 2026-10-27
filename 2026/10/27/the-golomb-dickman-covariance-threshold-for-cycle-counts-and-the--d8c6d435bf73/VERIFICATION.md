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

The proof is deductive: the cycle containing a fixed label has uniform size; marking a \(j\)-cycle produces the complementary uniform permutation; and a standard insertion of a new label cannot shorten the maximum cycle. The inequalities in RESULT.md cover every admissible integer parameter, without relying on experimental ranges.

The standalone standard-library verifier `check_cycle_max.py` computes exact cycle decompositions for all permutations with \(1\le n\le8\), checks the expectations and covariances against the marked-cycle formula, and independently computes finite \(\Pr(M_n\le k)\) by the uniform-tagged-cycle recurrence. The executed `check_results.txt` reports 36 exhaustive covariance comparisons and 1,829 exact-rational sign/identity/bound checks for \(2\le n\le60\), plus larger finite-case diagnostics at sizes 100 and 140.

These calculations are finite diagnostic checks and not independent validation of the infinite claim. The Golomb–Dickman asymptotic is taken from the cited classical paper. No arbitrary Ewens parameter or conditional stochastic ordering is asserted. Independent audit has not been performed.
