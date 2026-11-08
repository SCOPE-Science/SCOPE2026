---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The 12 exact integer triples 2p_a+p_b yield all 66 squared distances 8(18),24(24),32(12),40(12), divided by eight. Independent regeneration gave face vectors 34/114/342 nonempty faces at squared thresholds 8/24/32. I independently fetched all three actual matching certificates (Git object blobs 0e28c0a5,1b10a05f,ffe3a246), checked every pair and every directed Hasse cover, and topologically sorted all 34,114,342 faces; all acyclic, leaving respectively (c0,c1)=(1,3),(c0,c2)=(1,5),(c0,c2)=(1,1). I separately rebuilt the oriented 20-triangle convex boundary cycle at sqrt(3), exact greedy 146 free-face collapse sequence at squared threshold 32, and integral transfer to the (V,E,F)=(10,24,16) sphere with all 16 final triangle coefficients ±1, establishing a primitive integral H2 generator. The original source code checks connectedness, triangle edge valences, cyclic vertex links and boundary-zero. Matching/collapse plus Forman and integral chain retraction prove the claimed homotopy types and split-surjective map; 11 degree-zero intervals and the 3/4/1 remaining bar multiplicities follow. Finite enumeration is exhaustive only for these 12 specified vertices.

## originality

PASS

The graph-metric result already covers the first two nontrivial types (3 circles,5 two-spheres); this overlap is excluded from originality. The new Euclidean squared-distance-32 intermediate S2, distinct sqrt(5) terminal threshold and primitive integral persistence inclusion are not implied by graph radius 3, which adds both classes together. The Platonic-solid classification and its dissertation concern different vertex configurations, with no dominating general Archimedean theorem identified.

## value

PASS

The regular truncated tetrahedron is a natural Archimedean 12-point Euclidean configuration. The previously studied graph shortest-path metric merges geometric diagonal scales; resolving them reveals a genuine longer-lived sphere and, crucially, which primitive H2 class persists. Exact integral barcode and inclusion maps are useful independently of a broader polyhedron census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
