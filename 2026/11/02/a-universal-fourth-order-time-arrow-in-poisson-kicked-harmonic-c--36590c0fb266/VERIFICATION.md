---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The two-time innovation relation Y_t=q Y_0+eta_t, q=exp(-gamma t), eta_t independent of Y_0 and centered with variance Var(Y_0)(1-q^2), gives E[Y0 Yt^3]-E[Y0^3 Yt]=-(q-q^3)(E[Y0^4]-3 Var(Y0)^2). The Poisson stochastic-convolution fourth cumulant is lambda E[J^4]/(4 gamma) and thermal Brownian noise contributes none. Maximizing q-q^3 yields q=1/sqrt(3), proving both peak and inverse formulas. Stationary time reversal makes the fourth joint-cumulant swap of independent added V vanish, while pair-partition terms cancel because the covariance is stationary; independent mixed cumulants add and K_{p,q}=q^q kappa_{p+q}. These are exact identities for symmetric/asymmetric marks, including nonzero mean after centering. Independently used exact symbolic cumulant and innovation calculations and checked the maximum, invertibility and noise cancellation for representative parameters. Unlike a simulation this reconstructs the general proof.

## originality

PASS

Di Bello et al. (arXiv:2309.13424v2) already propose the same shot-noise harmonic model and exhibit the chronological X,X^3 asymmetry in Figure 5 and Equation 68. The model and qualitative irreversibility therefore are not new. In the inspected sections and Appendix B, however, they do not evaluate this centered full-lag fourth cumulant profile, prove the universal unique maximizing lag, or give the reversible-sensor invariance and joint-cumulant hierarchy. General Lévy-OU and cumulant formulas are known and could mechanically imply this result with specialization; no direct published identical full package was located. Best-knowledge PASS with a meaningful general-theorem overlap risk.

## value

PASS

The published observable is physically motivated, not a made-up moment. Its exact sign, nontrivial optimal lag, identifiability of only the aggregate fourth-kick intensity, and robustness to independent time-reversible measurement contamination are useful observable-specific quantitative facts. It does not claim entropy-production measurement or finite-sample signal-to-noise optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
