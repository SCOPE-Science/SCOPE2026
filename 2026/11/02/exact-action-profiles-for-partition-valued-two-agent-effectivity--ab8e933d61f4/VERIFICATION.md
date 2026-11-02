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

Run `python checker.py` with Python 3 and no third-party dependencies. The program independently constructs cyclic deterministic outcome tables for all 21,297 finite positive cross-intersection matrices with 1–3 row blocks, 1–3 column blocks, and intersection sizes 1–3, checking each action type's exact output set. It exhaustively counts row-and-column-surjective arrays for six small parameter triples and separately computes their counts using the stated omission-event inclusion-exclusion formula. Results include 2 such arrays on a 2-by-2 grid using 2 symbols, 102 on a 3-by-3 grid using 2 symbols, 12 on a 3-by-3 grid using 3 symbols, and 24 optimal labelled outcome functions for the heterogeneous cross-intersection matrix with entries 2,1,1,3. The output is `ALL_CHECKS_OK`.

These finite tests are not a general proof. The mathematical proof separately derives the necessary multiplicity inequalities and gives a modular construction satisfying all of them for every finite cross-intersection matrix. A cross-intersection matrix of positive integers can always be instantiated as two transverse partitions by using disjoint labelled cell sets of those sizes. No computational dependencies or external certificates are needed.

All historical-priority conclusions are limited to the inspected literature; no independent scientific audit has been performed.
