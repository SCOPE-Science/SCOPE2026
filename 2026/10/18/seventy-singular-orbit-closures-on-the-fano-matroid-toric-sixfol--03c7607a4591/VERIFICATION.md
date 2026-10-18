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
# Mathematical reproduction
Run `python3 verify_fano_singular.py` using Python 3's standard library. All incidence, affine rank, face-intersection, integer-minor, orbit, and saturation calculations are exact. The script emits `VERIFY_OK`, the complete six-entry proper face vector, \(308\) singular torus orbits, the three maximal-cone symmetry orbits, and generic class group `Z`. Its assertions are checked from the finite Fano matroid definition and the complete Edmonds rank-inequality description. Standard mathematical facts used externally to the script are the matroid-polytope inequality theorem and the toric regularity/orbit–face/class-group correspondence.

The checker establishes an exhaustive finite census, not an infinite computational extrapolation. Full-text overlap with the 2026 Fano-Gröbner paper was unavailable and independent mathematical audit has not been performed.
