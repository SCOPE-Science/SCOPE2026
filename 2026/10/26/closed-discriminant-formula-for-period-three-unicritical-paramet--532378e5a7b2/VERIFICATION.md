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

## Mathematical checks

The symbolic proof derives the period-three polynomial, the derivative factorization of \(h_d\), both required resultants, the composition resultant, and the discriminant sign. The standalone `verify.py` constructs the integer coefficient list of \(G_d\), computes its Sylvester determinant exactly with fraction-free Bareiss elimination, and compares the discriminant with the closed formula for \(d=2,\ldots,7\). All checks pass. For \(d=5\), the formula yields \(2^{48}101^4 431^4\); for \(d=7\), it yields \(2^{48}3^{54}19^{12}14731^6\), matching the period-three examples in Hutz–Towsley.

## Scope and limits

The exact proof covers every integer \(d\ge2\), while the program checks only the listed finite degrees. The result is a polynomial discriminant and does not establish a number-field discriminant, irreducibility, or any higher-period formula. The finite-characteristic interpretation is inherited from the published transversality criterion. Independent audit and external validation have not been performed.
