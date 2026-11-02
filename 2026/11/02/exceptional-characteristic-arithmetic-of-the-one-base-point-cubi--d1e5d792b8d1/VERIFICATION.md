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

# Verification of the arithmetic plane-pencil theorem

The standalone script `verify_pencil.py` runs with Python 3 and SymPy. It recomputes the resultant \(x^9\), the exact genus-one double-cover quartic and its classical discriminant, the characteristic-two and characteristic-three Gröbner bases, the characteristic-two nodal tangent form, the characteristic-three local cusp equation, and the characteristic-three Hasse invariant coefficient.

The script exhaustively enumerates all projective points and all finite and infinite parameters over \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_3,\mathbb F_9\). Actual terminal output concludes with `ONE_BASE_POINT_BAD_CHARACTERISTICS_AND_ARITHMETIC_COUNTS_PASS`. Finite arithmetic examples are cross-checks only: the theorem for all extensions follows from the proved Jacobian equalities, geometric singularity types, and normalization argument. The script does not compute Kodaira resolutions or certify historical priority. Independent audit has not been performed.
