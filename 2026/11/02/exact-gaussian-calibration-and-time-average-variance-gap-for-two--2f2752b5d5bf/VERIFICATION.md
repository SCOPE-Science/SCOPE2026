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

On SPD quadratic U(x)=x^T H x/2, substitution into the two explicitly specified SRK-I/SRK-II stages yields the same pathwise recursion Z_new=P(hH)Z+sqrt(2)(DeltaB-HJ), with P(x)=1-x+x^2/2 and Brownian-pair covariance Var(DeltaB-HJ)=h(1-x+x^2/3). The AR modal contraction satisfies |P(x)|<1 precisely 0<x<2; its invariant variance v=2h q/(1-P^2). Exact factor 2xq-(1-P^2)=x^3(3x-4)/12 establishes unique calibration x=4/3 and simultaneous SPD calibration only isotropic H=4I/(3h). Summing stationary lag covariances gives physical-time variance 2/lambda^2 q/(1-x/2)^2 = (2/lambda^2)[1+x^2/(3(2-x)^2)], strictly above OU for every positive stable step and exactly 7/3 at resonance. Euler scalar coefficient equals OU because the AR multiplier is 1-x and innovation variance 2h. Independently rechecked polynomial identities and 7/3 rational value and stage algebra. Proof covers arbitrary dimension by spectral diagonalization, not finite experiments.

## originality

PASS

Best-of-knowledge comparison of exact statements and mathematical implications across relevant primary literature and Resultary; key source-access/alias risks are explicitly retained. The assessed new claim is not the background object, source algorithm, or textbook intermediate identities.

## value

PASS

An exactly invariant Gaussian stationary distribution need not optimize physical-time Monte Carlo variance. These two source samplers coincide pathwise on Gaussian targets even though their stage counts differ, have a unique invariant-exact step, and always inflate linear-observable asymptotic variance while the biased first-order Euler chain has the OU coefficient. This sharp concrete tradeoff is a natural integrator diagnostic; no claim of superiority at equal gradient cost.

The dated certificate retains the supplied scientific assessment, sources and limitations.
