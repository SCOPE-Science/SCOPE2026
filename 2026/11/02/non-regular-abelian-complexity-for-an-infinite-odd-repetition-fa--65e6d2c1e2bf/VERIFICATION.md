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

# Reproducibility

Run `python3 verify.py` with Python 3 (standard library only). The recorded output is in `verify_output.txt`. The script independently reconstructs finite fixed-point substitution blocks, enumerates all nine adjacent-pair languages, obtains sliding-window extremal Parikh counts, and compares them with the exact matrix recurrence. It also checks the integer parity/sign relationship and tests the weighted-factor recurrence for bounded integer weight choices.

All finite tests passed: 20 factor-language cases, 700 exact parity/sign checks and 162 weighted-factor tests. This does not establish nonregularity by computation; the general proof uses the irrationality of the cyclic substitution eigenvalue argument and the finite automaton orbit contradiction. The pair-language method is exhaustive for tested block lengths only; no finite test is claimed to exhaust the infinite theorem.
