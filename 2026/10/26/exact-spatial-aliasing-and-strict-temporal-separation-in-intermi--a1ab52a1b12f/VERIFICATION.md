---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Solve the three-state stationary Fourier generator with reset injections into state 0 or symmetric ±. With L=beta+rho and S=alpha+beta+rho, their characteristic functions have the common strictly positive denominator Q=(rho+Dk²)(L²+v²k²)+alpha(rho L+v²k²), and numerator difference rho*k²*(v²-DL). Therefore the complete stationary position laws agree iff v²=DL; on balance Q=L(rho+Dk²)(S+Dk²), giving both exactly rho/(rho+Dk²), the symmetric Laplace law. The internal stationary ballistic fractions differ, alpha/S versus (alpha+rho)/S. Applying the stationary generator to X eta(J) gives H=v*pi_bal/L and to X² gives variance 2D/rho on balance. Condition on no Poisson reset over lag t; heading expectation decays as e^(-beta t), yielding C(t)=e^(-rho t)[E X²+v²*pi_bal*(1-e^(-beta t))/(beta L)]. This proves C_B>C_D>C_resetBM strictly for t>0, with positive difference D*rho/(beta S)e^(-rho t)(1-e^(-beta t)) and integrated gap D/[S(beta+rho)]. These are stationary correlations, not arrival probabilities or full-process equivalence.

## originality

PASS

The parent paper already derives both one-time stationary densities: equality at v²=D(beta+rho) is a specialization of prior formulas and expressly not a novel standalone result. The distinct additional claim is exact all-positive-lag stationary covariance ordering and the nonzero integrated discrepancy among models with identical position marginals.

## value

PASS

The research question is identifiability of distinct transport/reset protocols from stationary observations. Constructing exactly identical complete position distributions but a provably strict, analytically quantified discrepancy at every time lag gives a meaningful discriminator and an integrated time-average variance contrast. This is a natural nonequilibrium stochastic-process invariant, not a cosmetic restatement of a known spatial density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
