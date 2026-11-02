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

Run `python3 checker.py` from this folder. It enumerates cyclic rotations of literal factors from the period-doubling fixed point and independently compares classes at lengths \(n\) and \(2n\) for every integer \(1\le n\le100\). It also checks that applying the substitution to the shorter observed classes gives exactly the longer observed classes. Finite samples of 4,000 and 8,000 start positions are compared to guard against premature factor-window truncation.

The program prints `VERIFY_OK` on completion. Direct execution passed. No external package is required.

The finite tests do not establish equality for all \(n\). That infinite conclusion follows from the proof's full factor-phase classification and parity argument, which require no extrapolation. No independent audit was performed.
