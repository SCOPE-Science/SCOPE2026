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

Run `python3 one_marker_separation_checker.py` using Python 3. The independent finite verification reports `CHECK_OK full_transition_tests 274 all_zero_transition_tests 9231 sharp_threshold_lengths 199`.

The first test independently enumerates both letter maps, the second enumerates every zero-letter map and eliminates the one-letter map by considering possible images at the two marker positions, and the third checks the lcm-based sharp worst-case thresholds. Their finite scope does not certify unbounded lengths: the proof of all-length equality uses the dichotomy for the transient length of the zero-transition orbit.

The literature comparison is a scholarly search, not proof of historical priority. No independent scientific audit has been performed.
