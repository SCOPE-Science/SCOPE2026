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

# Reproducibility and limits

Run `python3 verify.py` with Python 3 and its standard library. It independently computes the possible interleavings of two identical one-marker roots using dynamic programming, compares every two-marker word for half-length 1 through 12 with the exact root-interval criterion (1,222 instances), and checks the tail histogram, the maximum, the three-gap deletion map, and the root-incidence identity by finite enumeration for half-length 1 through 100 (671,650 instances). The program completed with `VERIFY_OK`.

These computations are finite crosschecks. The proof for every integer half-length and root threshold is the interval and bijective argument in `RESULT.md`; no inference of infinite correctness from a finite run is made. No independent scientific audit has been performed.
