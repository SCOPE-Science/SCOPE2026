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

# Reproduction and limits

Run `python check.py` from this directory with Python 3.9 or later; no third-party packages are required. The program enumerates all binary cut strings for deck sizes \(1\) through \(12\) at probabilities \(1/4,1/2,3/4,9/10\), computes inversion parity directly for the resulting permutation, and compares the exact rational expectation to the proposed recurrence. It printed `PASS: 48 exhaustive rational cut-pattern checks, sign/parity and phase-boundary consistency checks` when executed against the packaged file.

The enumerations support only those explicitly finite cases. The proof of the generating function, positivity phase, oscillatory phase, and all-time parity law is analytical and is given in `RESULT.md`. No independent external audit has been performed. The possible presence of a more general earlier sign-character calculation remains a scientific-priority limitation.
