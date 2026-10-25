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

The standalone `verify_color_character.py` program uses only Python's standard library. Running `python verify_color_character.py` prints `COLOR_CHARACTER_CHECKS_OK 192 direct_invariant_simplices 11504` after completing all assertions. It compares the theorem with exact orbit-quotient independence polynomials for 192 permutations and, independently for cases with at most 18 original vertices, computes the signed simplicial trace from every invariant independent face. No floating-point approximations occur in the combinatorial checks.

The infinite-family claim is proved symbolically in `RESULT.md` using a simplicial orbit model, elementary folding collapses, a two-state cycle transfer matrix and the established nonequivariant homotopy theorem. Exhaustive finite checks are not a substitute for these arguments. The calculation does not address integral representation lattices or simultaneous color-and-cycle symmetries.
