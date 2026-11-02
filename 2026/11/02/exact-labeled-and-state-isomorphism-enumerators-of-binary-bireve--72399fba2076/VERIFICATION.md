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

# Reproducible verification

Run `python3 verify.py` with the standard Python 3 library. The program directly generates all pairs of state transition permutations and both output types at every state for one through five states; it tests inverse reversibility through the complete incoming transition maps and tests strong connectedness through directed reachability. At two states it also matches the documented GAP count of eight classes when *both* state and alphabet relabelings are allowed, contrasting with ten classes under state relabeling alone. Through four states it computes canonical representatives under all state relabelings, independently of the Burnside formula. The script also evaluates the exact labeled connected recurrence and the unlabelled Möbius inversion, checking the first ten or twelve orders, as applicable.

The captured output in `verification_output.txt` ends with `VERIFY_OK`. The numeric results in `enumeration_table.csv` follow from the exact proved formulae, not extrapolation. Brute force is finite corroboration, not an argument for all positive state sizes. The infinite results are supported by the proof in `RESULT.md`.

No external independent mathematical audit was performed.
