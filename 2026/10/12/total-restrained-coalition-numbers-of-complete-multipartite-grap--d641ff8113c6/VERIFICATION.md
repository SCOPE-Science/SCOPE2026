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

The proof is analytic. A direct checker is included as a finite stress test.

`verify.py` builds each complete multipartite graph from its part-size profile and tests the TRD definition from adjacency itself. It enumerates every set partition and computes the exact largest total restrained coalition partition. It compares this exact value with the claimed formula for every connected complete multipartite profile of orders \(2\) through \(8\).

The checker also verifies the structural TRD criterion for every vertex subset in those profiles. It does not use the closed classification when deciding whether a set is TRD or whether a partition is a valid total restrained coalition partition.

Finite enumeration does not prove the all-orders statement. The infinite theorem rests on the structural argument in `RESULT.md`.
