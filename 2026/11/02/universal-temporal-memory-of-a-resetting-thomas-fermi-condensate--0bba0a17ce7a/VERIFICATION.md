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

PASS. Read frozen RESULT.md and verify_edge.py. From b''=ω²/b², b(0)=1, b'(0)=0 follows b'²=2ω²(1−1/b), strict b''>0 and 0<b'<sqrt(2)ω. Stationary Poisson age A~Exp(r) and no-reset conditioning yield C_r(τ)=x0²exp(−rτ)Cov(b(A),b(A+τ)); the reset-event contribution vanishes upon centering. Since b and b(·+τ)−b are strictly increasing, independent-copy covariance is strictly positive; long-lag factor follows L² derivative limit b'(t)→sqrt(2)ω. Independently rederived exact moments Cov(Z²,Z²)=20, Cov(Z²,Z⁴)=672, integrated shift moments 28 and 2304, giving Var=5ε⁴−56ε⁶ and integrated covariance=7ε⁴−96ε⁶, hence rT=7/5−88ε²/25+O(ε⁴). Slow-reset dominated limit rT→1. These identities and the tail-splitting proof support the asymptotics; no finite ODE quadrature is substituted for them.

## originality

PASS

PASS at best knowledge. Mesquita et al. introduced exactly the condensate reset protocol and the one-time stationary edge law, while Stojkoski et al. studied renewal autocorrelations for diffusive resetting. Their inspected results do not yield the nonlinear convex-edge strict inequality or the Thomas–Fermi-specific 7/5 and -88/25 memory asymptotics. More general deterministic-age renewal theory could subsume the first covariance identity.

## value

PASS

PASS. Temporal memory is a natural missing observable of a known condensate protocol; exact all-rate strict inequality and nontrivial two-limit quantitative law are meaningful in modeling reset dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
