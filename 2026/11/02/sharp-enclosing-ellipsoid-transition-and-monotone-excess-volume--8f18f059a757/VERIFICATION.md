---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The original optimal ellipsoid formula and transition are mathematically correct but already in Todd (1982). The final corrected claim explicitly imports that known result as a premise. For inactive caps the volume ratio strictly grows because the ellipsoid stays unit and cap volume shrinks. For active caps, h=1−a, q=(d−1)/2, the ratio is a positive dimension constant times F(h)=(2−h)^q/[∫_0^1 y^q(2−hy)^qdy]; derivative of logF is q times a strict negative weighted average inequality y/(2−hy)<1/(2−h). Endpoint a→1 gives (d+1)/2 multiplying the constant; endpoint a→−1 gives 1. Fixed a>0 Laplace asymptotics give √(2πd)a/(1+a), and a=τ/√d Gaussian-marginal convergence gives e^{−max(τ,0)^2/2}/Phi_bar(τ). Boundaries include d=2, τ=0; independent quadrature grid corroborated d=2,3,7.

## originality

PASS

Strong prior coverage required scientific repair. Michael J. Todd 1982 Proposition 1 and §3 already derive one-sided-cut ellipsoid shape and exact transition at −1/d; the original all-height shape headline is NOT original. The rewritten claim explicitly credits Todd and asserts only the full strict normalized excess-volume ordering and endpoint/high-dimension quantitative laws, for which Todd text reviewed did not give equivalent formulas. A further implicit calculus corollary or unindexed optimization result remains a substantial risk.

## value

PASS

The exact monotonic enclosing-volume overhead measures rounding efficiency across all truncation heights; strict ordering plus dimension-varying thin-cap and Gaussian scaling provide useful quantitative benchmarks. This is a narrow self-contained consequence of a known optimal ellipsoid and should not be marketed as discovery of the ellipsoid itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
