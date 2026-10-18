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
# Verification record

The reproducible exact-rational checker is `check.py`; its captured stdout is `check_output.txt`. It builds the deletion shadow directly by taking all pairs of deleted positions, compares its cardinality with the independent closed per-word canonical formula, and averages cardinalities and squared cardinalities using rational arithmetic. It evaluates all words for \(q=2,3,4,5\) over the length ranges stated in `RESULT.md`, totaling 79,073 complete source words. Its final line is `PASS total source words 79073`. The binary computations are controls, not novelty claims. No random sampling is used.

The mathematical proof reconstructs the greedy canonical embedding, the nonbinary return-triple correction, independence of uniform increments, the signed nearest-neighbor covariance cancellation, and all variance terms. The exact finite checks do not establish the infinite theorem independently. No independent audit has been performed. No claims are made about the full distribution or nonuniform source statistics.
