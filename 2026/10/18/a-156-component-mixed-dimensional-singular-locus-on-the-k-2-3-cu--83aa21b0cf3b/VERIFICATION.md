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

The exact standard-library face checker `check_cut23.py` was run from the package and produced `VERIFY_OK`, counting 16 vertices, 36 facets, 729 nonempty faces, 144 maximal nonsimple three-faces, and 12 maximal nonsimple square faces. It checks active-facet descriptions and transverse primitive-ray relations. Independent audit has not been performed.

The characteristic-independent proof in `RESULT.md` uses the saturated vertex-difference lattice, exact orbit-face order, and dual affine toric semigroups. Exhaustive enumeration of finitely many faces verifies the finite combinatorial portion; it is not a substitute for the all-field semigroup arguments. Nonreduced Jacobian structure and nongeneric intersections are not asserted.
