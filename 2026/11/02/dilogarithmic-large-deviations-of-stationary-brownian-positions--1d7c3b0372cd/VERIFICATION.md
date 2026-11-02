---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification details

The analytic derivation is in `RESULT.md`; the independently executable Python 3 program `verify_ldp.py` is included in the same package and uses only the standard library. Running `python verify_ldp.py` on the embedded code reports `PASS: 19 independent analytic/numerical checks`. These comprise four product-to-dilogarithm Riemann tests, six optimizer/evenness checks, three central fourth-order expansions, three large-displacement asymptotic checks, and three exact-variance convergence checks.

The program tests finite numerical values and cannot establish convergence at an infinite time, a full large-deviation principle, originality, or independence. The mathematical proof derives the stationary perpetuity, establishes local moment-generating-function convergence including derivatives, proves exponential tightness and the lower bound by tilt, and calculates the Legendre shape. The exponential-moment domain has open endpoints: \(|\theta|<1\). In particular, no theorem requiring continuity of the extended cumulant limit at \(|\theta|=1\) is silently invoked.

Unproved extensions include arbitrary refractory laws, non-Poissonian reset times, position distributions away from stationarity, and finite-parameter density prefactors. Independent audit has not been performed.
