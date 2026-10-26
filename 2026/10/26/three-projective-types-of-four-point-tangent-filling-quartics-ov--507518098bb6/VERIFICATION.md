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

# Reproduction and boundaries

The attached scripts are standalone when kept together in their package directory. Python 3, NumPy and SymPy are required for the three exhaustive scripts. Run `enumerate_tangent_quartics.py`, `check_geometric_smoothness.py`, `classify_projective_orbits.py` in that order, then `verify_representatives.py` (pure Python, independent of the other scripts). Each step writes its claimed data from exact finite arithmetic. Reference outputs, 378 candidate coefficient vectors, the 234 accepted vectors, and their three-orbit partition are included.

The geometric-smoothness test uses polynomial ideals on all three affine charts over F3; the unit-ideal criterion is valid over the algebraic closure. The numerical finite-field point test alone is not treated as a geometric smoothness proof. Group orbit identification is under projective coordinate changes over F3; no geometric isomorphism statement is made.
