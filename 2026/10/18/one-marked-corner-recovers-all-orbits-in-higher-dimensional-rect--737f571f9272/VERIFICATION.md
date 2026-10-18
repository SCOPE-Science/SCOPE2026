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

# Reproducible verification and limits

The four scripts in this package are self-contained checks of explicit finite parameter families. Execute each from the directory containing the scripts. All require Python 3. The exact automorphism checker additionally requires `networkx` version 3.6 or compatible.

* `python3 verify_direct.py`: vertex-level graph construction and stable refinement; 239 factor tuples, 124,767 vertices, max 20 strict splitting rounds. Output: `direct_output.txt`.
* `python3 verify_quotient.py`: a separately implemented weighted quotient automaton with 188 factor tuples, 24,015 orbit-profile states, max 21 strict splitting rounds. Output: `quotient_output.txt`.
* `python3 verify_orbits.py`: exact independent automorphism orbit enumeration on seven small grids. Output: `orbits_output.txt`.
* `python3 verify_reconstruction.py`: checks predecessor-deck recurrence, opposite-end recurrence, and pair reconstruction identities on 106 factor tuples and 31,285 vertices. Output: `reconstruction_output.txt`.

All four executables passed from their saved source files. Individual computation is exact integer and combinatorial testing. The general result rests on the proof in `RESULT.md`; tested finite ranges cannot establish the full theorem. The source comparison is a self-review only, with no independent originality or correctness audit.
