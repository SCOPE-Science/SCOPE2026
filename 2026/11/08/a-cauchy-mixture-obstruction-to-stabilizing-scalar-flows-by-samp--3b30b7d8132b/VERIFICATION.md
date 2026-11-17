---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

Exact stochastic integral multiplier on each sampling cell follows from stable characteristic functions and variation of constants. Positive alpha-stable subordinator variable V times independent standard Cauchy C has characteristic exp(-|u|^alpha), yielding via Poisson log potential E log|e^(theta tau)+dVC|=0.5 E log(e^(2theta tau)+d^2 V^2). Log absolute moment integrable by stable tails/local density and log-moment bounds; sampled log SLLN applies. Within-cell sup has finite log+ expectation using p<alpha maximal moment and deterministic-kernel integration by parts; Borel-Cantelli removes k^-1 fluctuation, with sampled times giving reverse limsup bound. Nonzero gain strictly increases exponent; continuity and divergence yield unique critical gain theta<0. Cauchy endpoint bcrit=|theta|/sigma sqrt(coth(-theta*tau/2)). Independent numerical Cauchy drift/gain/critical cases checked; source verify.py read, not rerun. Finite checks are not the a.s. proof.

## originality

PASS

Best-of-knowledge finding concerns exact almost-sure logarithmic sample-product exponent for symmetric alpha-stable innovations with 0<alpha<=1 and feedback multiplying the sampled state in the NOISE coefficient. The Brownian same-architecture stabilization theorem has alpha=2 and cannot extend its finite-variance sufficient condition to these infinite-first-moment laws; Zhang 2026 uses alpha>1 and sufficient results; G-Levy results concern nonlinear expectation/moment notions. The stable/Cauchy mixture and Poisson identity are classical and are not claimed original. New result is exact all-gain pathwise exponent and obstruction in this parameter regime. Relevant full G-Levy paper unavailable, so historical priority explicitly qualified.

## value

PASS

Sharp stability/instability boundary for an established sampled stochastic-control architecture precisely at the infinite-mean heavy-tail range 0<alpha<=1. It overturns naive extension of Brownian noise stabilizability by showing the universal nonnegative increase in upper a.s. exponent and gives explicit Cauchy gain threshold; control researchers can use the exact rate rather than insufficient moment criteria.

The dated certificate retains the supplied scientific assessment, sources and limitations.
