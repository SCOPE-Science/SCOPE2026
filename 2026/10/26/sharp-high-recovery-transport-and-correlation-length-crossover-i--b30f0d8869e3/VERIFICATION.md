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

The analytical theorem follows from the exact source stationary-current and transfer-eigenvalue formulas. A positive-root count using a polynomial coefficient sign change proves uniqueness for all positive rate ratios; the implicit-function expansion at the unique root gives the optimized coefficients. The logarithm of the exact second-to-first transfer-eigenvalue ratio gives the correlation-length coefficients.

The standalone `verify_tep.py` script was run with Python, SymPy, NumPy, and SciPy. It passed 67 distinct groups of symbolic and numerical assertions: eleven symbolic identity and asymptotic-series groups, twenty-four independent current/optimization groups, twelve fixed-density correlation-asymptotic groups, and twenty optimizing-limit and susceptibility groups. Independent density-coordinate optimization was compared against the derivative-polynomial root. The script states all tested parameter values and tolerances.

Limits: numerical observations are not proofs of all-parameter uniqueness or all-order asymptotics; these claims are proven separately. No full finite-system Markov generator computation was necessary for the thermodynamic consequences. Independent scientific audit and external priority validation have not been performed.
