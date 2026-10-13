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

The symbolic proof reduces every play to its first ignition plus the unique second ignition that occurs after the first propagation. For a first vertex in one shore, the opposite shore is forced; the second ignition can preempt at most one original-shore vertex. The following propagation is governed by inner products with the first vertex's sign row or sign column, producing the indicator correction for one preempted opposite-sign correlation. Zero inner products are precisely the vertices left for later free ignition.

`artifacts/verify.py` implements the stated one-propagation-per-round rule independently and recursively searches all later ignition choices. It exhaustively checks all \(1168\) signings across \(K_{2,2}\), \(K_{2,3}\), \(K_{3,2}\), \(K_{2,4}\), \(K_{4,2}\), and \(K_{3,3}\), plus \(651\) deterministic structured instances on additional small profiles. The finite checks corroborate but do not prove the arbitrary-size result.

The main unverified limit is bibliographic rather than computational: the full text of the extremely recent initiating source was not available for section-by-section novelty comparison, so an equivalent observation hidden outside the abstract remains possible.
