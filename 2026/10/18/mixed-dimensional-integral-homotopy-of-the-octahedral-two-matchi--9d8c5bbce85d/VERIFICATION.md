---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Reconstructed M_2(K_{2,2,2}) as degree-at-most-two subsets of the twelve precisely specified graph edges. Independent enumeration of all 4096 masks yielded 772 faces including empty, nonempty face vector (12,66,196,297,180,20), 377 disjoint matching pairs and an acyclic oriented Hasse graph (771 nodes, 2928 covers). Independent signed algebraic Morse projection recovered the claimed 6×10 integer attaching matrix: rank three with a unit 3×3 minor and all nonzero Smith factors one. The one-vertex CW model has six 3-cells, ten 4-cells and none in dimensions 1,2 or >=5. Thus π3 of its 3-skeleton is Z^6, the degree matrix fully controls 4-cell attachments, and integral homotopy reduces to three S3 plus seven S4. Separate mod-two boundary ranks (1,11,55,141,153,20) give reduced Betti (0,0,0,3,7,0); finite enumeration is exhaustive for this graph only.

## originality

PASS

Best-of-knowledge statement-level comparison of the precise functor, object and parameter with relevant full-text primary sources and published mathematical results. Ordinary matching M_1(O) and discrete Morse matching complexes on the same graph differ from M_2(O), since two incident selected edges are allowed here and homology dimensions differ. Vega covers wheel/caterpillar two-matchings; Singh covers M_(n−2)(K_n) and M_(n−1)(K_n,n). O=K_2,2,2 is neither a wheel/caterpillar nor complete/bipartite, so those statements do not imply the 3/7 sphere claim. Checked the published octahedral M_1(O) exact homotopy/character and octahedral discrete Morse complex; their face definitions differ from M_2(O). No same M_2(O) 3/7 exact table in inspected primary/results; absence from ranked search alone cannot prove priority. The existing M_1(O) ≃ wedge^11 S1 and its full symmetry character are not sufficient to derive M_2(O); passing to the higher-degree-bound complex adds interacting faces and new attaching maps. Singh’s graph/threshold parameters exclude O. Any remaining bibliography uncertainty is retained as residual risk, not presented as novelty proof.

## value

PASS

The smallest maximally symmetric complete-tripartite octahedral example with a nontrivial higher matching threshold has a nonpure complex and genuine adjacent-dimensional integral sphere-wedge homotopy, stronger than a Betti or Euler-characteristic table. It supplies a concrete computable reference point for higher matching complexes beyond complete and bipartite families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
