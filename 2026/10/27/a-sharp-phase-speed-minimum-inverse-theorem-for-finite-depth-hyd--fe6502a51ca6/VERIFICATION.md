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

The main proof is an exact symbolic argument based on strict monotonicity of two explicit hyperbolic functions, finite algebraic inversion, and a converse global-minimum check. Numerical replay of `checker.py` gave `PASS 800 forward/inverse and strict-bound checks; monotonic cases; critical scaling; 24 inverse target cases`. The tests require Python 3, NumPy and SciPy. They sample finite parameter families and are not exhaustive or a substitute for analytic quantifiers.

Critical definitions and endpoints are specified in `RESULT.md`. No finite-precision tolerance is part of the theorem; the strictly positive parameter domain excludes the equality boundaries. Independent audit and external validation have not been performed.
