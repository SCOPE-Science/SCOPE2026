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

# Verification of the mathematical result

Run `python3 verify_partition_speed.py` in a directory containing the bundled checker. Successful execution produces:

```
PARTITION_FO_SPEED_FINITE_OK 945 checks
```

It exhaustively enumerates integer partitions through size 19 for selected small multiplicity patterns, verifies finite-difference identities for those patterns, checks the equality between small pp-quotient dimensions and summand multiplicities, and tests the first asymptotic coefficient numerically at partition sizes 600, 1500 and 3000. Its assertions are finite sanity checks, not an exhaustive proof of an asymptotic or an all-formula theorem.

Mathematical dependency chain: Baur–Monk normal form for sentences; Smith-normal-form computation of the eventual pp indices on cyclic modules; arbitrary-power bounds for failures of tests supported on infinitely many part sizes; Rademacher first-term differentiability and exponentially smaller tail; disjoint decomposition by the minimal set of deficient part sizes. The positive integer leading constant is an exact finite sum, so no cancellation is possible. The statement does not assume any independent external verification.
