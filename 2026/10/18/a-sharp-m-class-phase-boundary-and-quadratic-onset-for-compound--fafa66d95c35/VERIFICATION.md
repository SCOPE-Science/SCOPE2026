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

# Verification record

The result uses the explicit squared-size-biased Beta jump transform and the independent Beta(1,2) canonical multiplier. The critical algebraic identities are the rational coefficient ratio, the sign criterion \(b(3-a)\le4a\), and the two critical Taylor coefficients. These are reproduced exactly for representative rational shape parameters in the standalone file `verify_beta_subgamma.py` using only the standard Python library. The checker passed 2,746 exact and numerical assertions, including strict interior improvement above the phase boundary. The verification is finite, while the theorem ranges over every real positive shape and is proved analytically in RESULT.md.

At the critical line the Taylor coefficient of degree one vanishes but the coefficient of degree two is strictly negative. The unique near-critical interior maximizer is obtained from a local implicit-function argument plus the strict global gap away from the origin. Neither global uniqueness throughout the strict interior regime nor a closed-form value for its noncritical optimizer is claimed.

Independent mathematical audit and priority assessment have not been performed. Published general transform identities and M-class definitions are expressly attributed; no formal external certificate is claimed.
