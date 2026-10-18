---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The metric is inversion count on S_4, equal to graph shortest-path distance on the adjacent-swap Cayley graph with 24 vertices and 36 edges. The audited two standard-library programs enumerate every clique and reduce exact F_2 boundary matrices; K_2 has face vector (24,96,112,30), K_3 (24,168,472,618,384,92) and K_4 (24,228,1112,3042,4848,4592,2592,822,112). Independently implemented BFS/clique enumeration and exact boundary reduction reproduced all K_4 face counts and ranks (0,23,205,907,2135,2708,1882,710,112,0), while cycle-image elimination reproduced 39 Z_2(K_2) generators, rank B_2(K_3)=326 and rank(B_2(K_3)+image Z_2(K_2))=327, so the critical map H_2(K_2)->H_2(K_3) has rank one. This gives eight bars [2,3) and one [2,4), not merely the Betti numbers; ranks of all other degrees give 13 H_1[1,2), five H_4[4,5) and two H_5[4,5). Each vertex has one distance-six antipode, giving K_5=(S^0)^{*12}=S^11 and K_6 a full simplex. Full finite enumeration certifies this one metric; not a theorem about S_n for all n or integral coefficients.

## originality

PASS

The strongest overlapping published result proves complete stagewise HOMOTOPY TYPES of the identical 24-vertex truncated-octahedral graph, including all nonzero Betti dimensions, and is explicitly credited. It does not determine the inclusion map H_2(K_2)->H_2(K_3) or barcode: identical source and target groups Z_2^9 to Z_2 admit image rank 0 OR 1 without extra data. The independently verified rank-one persistence bridge and therefore full barcode are the surviving original claim, not the stagewise homotopy classifications. Best-of-knowledge, with substantial same-day overlap and possibility of an earlier implicit calculation.

## value

PASS

Kendall adjacent-swap distance on the 24 rankings is canonical, and its precise interval decomposition is a natural exact invariant beyond scale-by-scale homotopy. The one surviving degree-two class across scale 3 is not implied by Betti dimensions; knowing that persistence rank provides a reproducible test case for graph-metric persistent homology. Its finite size does not negate the motivation, and no extrapolation beyond S_4 is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
