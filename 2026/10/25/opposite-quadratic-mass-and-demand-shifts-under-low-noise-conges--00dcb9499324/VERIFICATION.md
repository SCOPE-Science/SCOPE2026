---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For any σ>0, y=t−Δ(M,E) reduces the equilibrium to Gσ(y)=y+Δ(mσ(y),eσ(y))=t. Both moments monotone in y and Δ coordinatewise nondecreasing, so Gσ strictly increasing with limits ±∞; existence and uniqueness follow. Represent pσ(x;y) as Pr(y+σW>=x) with standard centered logistic W, and integrate clipped threshold moments. At interior y, mσ(y)=y+exponentially small error; eσ(y)=y²/2+(π²/6)σ²+exponentially small by E W²=π²/3. The implicit Taylor expansion at θ has slope D=A+θB>0, giving y−θ=−(π²/6)Bσ²/D+O(σ4), hence the two coefficients. Direct softplus integration of L1 distance yields 2σlog(2cosh((y−θ)/(2σ)))+small=2σlog2+O(σ3). Explicit witness θ=1/2, h1=2ME gives A=5/4 B=1 D=7/4 and coefficients -2π²/21 and +5π²/42, and has non-symmetric interaction derivative, so nonpotential. Independent adaptive quadrature and scalar-root computations at three interior thresholds and small σ substantiate signs/coefficient convergence.

## originality

PASS

The local Sommerfeld expansion for a smoothed step is elementary prior work. The potentially strongest 2026 preprint Dupont–Petit–Séguret covers broad nonatomic nonpotential congestion equilibria and qualitative zero-noise behavior, and may state rate questions; full manuscript was inaccessible in this run, so broad noncoverage is NOT asserted. The available primary complete Koster–Verhoef–Shepherd–Watling article treats discrete group two-link probabilistic pricing rather than a continuous one-type threshold and opposing aggregate feedback coefficients. Bagchi–Boyles treats algorithmic iteration rates at fixed logit scale. No dominating implication was established, best-of-knowledge originality with serious residual risk.

## value

PASS

Two natural aggregate observables—population headcount and characteristic-weighted demand—respond in strictly opposite directions to vanishing choice noise in a genuinely nonpotential equilibrium, despite an O(σ) assignment disturbance. Exact feedback-sensitive σ² constants show why replacing demand with headcount may misrepresent a charging or congestion model. This is a motivated quantitative refinement, not just a routine logit integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
