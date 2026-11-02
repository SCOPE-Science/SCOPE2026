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

The standalone file `verify_decomposed.py` constructs the fifteen unordered pair partitions of six symbolic branch roots and their Richelot coefficient determinants over the exact cyclotomic ring defined by \(\omega^2+\omega+1=0\). It checks the complete list of determinant norm factors, the special partition sets at \(s=0\) and \(s^2=-50\), and Frobenius fixed-point counts for all choices of the root permutation parameters. It also verifies coefficient-frequency identities in eighteen prime fields.

Command: `python3 verify_decomposed.py` (SymPy required). Observed terminal marker: `GENUS2_DECOMPOSED_RICHELOT_FROBENIUS_EXACT_PASS`.

The proof covers all prime powers \(q\) of characteristic at least seven. Finite prime tests alone would not establish that scope; the all-field proof uses universal polynomial identities and an algebraic Frobenius permutation argument. The proof explicitly restricts to geometrically decomposed quotients, not a base-field product of elliptic factors. Independent validation and historical novelty certification are not performed.
