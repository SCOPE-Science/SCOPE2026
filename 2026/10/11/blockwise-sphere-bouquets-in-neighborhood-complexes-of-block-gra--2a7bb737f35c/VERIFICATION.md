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

# Reproducible verification

Run `python3 verify.py` from the directory containing the script. The code uses the Python standard library only and constructs each open-neighborhood complex by enumerating all nonempty subsets of the open neighborhood of each graph vertex; it obtains homology dimensions by direct binary Gaussian elimination on simplicial boundary matrices.

The completed run returned:

```
VERIFY_OK exhaustive_labeled_block_graphs_n2_to6=4792 random_block_graphs=150 gluing_identities=99 branch_tree_line_graphs=100 signed_automorphisms=72 random_orders=[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28, 29]
```

In the small exhaustive loop, all connected labeled graphs with two to six vertices are considered and precisely those for which every biconnected block is complete are subjected to the theorem's predicted Betti-number comparison. Larger test graphs are produced by recursively gluing random complete blocks along individual vertices. The 99 gluing checks compare literal face sets, not merely homology. The tree tests construct a line graph from an independently generated tree and compare homology with the **original tree's branch degrees**, independently of the block counter. The symmetry test exhausts the 72 graph automorphisms of two four-cliques meeting in one vertex and tests the oriented boundary-chain transformation, including signs.

**Limit of computation:** these finite mod-two ranks neither certify integral torsion-freeness nor establish homotopy types for every order. Those claims rely on the full elementary block-gluing proof in `RESULT.md`. In particular, a collection of Betti numbers alone does not certify a wedge of spheres, and no such inference was used.
