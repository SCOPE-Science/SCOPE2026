---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A multipath has ≤n−1 arcs, so K=X(G) is at most d=n−2 dimensional. The closed star of added arc b is a contractible cone A. The top relative simplices C_d(K,A) are exactly Hamiltonian s→t paths avoiding b; each such facet has all codimension-one faces in A since deleting any path arc destroys its s-to-t route, so the relative differential vanishes. For each P the missing Hamiltonian directed cycle P+b has all proper subsets in K, and its formal simplex boundary is a genuine embedded d-sphere with relative class ±[P], proving the full integral isomorphism. Collapsing the (d−1)-skeleton and projecting onto these selected P facets produces r; the wedge inclusion i of cycle boundaries has r∘i degree one on each sphere and no cross-terms, also for d=1. Independently enumerated all 136 source/sink allowed digraphs for n=3,4 and checked mod-two top chain nullity equals h; this finite check supports but does not prove the general integral theorem. No claim to calculate all lower-dimensional homology.

## originality

PASS

Caputi–Collari–Di Trani–Smith analyze multipath complexes of transitive tournaments, including reversed long arc Euler characteristic and wedge-type results for the unreversed transitive tournament, but their stated theorems do not provide the arbitrary source/sink feedback arc top integral homology and explicit sphere retract. This theorem is a natural generalization from one particular construction to every finite such digraph, with distinct top-homology and homotopy-summand conclusions.

## value

PASS

Connects the NP-hard Hamiltonian s–t path count to a canonical top reduced integral homology rank and exhibits explicit homotopy sphere retracts; gives a robust structural bridge between graph cycles and simplicial multipath topology, not merely computation of one graph. The theorem leaves lower homology open and does not overstate a full wedge decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
