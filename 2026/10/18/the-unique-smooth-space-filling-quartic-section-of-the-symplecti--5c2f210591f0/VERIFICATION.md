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

# Exact verification

Run `python verify_tangent_census.py`, then `python verify_group_orbits.py`, then `python verify_geometric_smoothness.py` in a directory containing all three scripts; the last requires SymPy.

The enumeration checks all 65,536 independent quartic-section classes and their gradients at the fifteen rational points. The symmetry test exhausts orbit closures under fifteen symplectic transvections. Gröbner checks over the prime field test the common zeros of the two equations and the complete rank-deficiency ideal on each of four affine charts, including all algebraic extension points.

Verified expected values: quartic evaluation kernel dimension 20; quotient dimension 16; rationally smooth sections 288; unique tangent matchings 288; symmetry orbit sizes (144,144); Jacobian ideals for smooth representative are unit on all four charts and for the other representative non-unit.

No independent audit or independent external validation is asserted. No conclusions about curves on other cubic surfaces are drawn.
