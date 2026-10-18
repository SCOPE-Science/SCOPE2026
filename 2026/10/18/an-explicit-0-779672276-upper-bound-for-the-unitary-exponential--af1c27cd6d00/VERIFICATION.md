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

Run `python3 verify_upper_density.py` from this directory. No downloads, additional files, or nonstandard packages are needed. A successful run prints `VERIFY_OK` and the claimed exact cutoff checks.

The script verifies all \(670\) finite-prime scores by integer inequalities, computes the weighted probability of negative-enough cylinders, recomputes the conservative prime-tail moment bounds through \(100000\), and checks the strict rational inequalities needed for the stated upper density. The auxiliary small-number regression checks implication examples through \(30000\) but is not a substitute for the prime-tail argument in RESULT.md. No independent audit has yet been performed.
