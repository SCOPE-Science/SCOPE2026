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

# Verification details

The included Python script `verify_cubic_dyadic.py` was executed successfully, exhaustively constructing full residue functional graphs for each integer level from 5 through 16. It checks the even permutation, all cycle lengths stratified by valuation, exact odd-image classes and eight-predecessor multiplicities, and the complete indegree distribution. The execution ended with `VERIFY_OK exhaustive_levels=5..16 all_cycles_odd_fibers_and_indegrees`. The infinite scope of the theorem follows from the even-iterate valuation induction and odd-fiber congruence argument, not the finite tests.

Historical priority is conditional upon literature actually inspected. No independent mathematical audit has been performed.
