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

The polynomial calculation is exact for every integer degree, not inferred from a numerical extrapolation. The one-alias DFT formula and its inverse are exhibited in `RESULT.md`, as is the dilation-invariant rational quotient argument for full two-circle rigidity.

Run `python3 check.py` with Python 3 standard library; no third-party packages or network access are needed. Its fixed-seed sampling experiments verify the exact angular Fourier formulas, both real projections, coefficient inversion, circular-intensity reconstruction and the aligned-grid counterexamples for degrees 1 through 9. The observed result was **PASS, 9639 finite numerical assertions**.

Finite floating-point assertions do not establish a theorem for arbitrary coefficients, degrees or radii. The proof establishes injectivity and the Nyquist two-by-two singular-value formula; it does not establish a Lipschitz inverse for the full nonlinear coefficient-recovery map. No independent audit or validation has been performed.
