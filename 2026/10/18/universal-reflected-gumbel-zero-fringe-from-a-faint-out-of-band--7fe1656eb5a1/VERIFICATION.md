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

The reproducible supplemental script `verify.py` evaluates exact Gaussian tilted moments for two compactly supported PSD shapes, both signs of an out-of-band pure tone, and a decreasing sequence of amplitudes. Its checks compare the analytic intensity with numerical differentiation of the zero-potential and the flux, and track convergence to the universal reflected-Gumbel profile. It reports `VERIFY_OK 68 quadrature flux, noncentral Gaussian potential and Gumbel profile checks` under NumPy and SciPy.

The numerical script is not a certificate of the global theorem: exponential tilting at unbounded frequencies, Birkhoff's ergodic law, and local uniform convergence are established in the analytic proof. Independent validation has not been performed.
