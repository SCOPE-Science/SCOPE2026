---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For fixed endpoints inside the open interval, conditioning on the endpoint of free Brownian motion gives the killed/free kernel ratio. With generator (1/2)d²/dx², Dirichlet eigenvalues are n²π²/(8ε²) and eigenfunctions have normalization ε^(-1/2). The sine bound |sin(nθ)|≤n sin θ on [0,π] follows from a sum of n unit complex exponentials for the sine ratio. Thus after dividing by the ground-state product the absolute remainder is bounded by R_ε, even arbitrarily near the wall. The free-kernel divisor contributes an exponential multiplier between 1 and exp(2ε²); outside or at the walls both the strict survival and the cosine product are zero. Integrating preserves both bounds without dividing by any small endpoint probability; a neighborhood of zero has positive mass on every centered Gaussian support. For fixed C, changing variables on its support yields H=1 for rank zero, H∼ε I(w)/sqrt(2πλ) for rank one, and H∼8ε²/(π³ sqrt(det C)) for rank two, using the cosine integral 4/π. This also gives the Brownian-motion and anti-periodic constants 4/π and 2. Normalizing a multiplier in [1-R_ε,(1+R_ε)exp(2ε²)] preserves covariance-uniform O(ε²) TV error against the moving cosine-weighted law; weak Gaussian convergence with bounded continuous weights yields the stated weak limit, not generally TV across supports. Source verification reports 2,381 finite deterministic assertions; supplied script inspected, not executed. The analytic pointwise bound, not the finite calculations, proves the uniform assertion.

## originality

PASS

Pass for the covariance-uniform relative confinement law, rank constants for the full endpoint family and conditional endpoint crossover taken together. The Brownian covariance parameterization, killed-kernel expansion, and classical pinned and free Brownian special cases are antecedents, not new here. The inspected results do not supply the two-sided relative estimate and normalized endpoint asymptotic across arbitrary moving and singular Gaussian covariances.

## value

PASS

The leading constant and power of ε matter in rare-event comparisons across covariance ranks. The relative bound remains informative even when the endpoint factor tends rapidly to zero, and the cosine tilt identifies which endpoints are seen conditional on the event. This addresses the moving-covariance regime, for which fixed-process asymptotics cannot simply be substituted, and explains why support changes permit weak but not total-variation convergence to the limiting law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
