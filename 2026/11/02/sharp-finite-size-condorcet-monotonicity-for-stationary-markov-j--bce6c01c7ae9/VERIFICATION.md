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

# Verification notes

The complete analytical proof is in `RESULT.md`. The independent script `check_markov_jury.py` can be replayed from this directory with `python3 check_markov_jury.py`; no dependencies beyond the Python standard library are required. It passed 1043 exact-rational assertions across eight parameter pairs, using both state-count dynamic programming and all-word enumeration, and checked pathwise complement ratios.

The script checks only finitely many sample sizes and rational parameters. The all-size and all-real-parameter theorem follows instead from stationarity, exhaustive pivotal-event classification, the exact complement bijection, and the finite-state Markov ergodic theorem. No separate external proof verification or historical-priority certification has been performed.
