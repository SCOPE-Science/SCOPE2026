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

Two source-independent constructions of the Petersen colouring graph were tested.

Run `python verify_direct.py` and `python verify_state_model.py` using Python 3. They require no nonstandard modules. The first enumerates all \(3^{10}=59049\) raw named assignments and derives the legal Kempe moves from connected components in the ten-vertex Petersen graph. The second enumerates the \(5\cdot4\cdot3!=120\) colour-partition encodings, constructs transitions symbolically, and checks each transition against connected-component switching.

Observed output from the source files included in this package:

```
DIRECT_PETERSEN_KEMPE_PASS
colorings=120 moves=360 degree=6 quotient_vertices=20 quotient_edges=40
shells_per_coloring=(1,6,25,61,27) radius=4 diameter=4
unordered_distance_distribution=(360,1500,3660,1620)
one_vertex_recoloring_graph=60K2
EXPLICIT_STATE_MODEL_PASS
states=120 oriented_pairs=20 quotient_edges=40 each_state_six_moves=TRUE
base_shells=(1,6,25,61,27) radius=4 diameter=4
```

The direct and symbolic programs exhaust their stated finite state spaces. The theorem also includes an explicit classification proof of every state and Kempe component; the computations do not extrapolate beyond a finite case. The classification has not undergone a separate independent scholarly audit, and exhaustive priority checking of inaccessible historical literature is not asserted.
