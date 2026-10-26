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

# Verification and proof limits

Run `python check.py` in a Python environment with `mpmath` installed. The included file was executed successfully: `arc convolution checks: 23414`, `numerical spectra checks: 147`, `all checks passed`. The exact integer checks exhaust arc-indicator convolution inequalities only for group orders 5 through 50 and confirm the elementary summation identity; they do not prove it for all orders. The 147 high-precision tests sample eigenvalue order near the predicted transition and cannot prove eventual-time assertions. The analytical proof in RESULT.md establishes the universal theorem via cyclic convolution cone closure and a finite-frequency spectral gap. The spectral comparisons at the equality threshold explicitly include both tied extremal Fourier frequencies, preventing an invalid single-dominant-mode argument. No independent validation has been performed.
