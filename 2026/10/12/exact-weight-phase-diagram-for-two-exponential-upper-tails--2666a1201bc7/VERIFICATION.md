---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Convolution gives T_t(r)=e^(−t)[r e^(−t/r)−e^(−tr)]/(r−1), with equal/sparse limits e^(−2t)(1+2t) and e^(−t). Direct differentiation reduces derivative sign to h_t; on x=t(r−1) below critical 1−u sign equals that of L_t(x), whose exact derivative factors as x²[(t−1)x²+t(2t−3)x+t²(2t−3)] /[(t+x)²(1+x)(t−(t−1)x)]. For t≥3/2 all coefficients nonnegative so strict increasing weight imbalance; for 1<t<3/2 the quadratic has exactly one positive root giving one interior strict minimum. Endpoint comparison gives tau unique in (1,3/2). Independently checked both derivative identities symbolically (residual zero), endpoint and dense grid examples t=1.05,1.2,tau,1.35,1.499,1.5,2; finite grid only corroborates the analytic sign proof.

## originality

PASS

The Bock–Diaconis–Huffer–Perlman 1987 and Yu 2017 gamma-convolution results establish pairwise majorization/crossing and tail-region Schur comparisons. Those known statements and the published local equal-weight curvature threshold do not state the entire pointwise two-weight global optimizer classification, interior minimizer and distinct tau crossover. Strong equivalent possible in older gamma-convolution full text: Oxford institutional attempt timed out, so prior-coverage uncertainty is material.

## value

PASS

The exact global weight-optimization phase diagram is a natural probability/concentration problem; it distinguishes an interior minimum from equal/sparse maxima and resolves two distinct transitions, not just a standard gamma convolution identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
