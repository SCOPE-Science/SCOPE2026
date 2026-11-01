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

## Reproducible checks
The `verify.py` companion verifies the formula for the equilibrium branch, the exact cubic characteristic polynomial, and the critical algebraic identity \(ae+bd-aq=-(r\eta/2)G_t\) using SymPy. An independent numerical branch-root and Jacobian-eigenvalue sweep passes for 164 valid parameter combinations. The code runs with Python, SymPy, NumPy and SciPy using `python verify.py`.

The all-parameter conclusion depends on the analytical inequalities \(X'(t)>0\), \(0<q<e\), \(D>0\), and \(AB-C_0>0\), not on finite computations. No claims about global basins or larger graph sizes were checked. Independent audit has not been performed.
