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
# Reproducibility and scope

Run `python3 verify.py` in the directory containing the included Python 3 standalone program. It has no third-party dependencies. A successful run emits `VERIFIED` and verifies the following expected totals:

- Marked constructions: \(16718\).
- Isomorphism classes after the three-maxima permutation action: \(3344\).
- Six fixed-set counts, sorted: \(68,68,1070,1070,1070,16718\).
- Vertex count range for the resulting Esakia posets: \(7\) through \(22\).

The verifier enumerates **all** normal-form choices (rather than sampling) and checks the induced partial orders by rebuilding their cover and transitive-closure relations. A second route performs Burnside counting from cycle orbits of admissible antichains. The written proof establishes why these normal-form choices exhaust all finite rooted regular posets with exactly three maxima and height four. The checker alone would not establish that conceptual exhaustive reduction; it tests the finite enumeration derived from it.

The duality identification uses a published theorem and is not separately reproved by the checker. Earlier equivalent counts might exist in sources not returned by the performed literature searches. No independent external audit is asserted.
