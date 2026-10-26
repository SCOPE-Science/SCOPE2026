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

The exact-rational `verify.py` enumerates the truncated binary-carry Markov automaton at fixed shifts. It checks the analytical central-binomial value for weights 1 through 6 at three admissible gaps each; the weights 1 and 2 are comparison cases, and the structural new theorem applies to weights at least 3. It also checks that the adjacent smaller gap changes the density in the selected tests for weights 2 through 6.

Command: `python verify.py`. The observed last line was `VERIFY_OK isolated_carries=PASS weights=1..6, three_distances_each`. Independent audit has not been performed. Finite tests do not prove the all-parameter claim; its proof is in `RESULT.md`.
