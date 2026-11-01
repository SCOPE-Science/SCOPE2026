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

# Mathematical verification and limits

The all-parameter theorem is proved by the two-sided stopped multiplicative walk and finite-overshoot bounds in `RESULT.md`. The referenced existence theorem and non-atomicity are established by Barański–Śpiewak, arXiv:1905.11048v1, Theorem 3.6 and Proposition 3.11. No finite run is interpreted as a proof of a continuum assertion.

To reproduce the auxiliary exact-rational example checks, run `python3 CHECK.py` using a standard Python 3 interpreter. The checker uses only standard-library fractions and math functions. It verifies continuity at the two breakpoint locations, affine inverse constraints, strict positivity of both Lyapunov products, the slope criteria for the inverse-first-moment phase, and an analytic-root numerical bracket. The recorded finite checks test the example, not the general stopped-walk theorem.

Scientific boundary: existence of a limiting coefficient for normalized masses is not claimed; the comparison constants are not optimized. Endpoint exponents are not global measure dimension, and only constant random map-selection probabilities are treated. Independent audit has not been performed.
