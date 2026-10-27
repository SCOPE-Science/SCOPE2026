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

# Computational and mathematical verification

The standalone `verify.py` uses only the Python standard library. It implements the exact dominating-set weighted sum as a product of local closed-neighborhood constraints and eliminates each Boolean vertex by integer-arithmetic variable elimination. It compares evaluations at \(z=-4,0,1,\ldots,32\) against the 2026 primary-source coefficient table: 34 distinct values for polynomials of degree at most 33 certify polynomial equality. It checks nonvanishing derivative and a direct five-vertex support-bridge identity. Its verified derivative is \(1{,}100{,}417{,}597{,}440{,}000\).

For all finite connected constructed graphs, correctness rests on the independently written leaf-forcing bijection in `RESULT.md`, not on an extrapolation from finite computations. Historical priority and independent audit remain unperformed.
