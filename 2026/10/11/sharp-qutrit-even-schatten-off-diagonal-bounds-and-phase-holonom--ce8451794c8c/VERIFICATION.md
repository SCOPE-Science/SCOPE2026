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

Run `python verify.py` with Python 3.10+ and NumPy. The verifier independently constructs Cayley–Hamilton trace-moment recurrence polynomials using rational arithmetic, checks their weighted degree and their exact values for the eigenvalue triple \((2,-1,-1)\), and confirms strict dependence on the cubic-trace square for even orders 6–32. It samples 3500 reproducible positive complex qutrit density matrices, checking purity, cubic moments, sixth-moment identity, and five even Schatten bounds. It checks 4355 grid points of phase and mixing strength against the analytic determinant positivity condition and tests the two equality branches, including rejection of the negative branch for mixing strength above one half.

Actual replay on the accompanying `verify.py` returned:

`VERIFY_OK checks=41205 exact_trace_recursion=60 random_density_matrices=3500 phase_grid=4355`

Finite sampling cannot establish sharpness for all purities, dimensions, or powers. Analytic proof of the entire statement is in `RESULT.md`. Complex matrices and the fixed basis are essential; positivity excludes the negative triangle phase above purity one half. No external mathematical audit has been performed.
