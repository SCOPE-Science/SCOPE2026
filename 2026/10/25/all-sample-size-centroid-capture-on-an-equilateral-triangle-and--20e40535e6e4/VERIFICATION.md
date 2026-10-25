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

Run `python verify_centroid.py` with Python 3 and `mpmath` available. The independent deterministic sampling check uses a fixed random seed and computes geometric angle gaps directly. The exact finite sum is compared with high-precision numerical integration for the first fifteen sample sizes, and the known three-point formula is checked algebraically. Simulations for four sample sizes and Laplace-tail numerical ratios through \(m=500\) are reported in `verification_centroid_output.txt`.

The theoretical result is derived analytically in RESULT.md; finite numerical checks do not prove infinite quantifiers or external originality. Independent audit has not been performed.
