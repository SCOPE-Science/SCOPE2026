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

The proof is analytic and covers all integers \(1\le s\le t\). The finite checker is corroborative only.

`verify.py` performs three independent checks from the definitions: it reconstructs complete bipartite adjacency, tests \(2\)-fair domination by exact neighbor counts, and enumerates every set partition for all profiles with \(s+t\le9\). The computed maximum coalition-partition size is compared with the theorem. It also instantiates the explicit construction for every \(4\le s\le t\le40\) and checks that every block has a valid coalition partner.

The infinite upper bound is not inferred from enumeration. Its critical step is the complementary occupancy rule: for \(s,t>2\), every proper \(2\)-fair dominating coalition union has shore occupancy \((2,2)\). The resulting block-size excess must be at least four for \(s\ge4\); the proof in `RESULT.md` handles singleton blocks on zero, one, or both shores separately.

Unproved limits: no claim is made for \(k\ge3\), for non-complete-bipartite graphs, or for a classification/count of all maximum partitions.
