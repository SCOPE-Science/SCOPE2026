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

Run `python verify_qr_tail.py` in a Python environment containing the versions of NumPy and SciPy described in `requirements.txt`.

The verification script performs 300 reproducible full-rank singular-limit perturbation tests and 255 smallest-singular-value expansion tests at seeded random matrices, and checks two closed exact central-Gaussian two-column tail formulas. It numerically integrates the independent noncentral chi-square ratio distribution for positive signal-to-noise at four settings. All executed checks passed, with maximal relative discrepancy \(6.760	imes10^{-10}\) in the 300 singular-limit tests and tail-rescaled quadrature ratios from \(1.000078\) to \(1.002493\). These finite checks do not prove the theorem; the proof is in `RESULT.md`.

The critical mathematical steps are: conditional Gaussian decomposition, uniform chi-square inverse moments up to the codimension; the Gram-kernel perturbation for the **actual** smallest singular value; integrable domination through the previous-column condition moment; and an exact Gaussian density-at-zero times ball-volume calculation. No external independent audit or certification has been performed.
