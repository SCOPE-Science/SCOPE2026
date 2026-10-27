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

# Reproducibility and limits

Run `python verify.py` with Python 3, NumPy, SciPy, and SymPy installed. The included self-contained checker performs exact symbolic simplification of both stationarity rays, both resulting real squared-wavenumber formulas, the density-balanced factorization, and the derivative of the ratio map. It then compares full quartic eigenvalues and independent scalar numerical maximization over a seeded collection of 558 positive parameter triples (7,254 numerical assertions). Actual observed result: `PASS: 6 symbolic identities, 7254 numerical assertions, 558 positive parameter triples`.

Numerics exercise broad but finite parameter ranges and do not certify all real parameters. Analytic completeness instead comes from the root-counting interval, the two exhaustive stationary-ray cases, strict monotonicity of the density-ratio map, and the factorization certifying the sharp inequality. No kinetic-temperature, collisional, multidimensional or nonlinear claim is checked here.
