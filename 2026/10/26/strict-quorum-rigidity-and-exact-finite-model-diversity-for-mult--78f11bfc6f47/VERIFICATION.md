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

Execute `python checker.py` under Python 3.9 or later. There are no third-party package dependencies. The program enumerates the named order-tuples independently of the structural normal form, directly evaluates the original per-edge quorum condition, groups qualifying tuples by number of distinct orders, and compares those integer counts with the proposed coefficient formula. It checks eight finite parameter triples, including the entire \(n=5,r=3,q=2\) search space and \(n=4,r=4,q=3\), and tests boundary counterexamples for several parameters.

Expected terminal line: `ALL_CHECKS_OK`. The proof's unbounded quantifiers over arbitrary \(n,r,q\) are discharged by the path/cycle and occupancy arguments in `RESULT.md`; passing the finite checker cannot independently certify those assertions. No external independent audit has been performed.
