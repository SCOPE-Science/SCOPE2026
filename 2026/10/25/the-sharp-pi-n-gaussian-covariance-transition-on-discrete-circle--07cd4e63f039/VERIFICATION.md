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
# Reproducibility
The included `verify.py` uses mpmath and does not need datasets. Run `python verify.py` with mpmath installed. It checks: (i) direct finite cyclic Fourier eigenvalues against a Poisson sum minus omitted Gaussian images; (ii) negative high-frequency witnesses for each congruence class modulo four at a fixed subcritical \(c\); (iii) positivity of every eigenvalue for selected finite sizes at a fixed supercritical \(c\); (iv) high-precision roots of the Nyquist eigenvalue on multiples of four and the approaching correction constant. Computations are finite and do not establish the uniform asymptotic theorem on their own.

Analytic limits are in RESULT.md. No machine/formal proof certificate, independent audit, or comprehensive literature certification is supplied.
