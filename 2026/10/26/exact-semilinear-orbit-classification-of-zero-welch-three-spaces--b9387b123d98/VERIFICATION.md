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

# Exact finite-field verification

Run `python3 welch9_orbits_verify.py` with Python 3 and no third-party packages. The script constructs the quotient field using `0x211` for the irreducible polynomial, tests irreducibility by polynomial gcd at Frobenius degrees 3 and 9, enumerates every normalized linear three-space through one, and evaluates each eight-term Welch sum without floating-point arithmetic. It computes all four scalar-normalization classes, the Frobenius class permutation, the unique subfield-stabilized example, and the explicit generic example. An independent 511-term trace evaluation gives Kloosterman value -5 and reproduces the published count formula.

Expected checks:

`CERTIFICATE_OK irreducible_degree=9 normalized_spaces=10795 zero_normalized=22 kloosterman=-5`

`SCALAR_CLASS_SIZES [1, 7, 7, 7] FROBENIUS_CLASS_PERMUTATION [0, 2, 3, 1]`

`SEMILINEAR_ORBITS (73, 1533) TOTAL 1606`

The enumeration is exhaustive over a finite domain and constitutes a finite proof of the asserted orbit classification. The published counting theorem provides an independent cross-check, not the orbit decomposition. The verification does not address other extension degrees or independently validate earlier published theorems.
