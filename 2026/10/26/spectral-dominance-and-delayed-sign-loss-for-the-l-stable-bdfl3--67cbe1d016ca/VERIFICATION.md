---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The exact constant-step scalar recurrence has characteristic P_s(ζ)=(10+6s)ζ³−15ζ²+6ζ−1. Its discriminant −108(9s²−12s+5)<0 gives one positive simple real root r and one conjugate complex pair of modulus q, all inside the unit disk. Using Vieta r q²=(10+6s)^{-1} and the root equation gives q>r iff r<2/5. Implicit differentiation yields decreasing r(s); P_{15/16}(2/5)=0, so the unique crossover is s*=15/16. Distinct-root spectral decomposition y_n=c r^n+2Re(d z^n) proves the open perpetual-positivity cone at and below the threshold and exact positive real-eigenray when q>r. Any d≠0 above threshold gives both signs infinitely often. For exact exponential initial values the Lagrange coefficients c=|t−z|²/|r−z|² and d=(t−r)(t−conj z)/[(z−r)(z−conj z)] are nonzero as required. At s* c>2|d| is proved by explicit exponential bounds. The angular phase cosθ*=7/10 has irrational θ*/π; compactness yields bounded waiting to a negative arc near critical, matching the lower envelope and giving (s−s*)N_−→(125/96)log H*=4.579428036... . Independent symbolic checks reproduced the cubic discriminant and r′(s*)=−32/125, plus four near-threshold first-negative indices (301,609,1541,4567); finite tests are not proof of the asymptotic limit.

## originality

PASS

BDFL3 has the historical alias BDF2OPT(4); its coefficients and A/L-stability are prior work, including the 2010 NASA analysis, and are not claimed new. The contribution is the exact root-modulus crossing, classification of all scalar positive-history cones, and reciprocal-distance first-negative index for exact exponential starter. The 2010 full text analyzes stability loci and numerical fluid dynamics rather than the positivity cone. Jensen–Ketcheson–Lóczi (2026) supplies the scheme and stiff-mode damping; only abstract and metadata were accessible this run because direct full-text retrieval failed and authorized institutional access reported VPN disconnected. The BDF2 delayed sign loss record concerns a different recurrence and square-root scaling. Qualified best-of-knowledge PASS; unread same mathematical model 2026 sections are a substantial residual priority risk.

## value

PASS

The optimized L-stable method can be absolutely stable on scalar decay while positive-history robustness collapses to a ray at s=15/16. This is a nontrivial exact spectral boundary distinct from routine A-stability, with an explicit 4.5794/(s−s*) delay explaining misleading finite-time positive simulations near threshold. It supplies precise diagnostics for a physically motivated numerical scheme without making unsupported nonlinear or adaptive-step claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
