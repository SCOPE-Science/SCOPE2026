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

# Verification and limits

The exact spectral calculation in `RESULT.md` gives all normal and tangent directions, not just a discretization. Its curvature-radius positivity establishes the full sharp convexity interval. The Schur inequality and its equality analysis identify the six axial and twelve face-diagonal endpoint degeneracies. A direct two-dimensional tangent restriction computes the characteristic polynomial; support-coordinate integration reduces the three-dimensional volume formula to normalized spherical monomial moments.

Run `python3 verify_quartic.py` with Python 3 and its standard library. The executable recomputes exact rational moments and the volume polynomial, verifies the endpoint rank classes and exact polynomial identities, and checks 12000 independently constructed random orthonormal pairs against the derived curvature form. It reports `ALL_CUBIC_HARMONIC_CHECKS_OK` when every check passes. The checker was executed successfully from the packaged source files. Random finite tests do not establish a global continuum result or historical priority; these are supplied, as far as established, by the analytical proof and documented literature comparisons.

This is a self-review only. No independent validation or certification has been performed.
