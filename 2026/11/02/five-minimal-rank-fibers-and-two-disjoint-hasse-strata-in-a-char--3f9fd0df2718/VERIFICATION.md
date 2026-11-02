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

Run `python3 verify_symbolic.py` (requires SymPy) and `python3 verify_fields.py` (standard library only) from the same directory.

The first checks the actual degree-thirty expansion of the branch polynomial cubed in characteristic seven, the Cartier matrix, discriminant, Hasse determinant, elliptic quotient Hasse coefficient, boundary identities, factorization of the Frobenius-twisted scalar, and the prime-field marked-census.

The second recomputes the coefficients by ordinary finite-field convolution, directly constructs inverse-Frobenius-semilinear Cartier iterates, and uses row-reduction over separate explicit field implementations of sizes 7, 49, and 343. It exhausts all smooth coefficient-marked pairs over the first two fields and verifies all five claimed minimal-rank points in the third.

Expected success markers:

`EXACT_GENUS4_C6_P7_IDENTITIES_OK`

`F7_EXHAUSTIVE_CARTIER_OK`

`F49_EXHAUSTIVE_CARTIER_OK`

`GF343_FIVE_DEEP_POINTS_OK`

These checks support the formal polynomial argument for all geometric parameters. Numerical or finite-field enumeration alone does not prove geometric completeness. No independent audit or validation has been performed.
