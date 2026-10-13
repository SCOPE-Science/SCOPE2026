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

# Verification and scope

Run `python3 verify.py` with Python 3; no third-party modules, randomness or network are required. The checker reconstructs all four forms over a sparse exact polynomial ring, verifies the six pairwise difference identities, four smoothness determinants, the gradients at the unique tacnode shared by the two nodally intersecting conics, and the four asserted projective transformations. It also checks the surviving coordinate substitution formula symbolically in the parameter.

The exclusion conditions are `r != 0`, `r*r != 1`, and `r*r != -1`, ensuring four smooth distinct conics, distinct node roots and distinct tangency points. The proof of stabilizer completeness rests on preserving the uniquely marked unordered component pair and its two-node secant, unique tacnode and tangent; comparing the unordered node pair eliminates the shear and restricts a coordinate ratio to a sign, and the nonzero mixed coefficient restricts the final ratio to a sign. These are exact universally quantified arguments, not extrapolations from samples. The verifier corroborates but does not replace them.

No independently conducted audit or third-party validation is asserted.
