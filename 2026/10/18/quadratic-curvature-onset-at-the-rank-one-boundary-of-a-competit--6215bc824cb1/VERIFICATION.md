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

# Reproducibility checks and limits

Run `python verify.py` in an environment with SymPy and mpmath installed. The script must print `VERIFY_OK`. It uses exact symbolic rational-function simplification to check the Jacobian determinant, equilibrium and eigenvalues, the first two parameter coefficients of the stable-graph invariance identity, and the coefficient of the second derivative. Exact rational trials test the one-step image and two basin-sign conditions at several sample parameters and initial states. Separately, 55-digit finite-precision basin shooting tests the cubic-order approximation at \(A=1\), \(b=3\), \(d=2\), detunings \(\varepsilon=\pm0.03\), and initial ordinates \(y=0.5,4\). These finite tests are not exhaustive and do not certify all real parameters or the infinite-time basin itself.

The analytical proof of smooth parameter dependence rests on the hyperbolic local stable-manifold theorem and the implicit-function theorem, neither of which is established by finite software execution. The script verifies the displayed algebra, not the theorem's global-topology inputs or historical originality. No independent audit or independent validation has been performed.
