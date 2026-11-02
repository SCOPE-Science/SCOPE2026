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

# Reproducibility and limits

The algebraic proof applies to every smooth parameter over the algebraic closure of \(\mathbb F_5\). Run `python verify_symbolic.py` with SymPy to check the exact Cartier polynomial, determinant, cubic discriminant and restrictions, and separability of the exceptional set; expected terminal marker: `EXACT_HASSE_DISCRIMINANT_AND_EXCEPTION_OK`.

Independently run `python verify_fields.py` in standard Python. It constructs the finite fields directly, squares the defining curve polynomial by coefficient convolution, computes Hasse matrices and Frobenius-twisted stable ranks, enumerates all smooth parameters over \(\mathbb F_5\) and \(\mathbb F_{25}\), and directly counts points for one rank-zero example over three successive extensions. Expected markers are `POINT_COUNT_F5_F25_F125_OK` and `GF5_GF25_FULL_CARTIER_STRATA_OK`.

The finite computations do not certify the global theorem by enumeration: unrestricted conclusions follow from the symbolic identities and semilinear argument in `RESULT.md`. The complex isomorphism-class quotient, excluded singular discriminant, other characteristics, Newton polygon and external audit are outside the claimed verified scope. No independent external audit has been performed.
