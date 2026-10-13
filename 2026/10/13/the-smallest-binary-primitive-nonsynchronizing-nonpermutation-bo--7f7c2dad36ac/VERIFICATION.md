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

Run `python3 verify.py` beside `verify.cpp` and `certificate.json`.

The program enumerates every ordered pair of total letter maps for state counts \(2,3,4,5\). It removes the all-permutation case, enumerates every nontrivial state partition to decide primitivity, and searches the subset automaton from the full state set to decide synchronization exactly.

For every accepted five-state automaton, a separate generated-congruence procedure checks primitivity again, and an independent pair-compressibility search checks nonsynchronizability again. The verifier then recomputes all canonical representatives under simultaneous state relabeling and letter exchange, all orbit sizes, and the rank-type split.

The finite computation proves no statement for more than five states or for larger alphabets. Independent audit has not been performed.
