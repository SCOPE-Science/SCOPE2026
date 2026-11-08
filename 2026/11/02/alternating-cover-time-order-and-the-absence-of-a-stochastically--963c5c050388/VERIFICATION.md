---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

On K_(n,n) each synchronous non-lazy step samples a uniformly independent vertex of the opposite side; two part-specific coupon streams are independent. Different-part starts yield U_(n,1)(t)^2; distinct same-part starts yield U_(n,0)(2s)U_(n,2)(2s) even, U_(n,0)(2s+2)U_(n,2)(2s) odd. Exact reveal identities U0(m+1)=U1(m), U1(m+1)=U1(m)/n+(n−1)U2(m)/n establish positive odd difference U1(m+1)(U1(m+1)−U1(m))/(n−1) for m>=n−2. Even first missing-coupon terms cancel, leaving rho^(2m)+O(q^m), q=1−2/n<rho²; asymptotic ratio 1. Enumerated coupon sequences n=2..5 and checked exact alternating CDFs for s=1..7; some early even differences are zero (e.g. n=4,s=1), correctly distinguished from eventual strict inequalities. Collocated starts pathwise dominated by distinct same-part, preventing any randomized global stochastic optimum.

## originality

PASS

Best-of-knowledge originality for the precisely bounded final claim; prior premises and covered specializations explicitly credited. Four searched implication tests and actual primary-source inspections below identify the distinctions and residual priority risks.

## value

PASS

Full deadline-by-deadline stochastic order is a natural risk-sensitive cover-time criterion not captured by expected speedup. An infinite, vertex-transitive bipartite family has perpetual late-time parity crossings and proves no deterministic or randomized universally optimal starting arrangement. Sharp differing tail rates explain the obstruction structurally.

The dated certificate retains the supplied scientific assessment, sources and limitations.
