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

The reproducible symbolic certificate is `verify_symbolic.py` (SymPy, exact integer polynomial arithmetic): it verifies the tangent coefficients, eliminants, resultant, degree-one subresultant, exceptional polynomial discriminant, and numerator-divisibility identities. Its observed terminal marker was `SYMBOLIC_HYPERFLEX_OK`.

The separately implemented modular verifier is `verify_modular.py` (SymPy's finite-field polynomial algorithms): it checks the exceptional-polynomial degree, squarefreeness, boundary avoidance, invertibility of the subresultant coefficient, and existence of the predicted contact point in characteristics \(5,7,11,13,17\); it additionally checks the irreducible factors in characteristics \(5,7,11\). Its observed terminal marker was `MODULAR_HYPERFLEX_OK`.

The proof of the universal characteristic statement is the integer-polynomial identity plus the separate characteristic-eleven coefficient check; the finite modular checks are supplementary tests, not a substitute for proof. Geometric square and cube roots are used only after the algebraic closure hypothesis. The isomorphism criterion is cited rather than reproved. Independent external audit has not been performed.
