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
The verification reconstructs the Figure 3 equilibrium from the printed parameters and evaluates the printed reaction terms directly.

Checks performed:
- solve the reduced positive-equilibrium cubic near the state printed in the Figure 3 initial condition;
- confirm both reaction residuals are below numerical tolerance;
- evaluate all four analytic Jacobian entries;
- compare the analytic Jacobian against central finite differences;
- verify negative zero-mode trace and positive zero-mode determinant;
- verify the modal determinant is strictly positive for every nonnegative spatial eigenvalue for the Figure 3 diffusion pair;
- recompute the modal determinant at the marked value \(k^2=0.83\);
- repeat the sign test for the Figure 4 diffusion pair.

The replay prints `VERIFY_OK` when all checks pass.

Limits: floating-point arithmetic is used only for a parameter point with large sign margins. The all-mode conclusion follows analytically once the reconstructed coefficients have the displayed strict signs. No independent audit has been performed.
