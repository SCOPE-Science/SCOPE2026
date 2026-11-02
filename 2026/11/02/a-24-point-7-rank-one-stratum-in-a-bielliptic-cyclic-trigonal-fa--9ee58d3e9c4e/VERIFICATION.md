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

# Verification

The complete result is proved by the Cartier differential basis and exact polynomial identities in `RESULT.md`. Independent machine verification consists of two source programs in this package.

Run `python3 verify_symbolic.py` with SymPy installed. The program checks coefficient extraction, five explicit Cartier coefficients, the discriminant, the determinant identity, the rank-one factorization, correct Frobenius-twist order, the degree-24 equation, the factorization into eight irreducible cubics, and the absence of intersections with the smoothness discriminant. It prints `SYMBOLIC_GF7_HASSE_DETERMINANT_AND_24_P_RANK_EXCEPTIONAL_PARAMETERS_OK`.

Run `python3 verify_fields.py` using standard Python. It reconstructs the defining sextic and its second and fourth powers directly over three finite fields, and independently evaluates every coefficient pair in each field. Its resulting smooth parameter counts by \((a\text{-number},7\text{-rank})\) for \(\mathbb F_7\), \(\mathbb F_{49}\), and \(\mathbb F_{343}\) are respectively \((37,6,0)\), \((2311,42,0)\), and \((116965,318,24)\) in the three theorem strata; the singular counts are \(6\), \(48\), and \(342\). It prints `DIRECT_F7_F49_F343_FOUR_DIFFERENTIAL_CARTIER_CLASSIFICATION_OK`.

The finite checks alone would not prove the universal geometric classification; the symbolic proof does. The status here denotes only the recorded self-review. No independent external audit or validation has been performed.
