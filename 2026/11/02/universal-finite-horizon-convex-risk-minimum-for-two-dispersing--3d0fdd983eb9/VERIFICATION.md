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

Run `python3 check.py` in the directory containing the extracted package. Its expected output is `EXACT_CHECKS_PASSED 6022`. It uses only the Python standard library and exact fractions, reconstructs state paths directly from the two-patch update, and checks the two-year variance identity and finite examples, including positive spatial correlation, anticorrelation and perfectly shared shocks. Checks are finite and cannot establish the universal claims on their own; the proof in `RESULT.md` establishes the general result.

The result requires positive exchangeable growth, independent environmental years, a fixed constant migrant-survival fraction, and mean-normalization by each strategy's own expected total. The independent audit has not been performed.
