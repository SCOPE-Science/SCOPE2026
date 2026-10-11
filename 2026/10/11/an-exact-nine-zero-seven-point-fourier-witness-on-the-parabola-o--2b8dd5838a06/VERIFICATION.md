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

The proof uses exact arithmetic in the degree-ten quotient by the eleventh cyclotomic polynomial. Run `python3 verify_parabola_seven_nine.py`, which needs only the Python 3 standard library. It checks the seven nonzero coefficient vectors and evaluates the Fourier sum for every one of the 121 pairs of field elements, comparing the resulting zero set against the nine-point list. The integer quotient is faithful because the eleventh cyclotomic polynomial is the minimal polynomial of the chosen primitive root.

A separate SymPy polynomial remainder check was used as an implementation cross-check and returned the same nine zeros; SymPy is not required to replay the included verifier. No claim about all seven-element supports, the sharp global maximum, or all primes is certified by this finite witness.
