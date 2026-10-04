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

The theorem is proved analytically in `RESULT.md`. Verification separates the logical proof from finite algebra checks.

1. The exact transformation from the central F CDF to the regularized beta CDF is the formula used in the lead source. At the scaled mean it gives \(q_\kappa(a,b)=\kappa a/(\kappa a+b-1)\).
2. The source's Theorem 1.1 and Section 2.1 were checked for the premise \(P_1(a,b)>1/2\) at every finite integer-degree pair.
3. For one-coordinate escape, the beta density after the rescaling \(u=y/b\) converges to the Gamma density; reflection gives the second boundary limit. All limiting thresholds are positive continuity points.
4. For joint escape, the proof computes the exact beta mean, variance, and threshold displacement and obtains a lower bound proportional to \(\min(a,b)\); Chebyshev then forces the upper-tail error to zero.
5. `verify.py` uses exact rational arithmetic to replay the threshold-displacement identity and its lower-bound chain on a representative grid. It returns `VERIFY_OK`. This finite replay is an algebraic safeguard only and is not evidence for the asymptotic quantifiers.

No numerical table, timeout, or failed search is used as a correctness certificate. The originality conclusion remains subject to the explicit residual literature-search risks recorded in `AUDIT.json`.
