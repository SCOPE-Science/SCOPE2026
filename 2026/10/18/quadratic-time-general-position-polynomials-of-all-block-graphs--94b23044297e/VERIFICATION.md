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

# Computational verification

The standalone program `block_gp.py` takes a labeled connected simple graph by its edges, identifies its biconnected components, verifies that they are cliques, and calculates every coefficient by the two-state incidence-tree recurrence. Its independent companion `gp_block_verify.py` constructs graph distances by breadth-first search and checks a candidate selection directly against all forbidden triples, then exhaustively enumerates the subsets of each sampled graph. Both are standard-library Python 3 scripts.

Actual execution: `python3 gp_block_verify.py`

Recorded output:

```
VERIFICATION_OK tested_block_graphs=3000 exhaustive_vertex_subsets=2068500 large_blocks=30,50,100,200
```

The test suite compares against independent brute force for 3,000 generated block graphs of orders up to thirteen, totaling 2,068,500 examined subsets. For larger block structures it compares independent dynamic-programming implementations and the known relationship between maximal degree and simplicial vertices. Its random construction is seeded and reproducible. The graphs sampled are not an exhaustive census of all labeled block graphs. The mathematical proof covers all orders, clique sizes and incidence-tree shapes; finite tests alone would not establish this.

Scientific limitations: The result assumes connected block graphs, and the coefficient-operation bound abstracts away multiprecision integer costs, which remain polynomial. The theorem and software have not been independently audited.
