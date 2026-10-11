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

The standalone verifier `verify_tutte_coxeter_mh.py` uses only the Python standard library. It reconstructs the graph from the symplectic generalized-quadrangle model over \(\mathbb F_2\), rather than relying on an asserted adjacency list.

It checks all ordered endpoint blocks for total magnitude length \(5\). For each block it enumerates the degree-\(2\), degree-\(3\), and degree-\(4\) chain bases, constructs the standard smooth-deletion boundary matrices, verifies \(\partial_3\partial_4=0\), and computes exact ranks over \(\mathbb F_2\). It also exhaustively enumerates simple \(8\)-cycles.

Expected terminal output:

```text
vertices=30 edges=45 girth=8
endpoint_profile_d1: blocks=90 C2=8 C3=36 C4=56 rank_d3=8 rank_d4=28 beta=0
endpoint_profile_d3: blocks=360 C2=14 C3=45 C4=40 rank_d3=14 rank_d4=27 beta=4
global_C2=5760 global_C3=19440 global_C4=19440 global_rank_d3=5760 global_rank_d4=12240
MH_3_5_F2_dimension=1440
eight_cycles=90 cycles_per_ordered_distance3_geodesic=4
CHAIN_CONDITION_OK
VERIFY_OK
```

The computation is finite and exhaustive for the stated graph and bidegree. It does not establish integral ranks, odd-characteristic ranks, or a theorem for arbitrary girth-eight graphs.
