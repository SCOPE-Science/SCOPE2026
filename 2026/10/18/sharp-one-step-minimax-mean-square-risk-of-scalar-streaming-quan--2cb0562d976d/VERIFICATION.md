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

# Reproduction and limits

Run `python3 CHECK.py` with Python 3 and its standard library; no external assets are required. The execution checked 72 full finite configurations of batch length, quantile, corruption probability, and magnitude bound; for each, it enumerated the conditional maxima of the clean and corrupted update cases and compared the exact expectation with the proposed binomial expression. Additional checks compared finite values with the quarter-corruption threshold, the scaled rare-tail factor, and numerical two-term batch-size centers at increasing corruption bounds. All checks passed in the packaged program's local execution.

These finite checks do **not** establish the universal minimax property beyond the enumerated sizes or the large-amplitude limit. The accompanying written proof addresses both through exact order-statistic cases, the binomial law, Stirling's formula, and geometric bounds on the upper-tail ratios. No independent audit or validation has been performed.
