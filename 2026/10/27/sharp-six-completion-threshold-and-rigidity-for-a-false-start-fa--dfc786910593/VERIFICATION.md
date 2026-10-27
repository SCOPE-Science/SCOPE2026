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

## Reproduction
Run `python3 repro/exhaustive_threshold.py` to exhaust every nonexceptional signed word through length \(17\) up to complementation, performing integer coefficient arithmetic through degree six. Its required assertions check no admissible six-completion below length \(17\), one normalized minimizer at length \(17\), and its explicit identity. Run `python3 repro/direct_witness.py` for the independent full-word implementation of the winning completion chain.

The exhaustive procedure checks a finite set completely, not an infinite family of parameters. The first script implements exact arithmetic and a binary-doubling geometric-series update; the second directly evaluates binomial sums over physically appended words, confirming final length \(960\) and failure at stage seven. Both programs are supplied as reproducibility evidence. Independent external audit has not been performed.
