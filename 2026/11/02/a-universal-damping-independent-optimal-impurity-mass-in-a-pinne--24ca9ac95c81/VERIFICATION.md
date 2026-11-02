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

Run `python checker.py` with Python 3, SymPy, NumPy and SciPy. `checker.py` reconstructs the exact six-dimensional covariance model from stated physical parameters, sets left and right temperatures to one and zero using linearity, solves all 21 symmetric equations exactly, verifies all 36 entries of the resulting Lyapunov residual, and checks the exact flux formula, factored derivative, discriminant identity and rational example. Twelve independent SciPy Lyapunov solves test parameters spanning distinct central masses, spring and pinning values, and friction strengths. A successful run prints a one-line JSON record with status `PASS` and maximum absolute numerical error below \(7\times10^{-15}\). `checks.json` contains the output obtained for this package.

The symbolic checks are finite algebraic identities with universal positive symbolic parameters, not finite numerical extrapolations. The proof of denominator positivity and all-parameter global optimality is given in `RESULT.md`. The result is not independently audited; a close mass-alternating 2010 article remained abstract-only and is recorded as an originality risk.
