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

The complete proof is in RESULT.md. With Python 3, run `python3 verification/verify_card_shuffle.py`. It uses standard-library permutations, `fractions.Fraction` and floating-point recurrences.

The finite checks independently enumerate random shuffles for block counts two through eight and compare exact bond probabilities with the inclusion-exclusion formula, then verify exact factorial moments and rational mixed stopping-time moment recurrences through 23 blocks. Larger-size calculations are *approximations*, using a truncated expansion of the one-round bond law; these illustrate, but cannot certify, the infinite covariance limits. The final program output includes `PASS 159 checks`.

The proof specifically uses an earlier published stochastic domination result and provides the missing two-coordinate gap bound. Stopped-martingale isometry and Poisson arrival-time overshoot control make the probabilistic normalization rigorous. No independent mathematical audit was undertaken. Historic priority remains provisional because related older full text was not obtainable.
