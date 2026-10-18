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

# Verification evidence and limits

The analytical proof begins with three exact first-jump equations on orbit types leaf/hub, hub/leaf, and distinct leaves, solving for the leaf/hub expected collision time in the two jump-rate conventions. The two rational formulas and their differences have the stated positive denominators. Their derivative numerator polynomials are strictly decreasing over positive mobility ratios for every integer star degree at least two. Positive polynomial identities prove the uniform upper bounds on their maxima and the explicit ratio \(m^{-1/2}\) attains both asymptotic constants.

The accompanying standalone `verify_star.py` is executable with standard Python 3. It enumerates every ordered off-diagonal two-particle configuration, constructs the original full absorbing continuous-time generator without orbit lumping, solves the first-step equations with exact rational arithmetic, and compares its initial-state mean to the claimed formulas. The delivered code was executed and passed 40 exact formula comparisons and 880 individual first-step equations for two to six leaves and four rational mobility choices, including a stationary trap, in both mobility conventions. This is finite corroboration, not an infinite numerical certificate.

No externally performed independent audit exists. Exhaustive novelty verification, other graph families, alternate initial laws, stochastic dependence, and full encounter-time distributions are outside the checks.
