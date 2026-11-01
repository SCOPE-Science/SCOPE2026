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

# Verification and reproducibility

Run `python check.py` using a standard Python interpreter; no extra packages are required. It compares independent two-dimensional surface quadrature of \(H^2dA\) with the one-dimensional tubular curvature integral, checks the explicit fixed-constraint ring energy, global curvature gap and Fourier second-order coefficients for several regular support perturbations, and evaluates the Clifford ratio benchmark. Its checks print three `PASSED` messages. The continuum inequality, uniqueness and spectral sharpness are established in the analytic proof, not by finite quadrature.

Admissible curves are embedded, have reach strictly larger than the tube radius, and have turning number one. The prescribed-area-and-volume profile is a restricted tube-family minimum, not a general global Willmore bound for all tori. Comparison with historical literature remains provisional. Independent mathematical audit: not performed.
