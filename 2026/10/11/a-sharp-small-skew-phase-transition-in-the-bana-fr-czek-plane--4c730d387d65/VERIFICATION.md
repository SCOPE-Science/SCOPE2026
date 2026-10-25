---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-25.md",
      "INDEPENDENT_AUDIT_2026-10-25.json"
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

From the exact real norm N=max(λ|u|,√(u²+v²)), N²=max(Q_strip,Q_Euclidean), choose an active quadratic at each N-unit vector. In equal-branch cases the τ-linear terms of [Q(x+τy)+Q(y−τx)]/2 cancel; mixed cases give linear cross term H=(λ²−1)x₁y₁−x₂y₂, bounded below by −max_{0≤t≤h}[(λ−λ^−1)t+q√(1−t²)], h=1/λ, q=√(1−h²). This concave function has argmax t=min(q,h), yielding C=λq (1<λ≤√2) and C=2q² (λ≥√2). The τ² remainders are nonnegative uniformly in all unit pairs, proving S²≥1−Cτ. For reverse asymptotic choose actual strict-activity unit points x=(h,s), s<q, y=(−t,√(1−t²)), 0<t<h; for fixed s,t and sufficiently small τ the squared objective equals 1−τ[(λ−λ^−1)t+s√(1−t²)]+O(τ²). Then first take τ↓0 and subsequently s↑q,t→min(q,h) to obtain limsup≤−C. Thus (S²−1)/τ→−C and S(0)=1 implies S_derivative(0+)=-C/2. Both formulas equal 1/2 at λ=√2. Exact rational checks λ=5/4 (C=3/4) and λ=5/3 (C=32/25), plus independent bounded minimization, corroborate without constituting a continuum proof.

## originality

PASS

Best-of-knowledge original endpoint coefficient and λ=√2 active-set switch. Xu–Liu 2026 establishes the same infimal norm and only the positive-skew envelope for τ≥sqrt(1−λ^−2); this does not determine its derivative at 0. The same-plane Wang et al. 2024/2025 FULL OA paper gives a supremal Euler–Lagrange constant and, in its high-λ proof, a related 2q² bilinear bound, but neither the full small-skew infimum nor the low-λ coefficient or matching witnesses. Chen et al. give a supremal von Neumann–Jordan functional. Published independent Resultary records determine a positive-skew saturation threshold and a Zbăganu supremum, neither of which mathematically implies the two-branch infimal endpoint derivative by any identified identity; the target Resultary item itself is duplicate dissemination of the source being audited, NOT an antecedent independent discovery. Priority remains qualified by contemporary or unindexed equivalent calculations.

## value

PASS

The coefficient is the precise natural sensitivity of the new quadratic skew Schäffer infimum for its canonical real two-dimensional Banaś–Frączek norm at τ=0, exactly where the focal source has no formula. The λ=√2 regime boundary determines whether the mixed strip/circle perturbation optimiser is interior on the circular arc or constrained by the strip cap. This is a structural global-in-λ transition, not a numerical interpolation or arbitrary slice; it supplies a mathematically useful sharp endpoint boundary even without the complete positive-τ profile.

The dated certificate retains the supplied scientific assessment, sources and limitations.
