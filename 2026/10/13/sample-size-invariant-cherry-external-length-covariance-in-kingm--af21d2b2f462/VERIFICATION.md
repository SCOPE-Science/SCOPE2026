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

# Reproduction

Run `python3 verify_cherry_external.py` using Python 3 standard library; no external dependencies.

The program checks the analytic theorem through three independent finite implementations: exact enumeration of all distinctly labelled pair-merger histories from 2 to 7 leaves (59,602 histories), exact singleton-count dynamic mixed-moment recursions through 60 leaves, and 1,767 exact level-specific cherry/singleton covariances. Arithmetic is rational throughout and comparisons are exact. The run prints three PASS lines; failure raises AssertionError.

# Verification boundaries

Finite enumeration and exact computation through 60 leaves are not proofs for arbitrarily many leaves. The all-size proof instead uses survival probabilities of marked leaves, independent exponential holding times, and an explicit finite polynomial sum. The rates are per unordered lineage pair equal to one; changing rate conventions changes the covariance scale. No external independent audit has been conducted.
