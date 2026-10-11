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

The numerical claim can be replayed with `verify.py`, which uses only the Python standard library.

The checker reconstructs the exact rational cubic for the homogeneous positive equilibrium and checks its exact negative discriminant; brackets and solves the unique real root and verifies both reaction equations; evaluates the paper's reported point and confirms nonzero residuals; reconstructs \(p_1,q_1,p_2,q_2\) and the modal determinant for \(d=0.12\); checks that the critical-value function is decreasing from the first spatial mode onward; verifies \(\varepsilon_c=0.00852879885272517\ldots\) and the spectral signs; and independently evaluates the source's rounded formula as \(0.00959299911177703\ldots\).

The verification is a check of the source's printed linearized model and the explicit \(d=0.12\) parameter slice. It does not reproduce the PDE figures, determine their implementation parameters, or certify nonlinear pattern formation.
