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

# Reproducibility and limitations

From this folder execute `python3 verify_cartier.py` (requires `sympy`) and `python3 verify_field_rank.py` (standard Python 3). Both were executed successfully on the packaged source. The former regenerates the complete Cartier coefficient matrix, confirms its nine nonzero entries, the rank-seven smooth-domain pivots, the exceptional \(Q\) polynomial, and the separable degree \(3+3+4+6\) factorization. The latter independently obtains the Cartier matrix by polynomial multiplication and calculates ten-fold Frobenius-twisted stable ranks at representatives of each irreducible exceptional factor in its splitting field, shifted generic controls, and every smooth \(\mathbb F_7\) parameter.

A finite-field enumeration alone would not prove the universal assertion for all algebraically closed fields. That assertion is instead supplied by the coefficient formula, the explicit rank blocks and four-cycle contraction in `RESULT.md`, and polynomial identities in \(\mathbb F_7[u]\). No full Jacobian group structures, Newton polygons, or isomorphism classifications are verified. No independent external audit has been performed.
