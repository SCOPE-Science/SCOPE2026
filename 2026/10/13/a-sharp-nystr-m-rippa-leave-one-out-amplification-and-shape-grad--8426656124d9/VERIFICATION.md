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
# Verification scope

The analytically established result is the exact two-site regularized leave-one-out map, its sharp norm gap, the optimizing correlation, and the shape-gradient sign phase. The proof is in `RESULT.md`. Extract `verify.py` and run `python verify.py` with Python 3; it uses only the standard library.

The verification program was executed from its packaged path and returned:

`VERIFY_OK exact_two_by_two_loo_checks=2800 exact_shape_derivative_checks=2340 numeric_peak_comparisons=50000`

The 2,800 matrix checks use exact rational inversion and compare both residual maps; 2,340 additional rational checks evaluate the sign factor of the derivatives and the maximizing polynomial, and 50,000 floating-point checks compare a computed analytic peak against direct evaluations. The universal result and asymptotic limit rest on the displayed proof, not on these finite tests. The numerical test does not assess finite-precision RBF solvers or arbitrary dimension. No independent external audit has been performed.
