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

Use the cubic Petersen graph with outer pentagon, inner pentagram and five spokes. Exhaustively recounted every 1024 subset and confirmed exact nonempty face totals (75,260,620,785) and mod-two reduced Betti vectors at d=0,1,2,3: respectively 4 in H2, 1 in H3, 1 in H3, 6 in H5. Reconstructed all three fixed-order augmented toggle Morse matchings at d0,d2,d3, giving 36,310,390 pairs, precisely critical masks four 2-cells; one 3-cell; six 5-cells, and directed topological sorts visiting every nonempty face. Independent F2-to-F1 collapse algorithm checks an immediate unique coface and maximality on every step and removed exactly 180 free-face pairs, reaching the 260-face F1 unchanged. Therefore the d1-to-d2 inclusion is a genuine simplicial simple-homotopy equivalence (not merely rank agreement), and integral wedge homotopy types and persistence follow. Saturation d>=3 is exact because graph maximum degree 3. The result concerns vertex-induced forests, not edge matching complexes.

## originality

PASS

Carnero Bravo supplies the graph-forest filtration framework but not Petersen graph, whose overlapping 5-cycles exclude treated cactus and graph-product specializations. Published Petersen Ind2(P) S3 is explicitly prior and not counted new. The d2→d1 180-simple-collapse, endpoint d3 wedge six S5 and precise integral persistence are additional facts; ordinary Petersen independence Betti numbers alone cannot imply them.

## value

PASS

The Petersen graph is canonical noncactus cubic girth-five test object for the entire induced-forest degree filtration; complete integral homotopy and persistence are natural exact invariants. Explicit 180 collapses give map-level simple-homotopy information stronger than an already known F1 homotopy type, and the terminal six-five-sphere stage is a nontrivial distinct classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
