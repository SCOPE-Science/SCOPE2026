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

# Reproducibility and boundaries

The standalone `verification_check.py` reconstructs the original three equations with exact rational constants and asserts that the displayed positive point makes all right-hand sides vanish. It differentiates the full equations, asserts the exact Jacobian, expands the cubic characteristic determinant, checks all coefficient identities, factors the cubic Hurwitz determinant, verifies both radical expressions solve it, and establishes strict ordering and transverse derivative signs. It verifies signs at three positive effort-response speeds using rational arithmetic.

Run `python verification_check.py` with SymPy installed. The computations passed locally with exact assertions; the scientific justification for every positive speed is the polynomial sign proof in RESULT.md, not a sampled simulation. Neither a nonlinear Hopf normal form nor an infinite-parameter-space global orbit analysis was performed.

Independent audit and validation have not been performed.
