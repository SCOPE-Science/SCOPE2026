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

The proof uses equal-current conservation for stationary cycles, constrained Hessian inertia, uniqueness and strict convexity at the scalar threshold minimum, and the analytic implicit-function theorem for the asymptotic correction. These are fully developed in `RESULT.md`.

Execute `python checker.py` in an environment with Python 3 and NumPy. `checker_output.txt` is the output of the bundled file as executed on the package content. The diagnostics numerically test eight cycle sizes, signs of all nontrivial physical Hessian eigenvalues, and the two-term large-size expansion. Tests of finitely many sizes are not an infinite proof. The critical scalar equation is solved numerically for diagnostic purposes only; uniqueness is proved analytically.

No independent mathematical or literature-priority validation has been performed. Numerical floating-point precision is not used to decide the universal theorem. The sharp threshold is restricted to linear attraction in winding \(\pm1\), and nothing is claimed about nonlinear critical-fold stability or other stationary winding classes.
