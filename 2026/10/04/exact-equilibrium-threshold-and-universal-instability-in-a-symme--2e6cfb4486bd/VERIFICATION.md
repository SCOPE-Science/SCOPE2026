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
The bundled `verify.py` performs exact symbolic checks against the printed vector field. It verifies:

1. the equilibrium parametrization \(E_\pm(t)\) and the parameter map \(\nu=\Phi(t)\);
2. the derivative identity \(\Phi'(t)=P(t)/(5(t^2+t+1)^2)\);
3. the Jacobian characteristic polynomial and all three coefficient formulas;
4. the Routh determinant identity \(a_1a_2-a_3=N(t)/(20t)\);
5. that the two coordinate relations printed in the source leave a nonzero unresolved second-equation residual unless the missing scalar condition is imposed; and
6. a numerical replay at \(\nu=0.21\), yielding exactly two eigenvalues with positive real part and one with negative real part.

A successful replay prints `VERIFY_OK`.

The checker confirms algebra and one numerical example. The universal root count is established by the analytic Routh and no-imaginary-axis-crossing argument in `RESULT.md`, not by finite sampling.
