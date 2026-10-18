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

# Computational and analytic verification

The physically timed polynomial model was reduced exactly to a scalar second-order equation and reconstructed by an explicit algebraic recovery formula. A third-order Poincaré–Lindstedt expansion produces two resonant identities, and both are checked symbolically in `verify.py`, together with the second-order forced-harmonic solution and the algebraic coefficient identities. The proof uses standard nondegenerate Hopf bifurcation theory to justify the orbit and smooth expansion; no finite computation substitutes for that step.

The same standalone script solves the original translated two-variable ODE as a periodic two-point shooting problem in five numerical cases. The recurrence errors and observed-versus-predicted quadratic period coefficients appear in `verification_output.txt`. Each numerical test is only corroboration near nonzero amplitude; it does not certify uniform error bounds, the entire parameter region, or independent validation.

Exact prerequisites: Python 3 with SymPy, NumPy, SciPy. Run `python verify.py` in the extracted directory. No external file, private data or network connection is required. The generalized-Hopf set and nonlocal cycles remain unassessed.
