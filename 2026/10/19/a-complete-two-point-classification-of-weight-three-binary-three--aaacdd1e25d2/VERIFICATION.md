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
# Reproduction and limitations

The file `check_decks.py` uses only Python's standard library and requires Python 3.8 or later. Execute `python3 check_decks.py` from the directory containing this file.

It constructs every binary word with exactly three ones and at most 25 zeros by enumerating unique zero-gap quadruples. For each, a dynamic-programming procedure calculates the full eight-coordinate three-deck. A separate combinations-of-position index construction rechecks smaller cases. It enumerates actual fibers, verifies the one- or two-word class structure, independently predicts partners from the gap criterion, and matches the exact generating-function coefficient through the parameter-count formula. Five hundred additional reproducible larger examples test the partner condition at increased lengths.

Expected output: `WEIGHT3_3DECK_ALL_CHECKS_PASSED totals=0..25 profiles=23751 random=500`.

This finite test does not prove the infinite theorem. All-length correctness rests on the symbolic gap/coordinate argument and complete class bijection in `RESULT.md`. The evidence does not claim an external audit or formal mechanical proof.
