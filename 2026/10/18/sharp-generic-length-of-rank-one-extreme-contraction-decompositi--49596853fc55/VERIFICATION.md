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
# Verification

The standalone `checker.py` was executed with Python 3 and SymPy. It passed affine-rank and exact independent-sign barycenter identities on 100 saturation strata with dimensions at most four, verified the nonzero four-vertex barycentric coefficients for the displayed \(2\times2\) rational witness, and excluded every at-most-five-term sign-vertex decomposition for the \(2\times3\) rational witness.

The arbitrary-dimensional claims rely on the six-step analytic proof: entrywise cube geometry, forced saturated-sign face, Walsh-character affine independence, independent-sign representability and affine Carathéodory, generic noncontainment of the rank-one map in a proper hyperplane, and explicit transcendental specialization. Finite tests alone cannot establish genericity or the arbitrary-dimensional upper bound. External peer validation is not claimed.
