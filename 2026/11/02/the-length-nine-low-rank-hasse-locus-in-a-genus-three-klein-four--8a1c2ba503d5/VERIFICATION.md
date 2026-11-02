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

# Reproducibility

With SymPy satisfying `requirements.txt`, run `python verify.py`. The script exactly checks the integer discriminant, the characteristic-seven hyperelliptic Hasse matrix, its three factors, the saturated Gröbner basis, the degree-nine standard-monomial quotient, all seven smooth geometric support candidates, transversality at the six rank-one points, and the quadratic local ideal at the origin. The full smooth-parameter enumeration over the prime field is a supplementary check; it is not the proof of completeness over the algebraic closure.

The symbolic calculations use `sympy.Poly(..., modulus=7)` and algebraic elimination with the equation `z*D-1`. Reproducibility is computational; it does not constitute independent scientific certification. See `RESULT.md` for the mathematical proof and precise limitations.
