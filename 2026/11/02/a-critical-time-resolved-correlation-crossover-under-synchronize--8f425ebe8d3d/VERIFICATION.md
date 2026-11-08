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

Conditioning on the common reset clock (Poisson model) or common Brownian multiplier (Itô model) makes particles independent centered Gaussians with common random conditional variance Z. Thus equal-time squared-position interparticle covariance is Var(Z), not ordinary X covariance. Its first moment satisfies m1'=-a1m1+2D; second conditional-variance moments obey m2'=-a2m2+4Dm1 with a2P=(lambda/s)(1-(1-s)^4)-4gamma and a2G=4(lambda-gamma)-6lambda s. Positive convolution kernels and exact gap a2P-a2G=lambda s²(4-s)>0 prove 0<CP(t)<CG(t) for all t>0, all real gamma, 0<s<1. Along gamma_s=lambda(1-3s/2+theta s²), a1=2lambda s(1-theta s), a2P=lambda s²(4(1-theta)-s), a2G=-4lambda theta s². Rescaling t=u/(lambda s²) yields compact-uniform positive-kernel convergence and scaled covariance limits (1-exp(-4(1-theta)u))/(1-theta) and (exp(4theta u)-1)/theta, after a vanishing scaled m1² term. The difference expansion is 8u²+O_theta(u³). Independent high-precision direct convolution quadrature checked strict inequality and convergence at 12 critical parameter/time combinations. Stationary fourth-moment thresholds follow a2 signs, not from finite simulations.

## originality

PASS

Best-of-knowledge PASS qualified: Galla (2026) already derives the weak-reset common-noise Gaussian approximation and stationary higher covariance, and prior exact Poisson reset work supplies component dynamics. The specific sharp joint transient scaling at t=O(s^-2), its separate Poisson versus Gaussian functions and universal initial difference are not directly present in the inspected primary statements. Moment ODE specialization may make it derivable from existing ingredients, but it requires the singular-time limit; global priority remains open.

## value

PASS

Quantifies a subtle but operationally meaningful breakdown of a Gaussian approximation that matches the entire particle variance curve exactly but strongly distorts time-resolved interparticle squared-energy correlations at the critical scale; one asymptotic saturates while the other grows exponentially. This is not merely the previously known stationary divergence criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
