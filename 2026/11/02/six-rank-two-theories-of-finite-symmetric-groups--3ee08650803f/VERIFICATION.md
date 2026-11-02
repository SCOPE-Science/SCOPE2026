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

The files `check_atomic_reduction.py`, `check_exact.py`, and `check_cycle_types.py` have been executed with their recorded outputs in `atomic.log`, `exact.log`, and `cycle.log` respectively. Reproduce with a standard Python 3.9+ interpreter in this directory; no external package is required.

`check_atomic_reduction.py` directly enumerates all 36 equality and multiplication atoms over the identity and two selected permutations in degrees one through six. It checks that the eight primitive tests retain all atomic information. `check_exact.py` considers every conjugacy-class representative as the first selection and every group element as the second selection through degree nine, confirming the profile sets and the six-class partition on the examined degrees. `check_cycle_types.py` independently enumerates integer partitions through degree fifty and applies the cycle-square criterion, confirming the seven-to-eight-type transition in every degree examined.

The unbounded equivalence claim relies on the symbolic proof of complete extension profiles and the elementary cycle interlacing theorem, not on extrapolation. These are reproducible computational cross-checks, not external proof certification.
