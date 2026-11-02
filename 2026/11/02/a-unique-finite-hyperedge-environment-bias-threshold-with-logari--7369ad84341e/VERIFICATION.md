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

# Reproducibility and limits

Run `python VERIFY.py` with Python 3 and SymPy installed. The checker verifies the exact response derivative, monotonic curvature-numerator identity and endpoint values symbolically; computes two- and three-member formulas exactly; tests rational two-state balance for multiple cooperative fractions and integer sensitivities; and numerically brackets representative sensitivity roots using deterministic bisection.

The final output is `PASS: symbolic identities, exact rational fixed-size cases, balance equations, and critical-point brackets`. These checks validate algebraic certificates and examples; they are not a computer proof of the general asymptotic limit. The all-group-size assertion is supported analytically by binomial moments and Taylor remainder control; the large-sensitivity statement is supported analytically by a two-sided sign-bracketing limit.

The environmental composition is sampled initially and thereafter frozen. Neither this checker nor the proof demonstrates dynamic evolutionary equilibrium or independence of interacting network groups. Independent scientific audit has not been performed.
