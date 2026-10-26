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

# Verification of the mathematical result

The essential calculation is reproduced entirely by the Rayleigh quotient, a weighted Cauchy–Schwarz inequality, and the positive Perron eigenvector of the alternating-conjugated path matrix. These analytic ingredients are explicitly proved and specialized in `RESULT.md`.

Reproduction: with NumPy and SciPy installed, run `python check_layers.py`. The script runs a deterministic suite at all integers \(2\le N\le17\) with seed `7302026`, verifies sharp modal speeds and eigenvector residuals, tests the strict inequality for unrelated random allocations, and verifies the two- and three-layer specializations. It reports 13,200 successful numerical assertions (3,200 each of four broad classes and 200 each of two special classes).

The script is finite numerical corroboration, **not** a proof for arbitrary layers and parameters. Strictly positive finite thicknesses are essential. The statement is restricted to the specified linear hydrostatic Boussinesq rigid-lid model. A complete historical priority check of some paywalled original texts could not be achieved; this does not affect the self-contained analytic algebra but leaves a publication-priority risk. No independent audit or external scientific validation is asserted.
