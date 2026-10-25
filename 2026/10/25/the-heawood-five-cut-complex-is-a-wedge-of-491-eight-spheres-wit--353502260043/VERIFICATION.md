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

# Reproduction of exact finite checks

Execute `python verify.py` with Python 3 and `networkx`. The checker starts from seven explicit Fano lines and independently produces the entire graph and all disconnected induced five-sets. It computes all 14,633 augmented faces and 96,894 Hasse cover relations, greedily pairs 7,071 disjoint covers, then verifies the complete acyclicity of the *actual* oriented Hasse graph by topological sorting all 14,633 vertices. Thus the Morse certificate checks an exhaustive combinatorial proof of the claimed integral homotopy equivalence. Critical cells after unaugmenting: one vertex and 491 degree-eight cells.

The separate mod-two chain-boundary test verifies positive-degree ranks 13, 78, 286, 715, 1287, 1716, 1716, 1259. The checker reconstructs all 336 graph automorphisms and evaluates signed traces on every invariant oriented simplex, confirming character constancy and multiplicities of all eight graph-vertex cycle types, as well as zero character average.

Completion marker: `HEAWOOD_FIVE_CUT_COMPLETE_EXACT_CHECKS_PASSED`.

Limits: the complete numerical verification is finite (the specified fourteen-vertex graph). Homotopy follows from the verified acyclic matching and Forman's theorem, not from the mod-two Betti values alone. The quotient statement follows from rational finite-group invariants, not from an integral quotient homology computation. Independent validation has not been performed.
