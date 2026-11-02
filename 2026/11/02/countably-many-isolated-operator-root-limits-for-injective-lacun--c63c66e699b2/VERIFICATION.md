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

`python3 checker.py` was executed on the exact included script in the preparation environment and printed `FINITE_ASSERTIONS_PASSED 18600`. The script uses Python standard-library `fractions.Fraction` to compare exact spike-window sums and their finite-size corrections across bases, scales and coordinate offsets.

It does **not** prove that the listed subsequences exhaust all limits or establish weak/strong topology conclusions; those are analytic proof steps in `RESULT.md`. Independent mathematical verification has not been performed.
