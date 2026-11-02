---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed correspondence between vertices of KG(n,2) and auxiliary K_n edges. A forest is bipartite, hence splits into two intersecting edge families; by the star-or-triangle lemma each part is a star or a triangle. Four-cycle obstructions in the two-star/triangle cases yield |F|<=max(7,n) and equality exactly the K4+pendant C families or full-star+off-edge S families. Explicit induced-disjointness graphs are forests; intersection counts between distinct extremal families yield the claimed disjoint clique exchange components. Independent exact Python subset enumerations for n=5,6,7 found, respectively, 20,120,525 optimum families and clique-component profiles 5 K4,15 K8,35 K12 +7 K15; all best+1 subsets were checked nonforest. Original C++ verifier was inspected, not merely trusted. For n>=8, all-order classification relies on the proof.

## originality

PASS

Large-n star-plus-one-edge extremality follows from a stronger 2018 K_{2,2}-free Kneser theorem and is explicitly prior. New portion is the sharp first threshold, all low-n equality cases and full one-swap optimum-exchange clique decomposition.

## value

PASS

Maximum induced forest/minimum feedback vertex set of the natural Kneser KG(n,2), including the sharp crossover n=7/8, exceptional geometry and connected components under optimal one-element replacement, is a motivated complete extremal and reconfiguration classification. The eventual large-n star shape alone is prior work, not counted as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
