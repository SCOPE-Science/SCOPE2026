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

The checker `check_quantum_square_zero.py` constructs the eight-dimensional PBW multiplication table directly from the defining relations, enumerates all radical elements, tests multiplication squares without relying on the theoretical coefficient equations, and determines multiplication ranks by Gaussian elimination over each field. The complete run covered ten field-parameter cases: all nonzero parameters of the fields of sizes two, three, four and five. It printed `QUANTUM_EXTERIOR_SQUARE_ZERO_OK 10 exhaustive field-parameter cases` with no assertion failure.

The characteristic-two nontrivial deformation is represented over the four-element field, whose arithmetic is implemented using its irreducible quadratic polynomial. The primitive-fourth-root resonance is represented over the five-element field. The general component classification, Grothendieck-ring identities and rank theorem are proved symbolically in `RESULT.md`; finite tests alone do not establish claims for arbitrary fields.

No independent audit has been performed. The geometric assertions concern the reduced variety, and no claim about the original possibly nonreduced scheme is certified here.
