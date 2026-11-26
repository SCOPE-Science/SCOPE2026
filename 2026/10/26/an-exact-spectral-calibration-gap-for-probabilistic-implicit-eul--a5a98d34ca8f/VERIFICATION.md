---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

On the two consistent kernel coordinates the RHS noise is multiplied by q_j; independence gives terminal variance sigma² a_j by summing h³ q_j^(2k+2). The deterministic step-doubling indicator is positive since (1+lambda_j h/2)²>1+lambda_j h. In u=log(sigma²) the sum of the equal-mean Gaussian distances is half the sum of log cosh((u−log r_j)/2); it is strictly convex, with the two derivative terms cancelling at the midpoint. This proves the unique variance scale and minimum, including zero exactly for matching ratios. The h-leading error is exp(−lambda_j T) lambda_j² T h/4 and the leading variance factor is h²[1−exp(−2lambda_j T)]/(2lambda_j), giving the stated limit. The sign of its logarithmic derivative is that of 5(1−exp(−2x))−2x; strict concavity, positive initial slope and negative tail show one positive root and two distinct rates at each submaximal positive level. Separate high-precision arithmetic reproduced x_*=2.482557115872138151849… and the gap 1.000620761200976286155… for T=1 and rates 1 and 10. The nonzero lower bound is for terminal-marginal distances (or objectives containing them additively); the resonance is at leading order, not asserted to be exact at finite mesh.

## originality

PASS

The numerical method, use of a scalar Bhattacharyya calibration objective, and abstract two-target geometric-mean minimization have prior coverage. The supported distinct content is the step-doubling spectral law for this forced solver and its exact classification of persistent gaps and unequal-rate matches. The generic S-divergence theorem does not identify that law, and the examined solver sources do not give it.

## value

PASS

This gives a concrete obstruction for an existing scalar calibration strategy: even optimizing the common scale separately at every resolution does not force both terminal marginal distances to vanish. The explicit spectral law identifies exactly when rates on opposite sides of its maximum evade that obstruction. This is useful for deciding when mode-dependent scales are necessary for these targets, not a claim about accuracy against the true solution law or global calibration over all times.

The dated certificate retains the supplied scientific assessment, sources and limitations.
