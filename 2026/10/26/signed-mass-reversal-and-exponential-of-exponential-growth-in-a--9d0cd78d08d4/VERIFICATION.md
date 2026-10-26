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

# Verification instructions

Using Python 3.10+ with SymPy and mpmath installed, run `python verify.py` in the folder containing the complete files. The file uses the original two-stage equations, reconstructs the logarithmic-rate predictor and first corrected endpoint, checks their symbolic reduction to the closed forms, derives the mass Taylor coefficient symbolically, and exercises finite positive inputs and large-step logarithmic diagnostics without evaluating overflow-prone outer exponentials.

Execution performed for this package: `PASS: 324 symbolic and finite verification assertions`.

The checks cover several fixed ratios, rates and step sizes. Exact symbolic assertions establish polynomial/identity reductions under their stated symbolic domains, but finite numerical checks do not certify universal statements. All universal signs, limits and quantified conclusions require the independent analytical derivation in RESULT.md. No independent audit or external validation has been performed.
