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

Run `python verify.py` using Python 3.10 or newer; no external packages or network access are necessary. The program evaluates EF1 scores directly from valuations and allocations with exact `Fraction` arithmetic, rather than implementing the theorem as a test oracle.

It checks the equalizing algorithm on 280 fixed inputs and exhaustively optimizes all choices of earlier recipients and later recipients for 90 weighted finite games (two through four agents, two exact scale values, three factor thresholds, five weighting profiles). These checks cover both sides of the claimed threshold and include nonuniform prior probabilities.

Expected output: `VERIFY_OK equalizer_input_checks= 280 exhaustive_weighted_policy_games= 90 max_agents_bruteforce=4 exact_rational=True`.

## Limits

The source code checks bounded finite instances only. The general theorem depends on the counting, explicit best-response, and equality-condition arguments in `RESULT.md`, not on extrapolation from experiments. No independent mathematical audit has been performed.
