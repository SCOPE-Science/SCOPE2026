---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Writing source and sink as vertex indicators, only identical or adjacent vertices contribute mixed covariance; yields sum_edges(q p^(d_u+d_v-1)+p q^(d_u+d_v-1))-sum_vertices(pq)^d. An explicit arm transplantation decreases branching excess and strictly improves the vertex term; remaining edge correction B_d is nonnegative by its signed difference. Iterate to unique path. The formula for P_n and n=2,3 boundary cases were checked directly. Independent exact orientation enumeration for every unlabeled tree n<=7 and p=1/3,1/2,2/5 matches both covariance and strict extremum. No lower extremizer is claimed.

## originality

PASS

Best-of-knowledge original on the stated restricted theorem after comparison of exact implications; no exhaustive priority claim and specified inspection limits remain.

## value

PASS

A parameter-uniform strict extremal theorem identifies a natural transition: four vertices have positive maximum away from p=1/2, whereas the unbiased four-vertex maximum is zero. An arbitrary-tree covariance identity plus an explicit monotone branch-reduction argument is stronger than isolated small-graph observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
