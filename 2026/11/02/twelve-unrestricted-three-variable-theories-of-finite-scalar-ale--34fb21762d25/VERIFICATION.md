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

# Reproducible checks

Requires Python 3 standard library only. From the directory containing the scripts, run `python check_patterns.py` and `python check_logic.py`. The first script enumerates all 1,666 ordered-pair extension profiles across eighteen finite scalar Alexander examples, verifies positive masks have multiplicity one and that precisely twelve distinct claimed signatures appear in the principal representative set. The second script constructs the entire labeled three-tuple atomic profile directly and refines logical quantifier types through rank four across sixteen examples, checking the expected equalities and twelve realized three-variable classes. Its independent width-four separator computation also succeeds.

Expected exact outputs are `patterns_output.txt` and `logic_output.txt`; they are re-created by running the two programs. The given finite tests do not prove all field orders, higher dimensions, or unrestricted logical depth. The published proof covers those cases by the anharmonic orbit calculation and three-pebble back-and-forth argument. Neither these tests nor their reproduction constitutes independent mathematical auditing.
