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

The `CHECK.py` file reconstructs the rational system at the Hopf equilibrium, verifies the Jacobian and transversal crossing, differentiates all nonzero second- and third-order entries, evaluates the full complex Hopf-resonance expression with the frequency dispersion identity, and checks the exact real/imaginary coefficient identities. It also differentiates the period coefficient, verifies the seventh-degree critical polynomial, verifies the one-sign-change Descartes substitution, and computes the unique root and minimum numerically after algebraic uniqueness is proved. Run `python CHECK.py` with SymPy installed.

The `NUMERIC_CHECK.py` file numerically integrates the original physical-time ODE near the Hopf curve, estimates the least period by successive local maxima, and estimates the first prey Fourier harmonic on the final orbit. Four parameter samples corroborate the analytic coefficient with relative deviations below 2.5%. Run `python NUMERIC_CHECK.py` with SciPy and NumPy installed. These finite computations do not prove either the infinite-parameter theorem or the local asymptotic expansion.

Limits: the source comparison is bounded and the 1963 foundational article is available only in abstract form. There is no claim of independent scientific validation or historical publication priority certification.
