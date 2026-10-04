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

The analytic proof verifies the equality theorem in every dimension. The supplementary executable check `verify_entropy_extremizers.py` was run from the packaged path and produced `VERIFY_OK`.

The script checks: (i) the exact symbolic first- and second-derivative identities for the one-dimensional deficit, (ii) agreement of the closed form with high-resolution quadrature, (iii) strict numerical positivity away from the three one-dimensional equality ratios, (iv) representative multidimensional equality and nonequality states, and (v) the autocorrelation signature that recovers the generator directions of a phased affine cube.

The numerical checks are not used as a substitute for the infinite-dimensional proof. The originality assessment remains literature-dependent and has not received an independent audit.
