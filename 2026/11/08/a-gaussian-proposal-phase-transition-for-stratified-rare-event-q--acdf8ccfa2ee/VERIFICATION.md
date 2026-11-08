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

# Verification and reproducibility

Run `python3 verify_rare_event.py` using only the Python standard library. The checker evaluates exact Gaussian cell-moment integrals numerically and tests the matched-proposal Bernoulli phase at finite grids, plus the proposed normalizations in representative underdispersed and overdispersed regimes. It produced `PASS: 634 tests; finite-grid Gaussian integral, Bernoulli phase and normalized variance checks` on the packaged script.

## Mathematical verification
The proof in RESULT.md derives the Gaussian likelihood ratio, Mills ratio and logarithmic endpoint coefficient, the exact positive-moment boundary, almost-sure and L1 convergence of the endpoint-centered series, L2 convergence where allowed, and the sharp series-tail constant. The jump-cell argument isolates the only asymptotically nonnegligible error for proposal variance at least one; uniform continuity of remaining cells gives their vanishing variance. These analytic derivations establish the infinite statements; computational checks do not establish limiting distributions by themselves.

## Scope and limits
The checker uses floating-point Gaussian cdf/inverse-cdf evaluations, so its numerical comparisons are not formal exact proofs. It cannot independently verify publication precedence or exclude general stratified-sampling theorems under different terminology. No independent scientific review has been performed.
