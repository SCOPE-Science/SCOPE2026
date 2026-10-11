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

The exact verifier is `verify.py` and uses only the Python standard library. It rebuilds the Heawood graph from the incidence rule, enumerates the ordinary \(3\)-cut complex, reconstructs the sequential element matching, checks all matching pairs, and certifies acyclicity by topological sorting of the complete oriented Hasse diagram. It separately computes all simplicial boundary ranks over \(\mathbb F_2\).

Observed exact checks:

- \(14\) vertices and \(21\) edges.
- \(42\) connected three-sets and \(322\) disconnected three-sets.
- \(322\) facets and \(16{,}235\) nonempty faces.
- Face vector \((14,91,364,1001,2002,3003,3432,3003,2002,1001,322)\).
- \(8{,}099\) matching pairs.
- Critical-cell profile: one cell in dimension \(0\), \(36\) cells in dimension \(10\), and none otherwise.
- \(112{,}924\) Hasse cover relations checked in the acyclicity test.
- Reduced mod-\(2\) Betti vector \((0,0,0,0,0,0,0,0,0,0,36)\).

The computation proves only the displayed finite Heawood claim. It is not evidence for an infinite graph family, for shellability, or for a stronger classification.
