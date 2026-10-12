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

# Exact verification record

Run `python3 verify.py` using Python 3.8 or later. This file has no external dependencies and contains the full finite calculation; it does not import unreleased data or require any network connection.

Expected successful output:

```
VERIFY_OK vertices=20 edges=30 girth_at_least_6=checked
VERIFY_OK all_subsets=1048576 direct_projection_agree=true min_size=8 minimum_sets=1475
VERIFY_OK optimal_splits=3:300,4:875,5:300 aut_group_size=240
VERIFY_OK orbits=13 sizes=5,30,60,60,120x7,240x2 representatives=exact
```

The program enumerates all \(2^{20}=1{,}048{,}576\) subsets twice by separate predicates: one directly intersects the twenty open-neighborhood bitmasks with the candidate selected set; the other independently intersects the ten Petersen disjointness masks on each bipartition side. For the accepted optimum sets, it enumerates the complete permutation and side-swap action and verifies the partition into thirteen orbit representatives. Assertions test the specific minimum, total number, side counts, group size, representatives and orbit sizes. The proof of the lower bound uses an unrestricted combinatorial obstruction for every hypothetical size-seven locating-dominating set. The census is exact for this single finite graph; it provides no theorem for higher-order bipartite Kneser graphs, and it does not establish priority over all unindexed historical literature.
