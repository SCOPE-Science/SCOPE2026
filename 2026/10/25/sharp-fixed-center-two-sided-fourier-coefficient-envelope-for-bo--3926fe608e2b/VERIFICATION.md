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

# Verification and scope

The analytic proof in RESULT.md establishes the global bound by exact Fourier duality, a paired square-root inequality, strict dual convexity, and a matching unimodular trace. It proves the endpoint asymptotics via standard complete elliptic integrals. It does not rely on finite sampling.

The self-contained `check_bound.py` numerical script requires Python 3, SciPy, and NumPy. Execute `python3 check_bound.py`. It checks 15 frequency/center configurations, five stationarity conditions and two endpoint consistency properties using independent Fourier sampling and quadrature. Its actual output was:

`VERIFY_OK extremal_Fourier_profiles=15 stationarity_cases=5 endpoint_checks=2`

Finite quadrature is not a proof of assertions for all center values, all indices or all bounded harmonic maps. The precise distinction between one-coefficient sharpness and simultaneous Bohr-majorant behavior is retained. No independent mathematical audit has been performed.
