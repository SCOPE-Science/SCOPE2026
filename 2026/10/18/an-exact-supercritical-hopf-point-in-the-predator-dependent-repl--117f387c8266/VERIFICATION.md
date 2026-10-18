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

# Reproducing the exact crossing and negative Hopf coefficient

Install dependencies from `requirements.txt` in a standard Python environment, then run `python verify_supercritical_hopf.py` from the directory containing both files. The standalone code uses only `sympy` and `mpmath`; it performs no network calls and requires no saved simulations.

The verifier performs, from the original three-dimensional equations, exact rational reconstruction of the scenario's payoff matrices, the coexistence branch, and its Jacobian. It asserts the exact identity between the Routh–Hurwitz determinant and the integer polynomial divided by its rational denominator, checks opposite exact signs at two rational endpoints, and encloses a strictly positive polynomial derivative throughout the interval. Every linearization coefficient, coordinate positivity constraint, and nonzero crossing derivative is checked by interval arithmetic.

For the first Lyapunov coefficient, the code differentiates the original field twice and three times, constructs normalized eigenvectors at the imaginary pair, solves the two required complex three-dimensional systems by interval Cramer's rule, and contracts the second- and third-order tensors. It asserts that both real and imaginary parts of the eigenvector residual intervals contain zero. The output enclosure obtained during replay is contained in \((-0.545928,-0.545926)\). This verifies the **negative sign** for the specified eigenvector convention; changing the amplitude normalization changes its magnitude but not the Hopf type.

Finite-time trajectories are not being used as a proof. The theorem of Hopf bifurcation gives small local stable cycles for sufficiently small positive \(K-K_*\), without claiming a numerical estimate of the existence-neighborhood size or global convergence. The dependency-library implementations have not received an independent audit in connection with this result.
