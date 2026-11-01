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

# Reproducibility checks

Run `python CHECK.py` using Python 3 and standard-library modules only. A replay of the included checker completed with \(84\) exact rational inner-product identities, \(21\) spectral-agreement or sampled-extremum tests, and \(8\) dense-scale asymptotic comparisons. Representative logarithmic spacings \(L=0.30,0.20,0.15,0.10\) yielded successive relative lower-constant errors of approximately \(0.00938,0.00417,0.00234,0.00104\), and successive upper-constant errors of approximately \(0.00560,0.00250,0.00140,0.000625\).

These checks provide an independent finite consistency test for the exact four-term overlap factorization, Mellin-periodization normalization, and limiting coefficients. They do **not** certify the continuum minimum or infinite Riesz property by sampling. Those are established analytically in RESULT.md through the positive alias formula, Fourier-series quadratic forms, and the two-range uniform minimum argument. No external validation, independent audit, or machine-checked theorem certification has been performed.
