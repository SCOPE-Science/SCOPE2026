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

# Reproducibility and proof boundaries

Run `python verifier.py` with Python 3. The program constructs each tested \(K_{m,n}\), verifies mutual visibility by the original all-selected-pairs geodesic condition, creates all legal fixed-size token-slide edges, and performs exhaustive BFS. The observed output is:

`VERIFY_OK bfs_cases=68 bfs_pairs=617027 bfs_configurations=4392 type_extrema=2175`

BFS cases are all ordered host sizes \(3\le m\le n\le7\) with \(m+n\le10\), including every feasible level up to the maximum, with disconnected top layers checked as isolated points. All ordered reachable source-target pairs were checked against the theorem's exact formula; BFS does not rely on the proposed closed metric. The independent combinatorial parameter check enumerates feasible occupancy levels and pairwise intersections for all \(3\le m\le n\le17\) and all connected layers, comparing their exact possible symmetric differences with the claimed diameter.

The infinite theorem is established by the explicit token-slide path and sharpness constructions in `RESULT.md`; finite enumeration alone cannot certify it. No independent mathematical audit has been performed. Historical-priority concerns and the disconnected maximum-layer exclusion are recorded in `RESULT.md` and `REVIEW.md`.
