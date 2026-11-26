---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Starting with the two Euler stages gives the claimed P_r and the physical interval [0,1-1/r]. For x>0 its sign is the sign of g_r(1-x). The discriminant is r^6(r^4-18r^2-27); on [0,1] the only stationary point that can become a zero is the local minimum, since the maximum exceeds g_r(0)=1. Its sign is initially positive and eventually negative, and g_r>=1 on [0,1/r]. This gives the tangency and both negative-interval endpoints in the physical domain. Independently the factor of P_r-c_r stays positive throughout that domain for r<=r_*: the bounded quadratic on 0<=rx<=1 is strictly below 2 and the expression on 1<=rx<=r-1 is at most 1. Fixed-step induction gives the all-iterate statement. The rescaling y-y_*=s z, r-r_*=s^2 gives simple limiting roots because g_r's parameter derivative is negative and its state curvature positive. The negative minimum is inside that shrinking interval; the local minimum branch of P_r is smooth at the tangency and has the claimed derivative. The ever-present zero at x=0 cannot compete just above onset.

## originality

PASS

Credit the published Heun polynomial and the numerical positivity-loss observation near 4.4037. The distinct supported claim is the exact global physical-interval iff, including the separate upper boundary, together with the two sharp local onset laws for the forbidden inputs and their minimum output. Neither the closest primary passages nor the related corpus findings checked give those statements or their quantified conclusion.

## value

PASS

The full carrying-capacity range is canonical, and practical fixed-step control requires a uniform interval guarantee rather than a test of a stable or typical orbit. The exact threshold excludes steps that fail immediately, and the width and depth quantify how much initial data is affected and how far it leaves the physical range near failure. The contribution is not the already reported approximate location or the general existence of a fold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
