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

Install `requirements.txt` in an isolated Python environment and execute `python verify.py` in the same directory. The recorded program output ended with `PASS: 35 quadrature, spectral, derivative, sign, and asymptotic checks` and displayed the critical asymptote ratios at time lags 30, 60, 120, 250. The nested positive spectral-density integral agreed with the independently age-integrated covariance at lag 2 to high precision.

The numerical program calculates the deterministic Ott–Antonsen flow independently of the stationary density and reconstructs the two-time covariance from the Poisson age integral. It does not depend on previously recorded files. Critical claims with continuum quantifiers and limiting asymptotics are proven analytically in `RESULT.md`; numerical checks do not establish them by themselves.

The proof requires exactly Lorentzian intrinsic-frequency statistics, an aligned Ott–Antonsen state globally restored at each reset, and a homogeneous Poisson clock. It does not verify physical finite-population errors, unpublished priority or any independent audit.
