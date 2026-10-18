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

# Verification record

The theorem is proved for all positive dimensions and all factor lengths at least two; the finite scripts do **not** certify the unrestricted quantifiers. For every coordinate \(i\), ideal cardinality is \(\prod_j(a_j+1)\), filter cardinality is \(\prod_j(m_j-a_j)\). The critical inversion is the rank-adjacent strict-neighbour formula in the proof. Test scripts implement the full strict transitive order without a supplied cover graph.

`check_chain_products.py` verifies the colour partition, exact orbit/cardinality formula and independent arithmetic recovery of the coordinate pairs for 112 concrete multisets, totalling 9,403 vertices. `check_group_orbits.py` recomputes the graph relation and refinement independently and compares against explicit factor-coordinate permutation orbits for 56 concrete multisets, totalling 2,425 vertices. The logs store observed counts, and source scripts are included for reproducibility. Boundary vertices and repeated/unequal factor lengths are covered by proof.

Unproved: optimal number of rounds in all factor configurations, identification among arbitrary posets, extension to non-product distributive lattices, independent literature priority. Independent audit: not performed.
