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

# Verification

The reproducibility file `verify.py` uses only Python's standard library. Run `python3 verify.py` and expect the terminal line:

`VERIFY_OK brute_n=2..8 exact_OEIS_n=1..24 asymptotic_diagnostics_n=100..100000`

Its finite exact checks compare two independently implemented count constructions and the first \(24\) published sequence values; numerical diagnostic ratios are printed for several larger lengths. These tests do not prove an infinite local limit or rule out prior results. The mathematical proof verifies the exact generating product, pointwise normal characteristic-function convergence, a whole-frequency Gaussian integrable majorant, uniform Fourier inversion, and the maximum/localization consequences. All calculations and source comparisons have been reviewed within the present scientific package; independent audit remains unperformed.
