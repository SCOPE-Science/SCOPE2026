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
# Reproduction and mathematical limits

Run `python verify.py` in a Python 3 environment containing `numpy>=2.0` and `sympy>=1.12`, as listed in `requirements.txt`.

The checker reconstructs the full transition matrix without relying on the quotient eigenvalue formula, checks matrix symmetry and stochasticity, and verifies the complete numerical spectrum against the independently calculated invariant decomposition. It tests all sizes from two through twenty-three, plus selected larger cases through sixty. Rational and symbolic identities confirm the low-size and high-size formulas for selected sizes. It checks the three-way positive subgradient identities in exact radical arithmetic for sizes eight through twenty-one. It also samples thousands of feasible two-orbit weights as a finite numerical stress test. Recorded execution: `VERIFY_OK 3292 exact/spectral/feasibility assertion groups; m=2..60`.

The supporting script is **not** a certification of all real transition weights or all integer sizes. Global optimality over infinitely many dimensions, including unrestricted non-invariant feasible kernels, follows only from the analytic convexity and spectral proof in `RESULT.md`. Originality remains a literature-based assessment and is not a mechanical proof. No independent mathematical audit is claimed.
