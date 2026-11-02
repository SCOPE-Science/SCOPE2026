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

The proof uses indefinite finite-pebble games, not bounded-depth extrapolation. The two Python programs use only Python's standard library, reconstruct the structures from their integer dimensions, and apply existence-only type refinement without counting. The included outputs are reproducible by running the scripts from the package root.

`verification/verify_two_equiv_grid.py` checks non-counting logical refinements for small full and punctured grids at widths two, three, and four. `verification/verify_equiv_two_pebble.py` independently checks two-pebble transition types across a larger rectangular range. Finite computation does not certify the universal quantifiers over all dimensions or all quantifier depths; those follow from the explicit game invariants in RESULT.md.

Every relation in the scripts is reflexive as required; a punctured cell is absent from the induced domain, not replaced by a marked element. Neither coordinate orientation is silently swapped.
