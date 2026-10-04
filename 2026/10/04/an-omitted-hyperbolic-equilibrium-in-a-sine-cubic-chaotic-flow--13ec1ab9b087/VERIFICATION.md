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

The accompanying `verify_equilibrium.py` uses only the Python standard library. It performs exact rational interval arithmetic; no binary floating-point value is used in a logical comparison.

The checker verifies three ingredients. First, the rational preconditioner \(A\) has nonzero determinant. Second, each of the six faces of the box \(B\) is subdivided into \(100\) rectangles, and interval Taylor bounds for sine and cosine certify the required strict sign of the corresponding component of \(G=AF\) on every rectangle. This exhaustively establishes the Poincaré–Miranda hypotheses for the stated box. Third, interval evaluation of the Jacobian on all of \(B\) certifies \(a_1>0\), \(a_2>0\), and \(a_3<0\) for the characteristic polynomial, which proves the claimed hyperbolic saddle type at any equilibrium in the box.

The computation does not enumerate all equilibria and does not prove uniqueness in the box. It also does not certify any attractor basin, Lyapunov spectrum, or global chaotic property.
