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

Conditioning on independent X innovations gives EX_n²/(2h)=1+Σ_{k=0}^{n−2}<g,K_ρ^k g> for g(z)=|1−(c/J)·||z||²|. Mehler P_ρ is positive self-adjoint on Hermite chaoses, so K_ρ=M_g P_ρ M_g is positive Hilbert–Schmidt and positivity-improving for ρ<1; its simple top eigenfunction overlaps g. Thus bounded moments iff Λ_J(c,ρ)<1, with linear/exponential top-eigenvalue growth on/above 1. Hermite coefficients prove strict monotonicity for 0≤ρ1<ρ2<1: equality would require gu constant, impossible since 1/g is non-L² near its zero sphere. Gaussian operator continuity, Λ(0)=1−2c+(1+2/J)c², and ρ↑1 test functions supported at large ||z|| prove unique frontier for 0<c<2J/(J+2). Independent exact Wick/Hermite check recovers 25/24 Rayleigh witness for J=1,c=1/2,ρ=1/2.

## originality

PASS

PASS best of knowledge for unique stationary-OU correlation phase boundary of this real-line sampler, not for general multiplicative transfer theory or the numerical method.

## value

PASS

Temporal persistence changes mean-square stability despite fixed standard Gaussian marginals, and unique threshold gives a useful sharp phase diagram and exact instability witness for a natural derivative-free quadratic sampler; not merely a numerical simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
