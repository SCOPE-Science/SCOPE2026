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
# Verification summary

The core universal proof is the Beta integration-by-parts induction, followed by coefficientwise nonnegativity of \(P_X(1-1/\alpha+z/\alpha)\) and an exact negative coefficient below the boundary. Independent validation has not been performed.

Run `python3 check_beta_binomial.py` using Python 3 standard library only. The exact-rational check covered \(n=1,2,\ldots,8\) and all 36 pairs of shape values in \(\{1/3,1/2,1,2,5/2,3\}\), totaling 288 cases. Each case verifies: normalization and positivity of inverse-PGF coefficients at the predicted threshold; exact zero of the degree-\(n-1\) coefficient; negativity of that coefficient at \(99/100\) of the predicted threshold; reconstruction of all beta-binomial masses by forward thinning.

Finite tests are neither an exhaustive real-parameter proof nor a guarantee of originality. Scientific limits and closest literature comparisons are recorded in the mathematical result and review.
