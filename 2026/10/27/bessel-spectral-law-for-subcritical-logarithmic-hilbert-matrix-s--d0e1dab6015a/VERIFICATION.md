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

# Reproducibility and limitations

The analytical certificate consists of (i) radial monomial moments, (ii) the column-summability estimate, (iii) the exact logarithmic-step kernel, (iv) dominated convergence away from the first column and uniform small-column tightness, and (v) the weighted-Volterra Bessel boundary problem. These steps prove Hilbert–Schmidt convergence and fixed-index singular-value limits without using finite extrapolation.

Run `python3 verify.py` from the directory containing that file, with Python, NumPy and SciPy installed. It checks the finite matrix normalization and the exact step-kernel identity, computes several finite singular spectra and the corresponding Bessel comparison constants. The output `CHECK_OK` certifies only those executable checks, not the theorem's infinite-dimensional assertions. The Bessel formula is known independently from Böttcher–Dörfler (2009), and the subcritical Hilbert-matrix transfer is the claim assessed here.

No independent audit, peer review, or external proof certification is asserted.
