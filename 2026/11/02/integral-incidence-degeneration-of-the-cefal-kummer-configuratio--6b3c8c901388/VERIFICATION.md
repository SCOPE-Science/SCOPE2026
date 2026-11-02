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

# Verification record

The public standalone checker `verify_incidence.py` was executed with the Python standard library and produced the success marker `CEFALU_INTEGRAL_INCIDENCE_96_HORIZONTAL_16_VERTICAL_CHAR3_AND_CHAR2_THICKENING_PASS`.

The checker expands the integer quartic and verifies both exceptional characteristic square identities coefficient by coefficient, confirms nonsingularity of the characteristic-two quadric's alternating polar matrix, computes the sixteen marked sign representatives and their complete pairwise incidence table, verifies 96 ordinary and 112 characteristic-three incidences with 16 additional diagonal pairs, and checks determinant \(3\) up to sign for the relevant rank-four integral character-algebra incidence multiplication map.

The checker does not prove that no hidden scheme-theoretic components exist. That fact follows from the explicit presentations of each of the sixteen disjoint componentwise incidence rings in the written proof. Finite examples are not used as an infinite proof. The geometric interpretation is limited to the marked closures of the Catanese integer model; independent validation has not occurred.
