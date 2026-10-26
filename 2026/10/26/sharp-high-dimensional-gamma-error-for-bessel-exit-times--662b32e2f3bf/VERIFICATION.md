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

# Verification and limits

Run `python verification.py` with the two packages and versions listed in `requirements.txt`. The program checks the exact Laplace-series cumulants, the matched-Gamma third-cumulant difference, the maximal Hermite correction, representative Bessel-zero comparison bounds, and the signed CDF approximation at the matched mean, computed independently by Laplace inversion. It prints the checked signed deviations and the limiting predicted constant.

Scientific proof relies on the analytic Bessel eigenvalue min–max bounds and integrated Fourier inversion in `RESULT.md`; no number of finite tests proves a uniform asymptotic for every real \(a\ge4\). Numerical inversion has finite precision and is corroborative only. Large-index asymptotic O-constants and literature priority have not been independently validated.
