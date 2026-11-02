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
# Verification evidence and scope

The proof of the all-parameter theta classification and the tree/unicyclic cases is given in `RESULT.md`. The supplied standalone Python program implements two separate graph-theoretic bond enumerations: connected bipartitions and inclusion-minimal edge deletions. Their output is compared on each graph tested.

The file `house_depth3_certificate.json` contains the actual six-edge graph, the ten distinct bond masks, and a complete binary query tree of depth three with eight distinct terminal bond witnesses. For every leaf the verifier checks all edge labels along that root-to-leaf path against the witness mask. Exhaustive triple-support testing confirms that no three edges of the house are VC-shattered. A separate exact Littlestone version-space recurrence confirms online depth three.

The program compares the theta product-and-pair formula with direct graph cuts for nine small path-length triples. It also enumerates every simple connected labeled graph on two through five vertices having at most six edges, a total of 595 graphs. It finds 60 labeled strict-gap cases, all relabelings of one five-vertex, six-edge graph, and verifies their dimensions using exhaustive Boolean traces and the exact online recurrence. Graphs with six or seven vertices and at most six edges are covered by the separate universal tree/unicyclic argument rather than an incomplete enumeration.

Actual standalone execution command:

`python verify_bond_threshold.py house_depth3_certificate.json`

Observed terminal assertions:

```
THETA_GRAPH_BOND_FORMULAS_PASS tests=9
EXHAUSTIVE_SHARP_SIX_EDGE_THRESHOLD_PASS connected_labeled_graphs=595 exceptional_labelings=60 exceptional_isomorphism_types=1
HOUSE_CERTIFICATE_PASS leaves=8 bonds=10 vc=2 ldim=3
ALL_GRAPHIC_BOND_SHATTERING_CHECKS_PASS
```

This is exact finite verification of the stated finite checks, not independent audit of the mathematical originality or the universal proof. Historical priority, generalization to all multicyclic graphs, and possible classifications in alternative terminology remain outside the verified scope.
