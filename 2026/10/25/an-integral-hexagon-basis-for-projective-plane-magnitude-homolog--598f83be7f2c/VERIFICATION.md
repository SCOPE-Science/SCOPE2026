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
# Verification of the integral hexagon basis

Execute `python3 verify_hexagon_magnitude.py` (Python 3 plus SymPy) without external inputs.

The checker reconstructs the point–line incidence graph of the Fano plane from three-bit vectors and orthogonality, independently enumerates all endpoint-localized magnitude chains of length four, builds the two integer boundary matrices using exact graph distances, verifies the chain-complex equation, and computes exact Smith normal forms. Expected primitive Smith data:

- Equal endpoints: chain ranks \(6,18,15\), boundary ranks \(6,12\), with all six and all twelve nonzero Smith invariants respectively equal to one. Therefore integral \(\operatorname{MH}_{3,4}^{P,P}\) vanishes.
- Distinct same-type endpoints: chain ranks \(9,24,11\), boundary ranks \(9,11\), and the matrix adding the four explicit candidate cycles has rank fifteen and all fifteen nonzero Smith invariants one. This is an exact integral basis test.
- All \(168\) invertible \(3\times3\) binary matrices are checked for preservation of Fano incidences, natural action on hexagon chains, and simple transitivity on \(168\) ordered noncollinear point triples; polarity exchanges point/line labels. This confirms the full \(336\)-element regular action.

Expected markers: `EQUAL_ENDPOINT_INTEGRAL_H3_VANISHES`, `FOUR_HEXAGON_CLASSES_INTEGRAL_BASIS`, and `FANO_336_FULL_AUTOMORPHISMS_REGULAR_ON_HEXAGON_BASIS_VERIFIED`.

The checker supplies a complete finite integer computation for the Fano-specific equal-endpoint fact; the formula for arbitrary projective planes is independently established by the written integer unit-pivot proof. No claim of external or independent audit is made.
