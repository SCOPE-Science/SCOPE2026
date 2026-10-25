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

# Finite verification and limits

Run `python verify.py` with standard Python 3. The program constructs the total cut complex from complement support conditions and evaluates signed fixed-face traces, independently of the topological proof. It compares them with the vertex-sign-twisted exterior-power character. It additionally constructs mod-two simplicial boundary maps and checks homology dimensions.

Expected output:

```
CLUSTER_GRAPH_EQUIVARIANT_CHARACTER_VERIFIED 8672
CLUSTER_GRAPH_MOD2_HOMOLOGY_VERIFIED 5
```

The direct signed traces cover 8,672 small-group actions, including internal transpositions and equal-size block exchanges. The mod-two tests cover five parameter tuples. These are finite and do not establish absence of integral torsion for arbitrary parameters; that fact follows only from the proof's integral chain and Alexander-duality arguments. Independent audit has not been performed.
