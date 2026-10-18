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

# Verification of the mathematical claim

The independent audit has **not** been performed. The checks below are the reproducible computations used in the self-review.

Run `python check_symbolic.py` with SymPy. It reconstructs the equilibrium and Jacobian, verifies the entire Hopf parameterization, computes the quadratic homological transformation directly, extracts the cubic resonant coefficient, and checks the real and imaginary components using the exact relation \(\omega^2=k^2-F^2\). It also checks the explicit period coefficient, derivative, quartic root condition, and value \(C(1/3)=16\). This script was executed successfully on the included source file.

Run `python check_shooting.py` with SciPy and NumPy for independent *numerical corroboration* only. It solves the actual ODE periodic shooting boundary conditions at \(t=1/4\) and \(t=1/2\) for four decreasing excursions, then measures the period relative to the actual equilibrium focus frequency. The observed coefficients approach the analytical values. These finite experiments are neither an exhaustive classification nor an infinite proof.

The universal statement depends on the analytical time-preserving Hopf-normal-form calculation and a strict sign/monotonicity argument. The scope is local around each fixed point of the two-parameter Hopf curve; parameter endpoints, global cycle periods and spatially nonuniform reaction-diffusion solutions are not covered. The complete original 1984 chemical-oscillator article was not inspected, so historical publication priority remains uncertain.
