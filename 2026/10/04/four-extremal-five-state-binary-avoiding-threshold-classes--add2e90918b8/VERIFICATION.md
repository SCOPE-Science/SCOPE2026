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
# Verification

The claim is a finite exhaustive census. `census.c` enumerates every ordered pair of maps from five states to five states, computes synchronization and exact state-avoidance distances by breadth-first search in the 32-subset power automaton, and canonicalizes threshold-eight extremals under all state relabelings and optional letter interchange.

`CENSUS.txt` records the complete expected census output. `verify.py` recompiles and reruns `census.c` and requires exact agreement with that file. It separately recomputes the four representatives' subset distances, strong connectivity, witness-word actions, and the full symmetry orbits; it checks that each orbit has size \(240\), that the four are disjoint, and that their union has size \(960\). It also verifies that the published five-state construction belongs to the third class.

Run `python3 verify.py` in the directory containing the three artifacts. A successful run prints `VERIFY_OK`.

The computation proves only the stated finite five-state binary classification. It does not certify any asymptotic statement or any bound for larger automata.
