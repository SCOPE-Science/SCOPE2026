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

Reconstructed the mechanism and all quantifiers from the frozen RESULT: A1,A2 partition the half-line, giving φ1(x)+φ2(x)=2√π√x, while 0<φ2(x)↑L<2. Positive-initial cooperative ODE solutions have monotone zero-argument limit u, and differentiation of √(u1+u2) yields √π≤∂t√(u1+u2)≤√(2π), proving πt²≤sum≤2πt² and nonzero u for t>0. Since u2≤2Lt, u1→∞ and then u2→∞, yielding u2/t→2L. With r=√u1, the exact equation gives r=√π t+2√(2L)√t+o(√t), hence u1=πt²+4√(2πL)t^{3/2}+o(t^{3/2}). The zero-start Laplace cumulant identity implies Pz(ζ>t)=exp(−z·u(t)), almost sure finite-time explosion for all finite z≥0 nonzero and the distinct type-specific exponents. Independently evaluated stable integral partitions and numerical ODE trajectories as finite illustrations, not infinite proof.

## originality

PASS

The exact interleaved stable process is introduced in Chaumont–Lamoureux and explicitly left undecided, while their next example has a different type dependence and is already known explosive. The assessed proof classifies the formerly undecided exact case and derives the quantitative type-dependent tails. General backward-ODE uniqueness theorems are credited but do not state this evaluation. An unidentified specialized comparison remains a genuine risk.

## value

PASS

The starting paper expressly identifies this concrete multitype conservativity mechanism as undecided. The exact nonconservativity verdict plus genuinely different type-one quadratic and type-two linear log-survival scales, and computable t^{3/2} correction, is an independently meaningful branching-process finding rather than an elementary renaming of a criterion. It gives an explicit boundary example for the reach of componentwise Grey tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
