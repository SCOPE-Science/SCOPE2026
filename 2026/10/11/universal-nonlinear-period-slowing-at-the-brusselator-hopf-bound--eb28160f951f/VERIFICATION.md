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

# Verification and reproducibility

Execute `python verify_brusselator.py` with SymPy installed. The checker symbolically substitutes the inverse coordinate map into the original Brusselator, confirms the exact scalar equation, tests the entire order-two Fourier solution, evaluates both order-three fundamental Fourier integrals, verifies the solved Hopf coefficients, and proves the period coefficient and a positive-square decomposition. These are exact algebraic/trigonometric checks, not a numerical extrapolation.

The nondegenerate Hopf theorem (transverse trace crossing and nonzero cubic amplitude coefficient) supplies a local stable cycle and an analytic expansion in the squared amplitude. The checker's outputs alone are not a substitute for this existence argument. The statement is local at fixed positive feed \(A\); higher-order terms, global periods and full priority over older inaccessible studies are not established. Independent audit has not been performed.
