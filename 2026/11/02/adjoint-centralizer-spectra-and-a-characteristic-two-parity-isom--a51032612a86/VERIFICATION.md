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

Run `python3 check_census.py` with Python 3. It uses modular polynomial arithmetic for prime fields and specified irreducible quadratic polynomials for finite extensions, then builds each adjoint linear map directly from structure constants. The checker does not apply the valuation-centralizer argument to obtain the matrix rank: it computes the rank by independent Gaussian elimination over the field. It exhaustively evaluates 24 finite configurations and every allowable derivation coefficient vector within each configuration (10,678 total). It compares all nullity multiplicities and characteristic-divisible commuting-pair formulas.

Expected observed marker from an actual successful run:

`TRUNCATED_DERIVATION_ADJOINT_CENSUS_OK 24 10678`

The analytic proof, not finite experimentation, establishes formulas for all truncation lengths and field sizes. The characteristic-two affine Lie isomorphism is checked by symbolic bracket relations in the proof; no claim of external or independent audit is made.
