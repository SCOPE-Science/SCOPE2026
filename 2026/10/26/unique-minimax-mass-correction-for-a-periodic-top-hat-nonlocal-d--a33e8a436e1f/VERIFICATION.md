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

The proof's necessary ingredients are the normalized Fourier-symbol calculation, the global threshold formula, strict ordering of maximizing and minimizing frequencies, and exact rational bounds for two specified weights.

Run `python check.py` next to the provided result. This checks rational Taylor truncations, polynomial comparisons, 310000 sampled positive frequencies, three periodic frequency grids, and numerical scalar optimization. These tests passed during preparation. The proof, not the samples, handles all real frequencies, all positive weights, periods, and horizons. The numerical optimizer is diagnostic, not a certified unique location of the maximizing frequency. The unique coefficient is proved analytically.

Independent validation of the science and independent bibliographic audit have not been performed. Full text of an earlier related two-level Toeplitz preconditioning study was not available for direct statement comparison.
