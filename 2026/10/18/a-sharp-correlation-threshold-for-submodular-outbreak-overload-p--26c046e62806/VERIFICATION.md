---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Condition on shared P: with n=d-|S|-2 unvaccinated other leaves, second vaccination difference equals -E[P^2(Pr(Bin(n,P)=r-2)-Pr(Bin(n,P)=r-1))]. Beta integration gives A_n and C_n with ratio C_n/A_n=((n-r+2)/(r-1))*((alpha+r)/(beta+n-r+1)). The resulting condition L(n)>=(0) is affine decreasing slope -(alpha+1), hence worst at n=d-2 and exactly reduces to (r-1)beta-(d-r)alpha >= d-1. For n=r-2 the sign is strictly negative, for n<r-2 zero. At r=1 the sign is positive for all pair choices; at r=d it is nonpositive. Independent exact rational Beta moments reconstruct for d=5,r=3,mu=1/4: correlation rho=1/6,1/5,1/3 gives respectively second differences -195/57344,0,3/256 and criterion lhs 1,0,-2, confirming strict sign reversal at the predicted boundary. Interpolating real parameters is justified algebraically by positivity of Gamma/Beta moments, not by finite grids.

## originality

PASS

The criterion is a particular discrete-concavity characterization of Beta-binomial overload tail as the number of susceptible leaves varies. The prior independent Poisson-binomial reliability/log-submodularity work and disease-network mitigation studies do not entail it after a correlated Beta mixture. No matching exact prior threshold was identified in targeted Resultary/literature searches, subject to known primary-access limits.

## value

PASS

An exact necessary-and-sufficient correlation threshold for diminishing vaccine returns is a motivated structural property of a natural exchangeable outbreak model. It quantifies a genuine sign flip even at constant expected infections prevented, rather than just an expected-case modularity calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
