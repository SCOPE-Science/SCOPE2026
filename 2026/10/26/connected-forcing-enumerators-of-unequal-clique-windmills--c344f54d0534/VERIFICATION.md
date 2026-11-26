---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The two cases give a disjoint classification of all nonempty connected starts. With a black hub, an occupied blade with more than k white vertices cannot receive a first additional black vertex: the only adjacent candidates are the hub and blade-mates, each of whom sees more than k whites. The total size of the initially empty blades is likewise a permanent obstruction if it exceeds k, because only the hub could seed any of them. Conversely each eligible occupied blade can be finished first, after which the hub can finish all empty blades. Thus the allowed seed counts and the bound on the weighted empty-blade set are both necessary and sufficient. With a white hub, connectivity confines the seeds to one blade h. A first force has m_h−s+1 white neighbors, and when legal it colors the hub and every remaining vertex of h. The other blades can be completed iff M−m_h≤k. Counting labeled subsets gives exactly the two terms, including a zero contribution if a blade is too large to be omitted or too small to host a suitable hub-free start. Monotonicity justifies using an ordered sufficient sequence instead of parallel closure. In the uniform case the minimum comes from the largest allowed number of omissions until the peripheral singleton threshold. At its predecessor k=(r−1)m−1 the size is three, also for r=2 where k=m−1. The hub becomes a singleton at k=rm; for k≥M every connected start succeeds, as also follows from the general expression. The supplied verify.py was inspected but not executed; it is a bounded replay comparing exact closure, the structural predicate and polynomial coefficients. The case proof establishes the result outside that domain.

## originality

PASS

Credit is limited to the arbitrary heterogeneous all-k connected enumerator. There is demonstrable prior coverage of the heterogeneous k=1 specialization, and the uniform all-k connected result is already a filtering consequence of an earlier all-starts classification. The earlier friendship scalar values are also covered; none of these specializations is credited as independent novelty.

## value

PASS

The distinct contribution is a complete labeled connected-forcing enumerator on a natural nonuniform block graph family, explaining the competition between local seed thresholds and one global weighted empty-blade budget. It determines all coefficients and minimum-set multiplicities for a heterogeneous profile, with a different mechanism when the hub starts white. The uniform and friendship applications illustrate the boundary but are not counted as an additional new contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
