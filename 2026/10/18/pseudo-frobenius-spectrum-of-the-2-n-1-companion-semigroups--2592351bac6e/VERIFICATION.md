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

# Verification and limitations

Run `python verify_fermat_companion.py` with Python 3. The checker performs shortest-path Apéry reconstruction independently of the greedy expression for n=3..11 (4,097 Apéry entries), and tests the coin-cutoff local-maxima and tail-count formulas for h=1..12 (16,368 positions). Both passed when executed with the embedded file contents. For arbitrary n the proof in RESULT.md is the evidence. The general greedy/Apéry lemmas are cited from arXiv:2306.10738v1 and hypotheses checked explicitly. No independent mathematical audit has been carried out.
