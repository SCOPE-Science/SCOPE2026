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

`verify.py` is a standalone checker using only the Python standard library. It reconstructs the Heawood graph from the Fano incidence rule, enumerates all \(2^{14}\) vertex subsets, verifies the full independence face vector, constructs the sequential matching, and checks acyclicity by topologically sorting the complete oriented Hasse diagram.

The expected independent-set counts by cardinality are \((1,14,70,154,147,56,14,2)\). Exactly six faces remain critical, all of cardinality \(4\), so all critical simplices have dimension \(3\). The empty face is matched.

As an independent chain-level check, the program computes mod-\(2\) simplicial boundary ranks \((13,57,97,44,12,2)\), yielding Betti numbers \((1,0,0,6,0,0,0)\). It also verifies directly that the comparison graph \(G_7^3\) has a \(4\)-cycle while the Heawood graph has no \(4\)-cycle.

A successful replay ends with `HEAWOOD_INDEPENDENCE_VERIFY_OK`. The computation proves only this finite graph case.
