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

# Verification and reproducibility

Execute `python3 verify.py` in this directory with Python 3 and SymPy installed. The checker is standalone: it independently forms full rational transition matrices from the edge sets of twelve regular bases, compares their characteristic polynomials to the predicted two-subspace factorization, tests stationarity and detailed balance, and evaluates the rational consensus variance. Four rational hub-copying rates per graph give 48 complete-matrix instances. A symbolic derivative identity and 97 additional exact size/variance comparisons give 145 reported finite instances.

Actual execution result: `PASS: 145 exact full-matrix/variance instances; tested 12 regular periphery graphs including connected, disconnected, bipartite and nonbipartite examples.` The checker ran against this file's code before delivery. No stochastic simulation, floating-point agreement alone, or assumption of an enumerated infinite family is used as a proof. The all-size assertion is established by the invariant-subspace decomposition and exact scalar optimization in `RESULT.md`. The finite computations only test implementation, signs, multiplicities and boundary formulas.

Limitations: the included tests do not constitute an independent proof, independent specialist audit, or complete bibliographic priority determination. Independent audit status remains not performed.
