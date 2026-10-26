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

The standalone `verify.py` uses the Python standard library. Run `python3 verify.py` in the same directory as this document. It independently enumerates every partial injection for each degree from one through eight, filters for preservation of every pairwise distance, discards cyclic maps, computes the nilpotency index directly by iteration, and compares each rank/index coefficient with the transfer recurrence. The totals are \(1,3,9,27,65,151,317,663\). It additionally evaluates the closed rank formula and parity-dependent total through degree 100. Successful completion prints `VERIFY_OK_CHAIN_PARTIAL_ISOMETRY_RANK_INDEX`. Exact finite checks do not prove a formula for all degrees; the separate proof in `RESULT.md` establishes the universal claim. No independent mathematical audit was performed.
