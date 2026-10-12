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
# Verification record

The theorem is proved by preserving the truth values of every subformula at every retained world. The critical implication case has two directions: root falsity has a material counterexample among the selected witness worlds, while root truth excludes material counterexamples globally; at a nonroot world a false implication is witnessed by the root-selected counterexample and a true implication receives an empty row. Induction on formula structure completes the unrestricted argument. Closed axiom validity transfers because a closed formula has no atomic truth choices. NP membership uses a bound of one plus the number of distinct implication subformulas, and hardness reduces 3-SAT by requiring exactly one positive/negative literal atom of each pair to hold at the universally reflexive root.

The provided `verify_fmt.py` program runs with unmodified Python 3 using only the standard library. Its finite test output was:

```
CHECK_OK compression_cases=1150 max_random_retained_worlds=4 distinct_witness_worlds=4 dualrail_instances=360
```

The code checks the actual recursive semantics and compressed truth tables rather than simply comparing pre-recorded counts. Its random cases and finite dual-rail tests do not prove statements about arbitrary-size or infinite models; the proof supplies those quantifiers. No independent audit or external theorem certification is claimed. The 1992 original pure-necessitation full text and a full paper underlying Tominaga's 2026 abstract were unavailable for complete-text comparison; this leaves residual historical-priority uncertainty, not a gap in the stated induction.
