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

# Reproducibility

Run `python3 verify.py` in a directory containing this file and the standalone verifier. It uses only the Python standard library. The recorded execution passed 38,779 exact rational sign checks for all admissible distinct pairs through size 80 and 13 exhaustive derangement mixed-moment comparisons for sizes five through eight. Numerical checks complement, rather than prove, the infinite theorem. Full sign and asymptotic proofs are in RESULT.md. No independent audit has been performed.
