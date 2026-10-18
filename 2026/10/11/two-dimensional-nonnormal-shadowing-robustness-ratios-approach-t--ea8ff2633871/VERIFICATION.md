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

Spectral projections P_s=[[1,K/2],[0,0]], P_u=[[0,−K/2],[0,1]] yield an absolutely convergent unique bi-infinite Green inverse since 0<1−epsilon<1 and −1−epsilon<−1. An explicit unit forcing gives Shad≥K/epsilon, while componentwise geometric sums give Shad≤(K+2)/epsilon. For |z|=1 the resolvent off-diagonal denominator |z−(1−epsilon)||z+(1+epsilon)| has squared value concave in Re z, minimized at z=−1 and equal to epsilon(2−epsilon). Resolvent maximum is K/[epsilon(2−epsilon)]+O(1/epsilon); thus product limit 2−epsilon. At epsilon=1/4 K=8 exact lower bound 56/39 exceeds sqrt(2). Independent rational arithmetic corroborated endpoint comparison, signs and finite witness; limiting theorem is analytic.

## originality

PASS

Yuan 2026 full primary HTML text states sharp sqrt(2) upper bound for NORMAL hyperbolic operators and asks about quantitative nonnormal behavior; this nonnormal two-dimensional upper triangular counterexample is outside that theorem. General Green inverse and stability radius identities are known, but do not alone imply this explicit sharp family ratio or finite violation. Scalar higher-order Ulam papers use a different norm/one-sided setting. Morales–Nguyen 2023 general shadowing paper was accessible at abstract/preview only, so its possible similar nonnormal example is a genuine residual risk, not grounds for automatic O failure.

## value

PASS

This explicit 2×2 diagonalizable nonnormal family supplies a natural sharp boundary to the cited normal-only sqrt(2) theorem and quantifies the role of nonorthogonal stable/unstable projections. Limit 2−epsilon and a certified finite strict violation resolve a motivated minimal-dimensional question without claiming an unproved universal upper bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
