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

# Reproducibility

Run `python3 VERIFY_COMPUTATION.py` using Python 3 and its standard library. The script constructs the seven vertices and an explicit determinant-one lattice map to the four-cycle stable-set polytope, enumerates all independent four-vertex supports, derives the eight primitive facet inequalities, exhausts their nonempty intersections, checks normal-cone smoothness by exact saturated-lattice minor gcds, and proves that the five nonsmooth edge cones have unit-square primitive relations. It prints `VERIFY_OK` on successful completion.

The checks use exact integers and rational fractions; no floating-point approximation, stochastic testing, symbolic black-box algebra, external package, or unavailable input is involved. The resulting complete finite face data are tied to the projective toric orbit-cone correspondence and saturated-unit-square conifold argument in `RESULT.md`. No inference is made about larger alternating-sign-matrix polytopes.

The reduced singular scheme is classified set-theoretically. The Jacobian scheme and local rings at the two triple fixed points are not computed. Novelty searches cannot rule out unlocated mathematically equivalent results. Independent audit has not been carried out.
