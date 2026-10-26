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

Execute `python3 checker.py` using the Python standard library. It constructs ordinary Parikh matrices from scratch, averages all cyclic rotations with rational arithmetic, computes the covariance independently from scattered-pair counters, compares every matrix coordinate in both identities, and verifies the factorization for all six circular four-block orders. The recorded passing output is:

`CIRCULAR_PARIKH_COVARIANCE_PASS words=1548 lengths=1..15 powers=2,3,5 permutation_signs=8,8,8 blocks=486`

The exact symbolic proof in `RESULT.md` applies to arbitrary positive word length and to all positive block multiplicities. The checker is finite corroboration only, not independent proof or formal certification. An independent mathematical audit has not been performed.
