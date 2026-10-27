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

# Verification of the D-optimal parallel-path shortcut theorem

The theorem is established analytically in `RESULT.md`, not by finite testing. The standalone executable `verify.py` uses NumPy, SciPy, and SymPy. Run `python verify.py` in a Python environment with those packages. The recorded output is `verify_output.txt`.

Actual computations on the package code: (1) nine path-length configurations, including both strict regimes and equality, checked against an unrestricted edge-by-edge nonnegative budget-constrained SLSQP optimizer; (2) nine direct reduced-Laplacian determinant comparisons against the product formula and budget identities; (3) three exact-rational reduced determinants independently enumerated as weighted spanning-tree polynomials; (4) three exact-rational path-edge permutation invariance checks. All reported checks passed.

The numerical optimizer is a finite diagnostic, not a certificate of global optimality. The strict-concavity, polynomial-invariance, and analytic KKT arguments in `RESULT.md` provide global uniqueness and validity for all stated integers and budgets. No computation or checker is asserted to prove an infinite statement independently.
