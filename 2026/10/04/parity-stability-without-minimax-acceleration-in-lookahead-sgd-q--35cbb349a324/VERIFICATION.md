---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

One outer cycle is the polynomial \(p(\lambda)=1-\alpha+\alpha(1-\eta\lambda)^k\). For even \(k\), the lower stability inequality is automatic and the upper one is exactly \(|1-\eta\lambda|<1\), giving \(\eta L<2\); for odd \(k\), the upper inequality is automatic and the lower gives the stated real-root ceiling, with multipliers \(+1\) and \(-1\) at the respective boundaries. For the minimax problem, even powers are nonnegative, so interpolation can only move modal factors toward one and cannot beat the classical equioscillating step. For odd powers the endpoint values are monotone in curvature; before the equioscillation point \(\alpha=1\) is optimal, while after it balancing endpoints yields \(F(x)=(b-a)/(2-a-b)\). The displayed auxiliary function has nonnegative derivative because \(|1-\kappa x|\ge|1-x|\) and \(\kappa(1-Q)\ge1+Q\), proving \(F\ge Q\). Equality is unique for \(k\ge2\). The verifier checks boundary multipliers, exact optimum values and dense grids as transcription guards.

## originality

PASS

The original Lookahead paper already writes the expectation multiplier \(1-\alpha+\alpha(I-\gamma A)^k\), studies noisy quadratics, and analyzes deterministic quadratics with momentum through a linear dynamical system. It emphasizes larger inner learning rates and fixed interpolation empirically, but it does not state the even/odd fixed-\(\alpha\) stability frontier or solve the robust spectral-interval minimax problem for plain-gradient inner steps. Resultary searches found related optimization stability/minimax records but no covering Lookahead theorem.

## value

PASS

The theorem sharply separates stability enlargement from worst-case acceleration: odd synchronization lengths can stabilize learning rates beyond the inner GD limit, yet no fixed interpolation improves the best robust spectral contraction. This directly clarifies a central motivation of Lookahead on a canonical model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
