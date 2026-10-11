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

The attached `verify.py` is a standalone standard-library script. Execute `python3 verify.py` from the package directory. It checks the exact polynomial identity used for the quartic critical-point calculation using integer coefficient arrays; evaluates 200 deterministic exterior/interior pairs via independent angular golden-section minimization; and checks three tangential finite-difference derivatives against the displayed Jacobian formula. The run returned `VERIFY_OK polynomial_identity=1 random_pairs=200 tangential_derivatives=3 exact_constant= 1.211565031277261`.

The mathematical proof is the KKT parametrization, exact derivative norm, monotonicity with outward distance, segment integration, and rational critical-point optimization in RESULT.md. Numerical optimization does not certify the global supremum or general-exponent assertions. The test's angular optimizer is restricted to the positive quadrant, exploiting the coordinatewise sign preservation proved in RESULT.md. No independent mathematical audit has been performed.
