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

# Reproduction and limits

Run `python verify.py` from the extracted package directory. It uses only the standard library. It reconstructs the algebra multiplication from the presented monomial quotient, sets arbitrary unknown generator images, imposes all differentiated defining relations, obtains a basis of derivations using modular nullspaces, verifies every Leibniz identity on the algebra basis, and computes the dimensions of successive Lie derived terms from matrix commutators.

The actual run returned `CHECK_OK` for each of twelve cases: length vectors `(3,5)`, `(4,7)`, `(3,9)`, `(3,4,6)` over each of the prime fields of sizes `2`, `3`, and `5`, followed by `VERIFY_OK`. In particular, over prime field size `3`, `(3,9)` gave derived dimensions `(12,10,5,1,0)` and over prime field size `2` it gave `(12,7,0)`.

A finite-field calculation cannot prove a statement for every characteristic or every length vector. The proof in `RESULT.md` is the argument for arbitrary fields and all permitted parameters. The fully inspected equal-truncation automorphism normal form may imply the equal-height tangent case, but does not state this unequal-height derived profile. No independent mathematical review was performed.
