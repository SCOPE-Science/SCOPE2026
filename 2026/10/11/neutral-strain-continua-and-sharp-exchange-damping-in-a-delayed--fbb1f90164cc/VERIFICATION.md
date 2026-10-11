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

# Verification notes

The proof applies to all strictly positive kinetic constants, arbitrary finite nonnegative paired delays, and common saturation \(\psi\ge0\), conditional on the explicitly stated \(\mathcal R>1\). The three-stage balance yields \(K\), the host equation yields the equilibrium segment or isolated state, and the antisymmetric characteristic determinant follows by a direct exponential-mode substitution. Positivity of the real characteristic derivative and the modulus comparison for complex roots are the key infinite-dimensional steps; no finite spectral search substitutes for them. The small-\(\psi\) derivative follows from the implicit-function theorem.

For an executable consistency check without third-party libraries, run `python CHECK.py` in the same directory. It verifies numerical equilibrium residuals, a nonsymmetric composition on the neutral line, characteristic equation residuals and monotone roots for several positive saturation values, as well as the predicted small-saturation slope. Expected final printed line: `CHECK_OK`. Finite numerical checks are not an exhaustive search of characteristic roots; the analytic modulus inequality performs that role.

No claim is made about the global nonlinear relaxation rate, full seven-state spectral gap, or arbitrary nonidentical-strain parameters.
