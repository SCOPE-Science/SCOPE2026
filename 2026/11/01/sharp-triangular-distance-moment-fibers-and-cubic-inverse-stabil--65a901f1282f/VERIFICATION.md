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

# Verification and limitations

Run `python verify_triangle_moments.py` with Python 3, SymPy, and NumPy. The verifier independently expands squared distance in four reference-simplex barycentric variables and uses the exact factorial integral of every monomial. It verifies all three forward identities symbolically in three unconstrained squared side variables, with no floating-point assumptions. It verifies the exact Heron moment identity and a pair of explicit, noncongruent moment-colliding triangles with an exact sixth-moment discrepancy. It additionally performs independent four-dimensional Gauss–Legendre quadrature for four concrete triangles to check normalizations and mixed terms. Successful execution prints `VERIFY_OK`.

The mathematical analysis in RESULT.md supplies the continuous sharp moment interval, its endpoint classification, the universal reconstruction theorem, and the cube-root inverse bound. Neither quadrature nor a finite parameter census establishes those statements. The moment inversion is algebraic; no external formal proof assistant or independent audit was used. Historical priority is provisional because an equivalent inverse theorem might have appeared alongside a known all-order forward-moment formula.
