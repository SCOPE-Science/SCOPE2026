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

# Verification evidence and limits

The algebraic proof works over the integers for every finite, nonempty downward-closed set system. The only critical factorization is \(H=ZDZ^{\mathsf T}\), where the coefficient of a common subset is \((-2)^{|C|}\); \(Z\) is unimodular by cardinality ordering. All determinant and Smith assertions derive immediately, and \(H^{-1}\) uses explicit Möbius inversion. The modular count follows from the diagonal Smith factors, not from a numerical extrapolation.

Run `python verify.py` in an environment with SymPy for independent exact determinants and Smith forms of the explicitly enumerated finite test cases. The check also verifies the matrix product for the inverse and selected reductions. No floating-point tolerance is used. Finite computations do not establish the all-dimensional claim by themselves.

The identity does not imply sharp Euclidean condition numbers or any guarantee for non-downward-closed restrictions. Published treatment of general signed weighted incidence matrices remains an originality risk. Independent audit: not performed.
