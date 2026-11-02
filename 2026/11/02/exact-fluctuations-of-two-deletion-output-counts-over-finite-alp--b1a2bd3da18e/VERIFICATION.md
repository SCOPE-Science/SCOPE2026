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

## Reproduction

Run `python3 verify.py` from the directory containing the packaged files. It uses only the Python standard library, enumerates source words with direct two-position deletions, checks the full conditional distribution of the return count for all transition patterns, checks exact rational moments, and separately integrates over transition patterns for additional parameter choices. Successful execution prints `VERIFY_OK` followed by the exact counts.

## Proof versus experiment

The general two-deletion counting identity is proved by an append-one-symbol induction; the independent-return statement follows from forest constraints on independent nonzero increments; and the variance follows from an orthogonal expansion in centered Bernoulli variables. Finite enumeration tests special parameters only, never serving as a substitute for those infinite proofs. The reported variance concerns *distinct exact-two-deletion outputs*, not the union of all deletion radii or fixed-length Levenshtein balls.

## Limits

No formal proof assistant, external expert review, or independent audit is claimed. Reproduction is deterministic and requires no external data or network access.
