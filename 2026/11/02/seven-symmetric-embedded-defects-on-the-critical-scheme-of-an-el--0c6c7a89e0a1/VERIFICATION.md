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

# Reproduction and verification

Run `python verify.py` in Python 3 with SymPy. The executed source constructs \(F=e_4(x_1,\ldots,x_6)\), computes its six derivatives in characteristic \(2\), obtains an exact Gröbner basis of size \(49\), and independently computes the Hilbert-series numerator by monomial deletion–colon recursion. It verifies the expected numerator \(1-6t^3+t^4+15t^6-13t^8-20t^9+35t^{10}-14t^{11}+t^{12}\), the reduced quotient polynomial \(21d+35\), the seven-frame Frobenius identities, and restriction-space dimensions for \(21\) lines in degrees \(0\) through \(8\).

The successful run prints `VERIFY_OK`. The exact Gröbner computation, local-rank and normalization arguments are described in `RESULT.md`; the program itself does not substitute for the characteristic-two support classification, geometric smoothness or uniqueness-of-priority reasoning. All calculations are exact, with no floating-point approximations. Verification is a self-review reproducibility check and not an independent audit.
