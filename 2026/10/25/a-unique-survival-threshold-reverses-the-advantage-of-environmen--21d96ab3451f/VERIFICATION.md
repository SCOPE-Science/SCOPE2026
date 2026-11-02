---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Each A_i strictly positive with two distinct positive eigenvalues because det A_i=s(cu1x_i+bu2y_i)+s²bc>0, and λ_i>sc. The rank-one secular equation 1=u1x_i/(λ_i−sb)+u2y_i/(λ_i−sc) uniquely defines λ_i. Equality λ0=λ1=L implies L−sc=R(L−sb), R=u2Δy/(u1Δx)∈(0,1), giving exactly the displayed s*>0; small-s λ0>λ1 whereas large-s λ1>λ0. Right Perron ray determinant has sign(λ0−λ1), while the left ray ratio z_i satisfying the derived positive-root quadratic is increasing in x and decreasing in y, so det[ℓ0,ℓ1]>0. The 2×2 spectral projector identity tr(P0P1)−1=−det[r0,r1]det[ℓ0,ℓ1]/[(ℓ0·r0)(ℓ1·r1)] converts the characteristic polynomial evaluation at λ0λ1 to sign(λ0λ1−ρ(A0A1))=sign(λ0−λ1). Hence unique strict change. At s*, both matrices share w and Λ*; positive componentwise comparison αw≤z0≤βw propagates through arbitrary switching products, proving common asymptotic rate. The long-block limit follows from rank-one Perron projectors. Independent exact example s*=28/45, Λ*=49/15, w=(9,10) and signs at s=1/4,1 were checked, not used as infinite proof.

## originality

PASS

Prior demographic stochastic-environment and matrix-product sensitivity studies establish qualitative dependence on temporal correlation, spectral theory, and rank-one correction machinery. Their read statements do not specify the exact one-crossover threshold for this additive rank-one-plus-common-diagonal two-stage pair or its every-switching order-indifference at equality. No broad Markov-autocorrelation claim is made.

## value

PASS

A uniquely determined switching advantage reversal in a natural two-stage population matrix family is biologically and mathematically interpretable. The common Perron ray at crossover gives a stronger exact arbitrary-order growth invariance than equal rates for two named periodic schedules; it is a structural boundary, not a synthetic numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
