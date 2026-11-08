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

For equal groups with periodic inter-booster times, mean susceptibility is s(u)=1-u(1-e^-1/u). Inversion-symmetric Perron root of M=(diag(1-alpha/2,1-alpha/2)+offdiag(alpha/2))diag(s(u+ub/2),s(u-ub/2)) gives rho-double-prime(0)=u^2/4[(d2s/du2)-2(alpha-1)/alpha*(ds/du)^2/s], with the first derivative squared as required. With Q=s s"/(2s"(u)^2) (here denominator denotes [s-prime]^2), direct differentiation at t=1/u gives dQ/dt=-t N(t)/(2(e^t-1-t)^3); N coefficients vanish through n=5 and are positive at every n>=6 by (n-1)[2^(n-2)(n-8)+n^2-n+4]. Thus Q increases strictly from 0 to 1 in u, yielding one crossover for 1<alpha<=2; alpha<=1 always positive curvature. Independently recalculated 15 local eigenvalue curvatures and u_c(2)=0.23803677671827. The zero-curvature equality case is deliberately not classified.

## originality

PASS

The original Foutel-Rodier–Charpentier–Guérin article fixes the model, spectral constraint and fair-allocation result for alpha<=1. Galeotti–Rogers and Delmas–Dronnier–Zitt already show unfair/static allocation effects. Here the exact unique threshold in recurrent deterministic boosters with exponential waning and alpha>1 is distinct; a universal nonlinear-cost theorem might give an implicit version.

## value

PASS

Closes the precise local allocation-direction gap in the disassortative range omitted by a fair-allocation theorem for the originating recurrent-vaccination model. Quantifies how resource intensity reverses which allocation lowers disease-free invasion potential, including a sharp threshold and explicit nonlocal witness. Not a global optimization or epidemic-outcome result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
