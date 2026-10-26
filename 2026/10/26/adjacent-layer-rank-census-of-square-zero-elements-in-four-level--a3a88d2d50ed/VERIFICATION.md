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

# Reproduction

Run `python3 check_square_zero.py` with Python 3 and its standard library. The script enumerates all radical block configurations for eleven dimension and field choices, checks every coefficient of the adjacent-rank profile formula by direct arithmetic and row reduction, and tests 196 matrix-rank counting identities. It uses the irreducible binary polynomial `z*z+z+1` for the four-element field. Successful recorded terminal output ends with:

`ALL_FOUR_LAYER_SQUARE_ZERO_CHECKS_PASSED 11 and 196 rank-count identities`

# Proof boundary

This finite enumeration is corroboration only. The infinite family theorem follows algebraically from the explicit three block-product constraints, standard rank-matrix counts, and the dimension formula for the image of the coupling map. Priority among all mathematics publications is not independently certified. Independent mathematical audit has not been performed.
