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

Run `python verify_qsd.py` (SymPy and NumPy). The exact symbolic checker validates all three resultants, the Perron-root range exclusions, the five-way rational boundary and the cofactor crossing derivatives, and Sturm variation counts at three rational endpoints. It separately enumerates the full seven-state continuous-time generator and checks the modal regimes for sample parameters. The proof in RESULT.md, rather than finite numerical tests, establishes the universal classification. There is no external independent validation.
