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

# Verification record

The complete proof is in `RESULT.md`, using normalized weighted area moments, angular-channel diagonalization and exact adjacent-ratio factorization. Every denominator in the displayed squared-channel and difference formulas is strictly positive for the stated ranges, including the boundary channel at index one. A nonnegative polynomial identity proves the comparison with the linear anti-analytic symbol. The positive threshold roots form a strictly increasing sequence; consequently finite spectral tests are not substituted for the proof of the infinite staircase.

`checker.py` is a standalone Python 3 standard-library script. Run `python3 checker.py` in this package to repeat exact rational moment-ratio checks and maximal-index comparisons. On this review it passed 29,904 exact rational identities/comparisons and asymptotic checks. All finite numerical checks are corroborative and do not certify statements about all weights or all indices. This package does not independently settle historical priority in any inaccessible paper.
