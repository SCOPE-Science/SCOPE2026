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

# Verification

Execute `python verify.py` with Python 3 and SymPy. The verifier reconstructs exact density matrices and partial transposes from the specified pure-state amplitudes in local dimensions 2, 3, 4, and 5. It computes all negative partial-transpose eigenvalues algebraically and compares their trace norms to the closed formulas. It also checks the symbolic second derivative, an exact positive qutrit witness, and six finite-dimensional numerical evaluations of the globally maximizing scalar equation.

The uniform sign theorem, unique optimizing parameter for every dimension, and sharp limit are proved in `RESULT.md` without dependence on these finite tests. The packaged code does not check all dimensions or exhaust all states outside the stated family. No external or independent audit has been carried out.
