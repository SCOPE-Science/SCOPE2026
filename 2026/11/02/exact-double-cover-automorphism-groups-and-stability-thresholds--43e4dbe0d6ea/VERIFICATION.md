---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

On t>=2 the hub is uniquely maximum-degree; both lifted hubs are uniquely maximum-degree in the connected bipartite cover. Removing them leaves 2k free K2 components (one from each shore of each peripheral K2) and the connected, side-marked B(K_r)=K_{r,r} minus matching for r>=3. The pointwise lifted-hub stabilizer is S_{2k} times the wreath factors, and the canonical shore exchange centralizes it; the expected lifted automorphisms preserve a pairing of 2k edge components and yield subgroup S_2 wr S_k. Group-order index follows. At t=1 the bouquet is a complete graph with stable crown cover. The graph is connected, contains triangles, and is open-neighborhood twin-free. Independent networkx isomorphism enumeration checked seven small mixed cases (not the infinite proof).

## originality

PASS

The construction already yields unstable triangular friendship bouquets, so mere existence is covered. The group decomposition for arbitrary mixed clique sizes and exact factorial excess index survives comparison of group actions, not merely titles.

## value

PASS

The exact full symmetry group, factorial instability index and sharp k=1 threshold classify a natural infinite graph family. The invariant depends only on triangular blades even with arbitrary larger blades, a structural phenomenon beyond the existing qualitative instability construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
