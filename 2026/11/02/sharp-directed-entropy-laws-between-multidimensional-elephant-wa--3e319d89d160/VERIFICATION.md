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

# Reproducibility and scope

`python3 verify.py` replays the packaged deterministic tests. The accompanying `verification_output.txt` records the successful run with 8,482 assertions. Calculations include exact rational count-state probability normalization, exact expected squared-frequency recurrences, direct probability-of-every-history KL versus the conditional KL chain rule, exact critical harmonic identities, and numerical small-imbalance Taylor checks.

The unbounded-time assertions are **not** justified by finite tests; they follow analytically from the exact conditional distribution, second-moment recurrence, uniformly positive likelihood Taylor expansion, normalized-martingale tail bound, and power/harmonic summation given in `RESULT.md`. Finite testing does not establish historical novelty, independent review, all numerical edge cases, or any results outside fixed interior parameters in dimension at least two.
