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

# Finite verification record

The standalone `verify.py` uses Python's standard library and requires the co-located `mk_isomorphism_certificates.json`. It checks all \(272\) perfect matchings, all \(1840\) unordered four-factorizations, and reproduces the same family by a separate proper edge-colouring recursion. It checks all \(8808\) Kempe edges by two different implementations, all \(9\) components, every sign, every square face, all eight explicit small-component graph isomorphisms, all \(384\) cube automorphisms acting on the exceptional classes, and all pairwise shortest-path distances inside each component.

The matching recursion is exhaustive because it branches on every available mate of the least unmatched vertex. The colouring recursion is exhaustive because at every step it branches on every locally permitted colour of one uncoloured edge. The complement method uniquely completes three disjoint perfect matchings to a four-factorization; all four factor indices are strictly increasing, so no duplicates are counted. A two-colour union is a disjoint union of alternating even cycles, hence the programme checks every permitted Kempe move. The saved eight isomorphism maps are each checked edge-by-edge and nonedge-by-nonedge against the standard definition of \(GP(8,3)\).

The proof is finite and complete only for the explicitly defined \(Q_4\). Full checks of this finite domain do not prove an analogous theorem for all hypercubes. An independent audit of these calculations and mathematical novelty has not been performed.
