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

# Reproducibility and checks

Run the bundled `b4_exact_certificate.py` with Python 3 (standard library only) in the same directory. It constructs the six boundary lines governing spline truncated cubes over \(T\in[0,2]\), \(X\in[0,1/2]\), enumerates all nonempty sign cells, triangulates them and calculates each of four degree-three positivity polynomials in the triangular Bernstein basis using exact rational fractions. Successful execution verifies nine cells, ten triangles, 400 nonnegative controls and area exactly one. The 400 inequalities prove the corresponding polynomial bounds for the entire real rectangle, not merely at the control points.

The remaining analytic steps are documented in `RESULT.md`: exact sine-series reduction, boundary Poisson positivity, sinc aliasing at the half frequency, and the known unit/superunit-scale zero theorem from arXiv:2609.13116v1. Only the Bernstein inequalities are established computationally by the checker; it neither independently proves the cited external theorem nor validates an arbitrary extension below \(\lambda=1/2\).

Independent verification: not performed.
