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

# Verification of the consecutive Stern-polynomial resultant classification

Run `python3 verification/verify.py` in a directory containing this file and the referenced script. The checker uses exact integer polynomial coefficients, independently derived binary degree/leading-coefficient data, and a Sylvester-matrix determinant evaluated by exact Bareiss elimination. No external Python package is required.

The replay checked 259 exact Sylvester determinants for \(1\le n\le259\), 16 arbitrary-integer realization witnesses \(1\le m\le16\), and four further distinct indices retaining the same resultant for each witness. It additionally checked boundary values and the special-degree behavior at index 39. The checker reported:

`VERIFY_OK: 259 independent Sylvester determinant comparisons; 16 exact surjectivity witnesses, each with 4 recurring-value checks; binary degree/leading-coefficient invariants confirmed`

The checks are finite. The universally quantified conclusion follows from the explicit induction and resultant laws in `RESULT.md`, not from the finite replay. Signed resultants and common-root assertions modulo primes are outside the theorem.
