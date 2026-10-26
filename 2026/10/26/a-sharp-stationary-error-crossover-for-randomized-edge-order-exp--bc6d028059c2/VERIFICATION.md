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

Run `python verify.py` with Python 3 and SymPy. The verifier explicitly constructs all six products of the three stochastic edge exponentials and checks the stationarity solutions, covariance contraction and forcing polynomials, both exact squared-error difference factorizations, and exact rational sign samples. The analytical proof in RESULT.md, not a finite grid of numerical tests, proves the universal inequalities, uniqueness of the threshold, and all initial-condition statements.

An independent scientific audit has not been performed. The literature comparison covers the specified sources, and the abstract-only related balanced-splitting article remains a priority risk. The mathematical conclusion is restricted to independently permuted three-edge flows on the unit-rate directed triangle.
