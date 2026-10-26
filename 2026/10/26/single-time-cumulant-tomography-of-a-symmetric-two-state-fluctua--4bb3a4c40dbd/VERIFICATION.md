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

# Reproduction and limits

Run `python verification/checker.py` with SymPy and mpmath installed. The checker separately (i) verifies the ordered-integration partial fraction formula for \(I(x)\); (ii) checks the symbolic derivative identity for the ratio and its initial coefficients and endpoints; (iii) computes the displacement cumulants independently by a telegraph matrix-exponential formula at four admissible positive parameter points using 70-digit arithmetic; and (iv) recovers the input switching and diffusivity contrast from the observed cumulants. It prints all tested parameter points and ends with a success message only when its assertions pass.

These finite computations do not verify the infinite strict-monotonicity assertion by enumeration. Its justification is the explicit analytic series coefficient formula and sign proof in RESULT.md. No statistical finite-data performance, unequal switching rates, or independent external audit has been checked.
