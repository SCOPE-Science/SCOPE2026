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

# Reproduction and verification

The proof is self-contained in `RESULT.md`. Run `python3 verify.py` with Python 3 and SymPy installed. The script recomputes the spherical-cap matrix Hessian exactly, verifies its determinant and discriminant algebraically, checks the exact transition root \(2+\sqrt6\), confirms the negative midpoint curvature certificate using *rational* radical brackets, and constructs the strict geometric inequalities ensuring the sample is a genuine mixed lens fiber.

Verified output: `VERIFY_OK: exact second derivative, Hessian determinant/discriminant, threshold root, strict radical sign, and mixed-fiber realization`.

Finite computation does not establish the universal quantifiers by enumeration; the exact analytic matrix-Hessian argument and the all-radius lens realization do so. No external independent audit or certification is claimed. Results apply to smooth mixed fibers only, and historical literature coverage is necessarily nonexhaustive.
