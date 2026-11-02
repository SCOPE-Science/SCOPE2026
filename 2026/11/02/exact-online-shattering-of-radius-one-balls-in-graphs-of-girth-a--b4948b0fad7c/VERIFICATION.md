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

# Reproducibility and scope

Run `python verify_closed_balls.py` in an environment with NetworkX and `python independent_check.py` in standard Python. The scripts use distinct state representations: the former represents Boolean neighborhood concepts as bit masks and checks VC traces; the latter directly recurses over candidate centers and decodes Prüfer tree sequences.

Recorded successful checks:

```
ATLAS_CONNECTED_GIRTH_GE5_PASS 35
TREES_PASS 2 through 12 (986 nonisomorphic trees)
EIGHT_VERTEX_SHARP_WITNESS_PASS
ALL_CLOSED_BALL_CHECKS_PASS trees=986 minimal_order=8 minimal_trees=12
INDEPENDENT_ALL_LABELED_TREES_PASS 1440
INDEPENDENT_RANDOM_TREES_PASS 350
INDEPENDENT_UNICYCLIC_PASS 55
INDEPENDENT_EIGHT_VERTEX_WITNESS_PASS
ALL_INDEPENDENT_CHECKS_PASS
```

The complete depth-three witness can be read directly from the tree edges in the theorem: first query vertex `5`; on its positive branch query `0`, and on its negative branch query `2`. The four depth-two branches are respectively distinguished by final queries `1`, `6`, `3`, `3`; the eight leaves correspond to distinct centers `0,5,6,7,1,2,3,4`.

All unbounded statements are proved mathematically; finite computations only check instances. The nonisomorphic-tree census uses NetworkX's generator, and the independent program separately exhausts all labeled trees through six vertices. No third-party audit or formal proof-assistant check is claimed.
