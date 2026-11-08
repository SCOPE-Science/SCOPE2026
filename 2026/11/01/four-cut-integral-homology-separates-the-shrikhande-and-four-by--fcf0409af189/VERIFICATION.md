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

Independent direct enumeration of all 16-vertex subsets and connected four-sets found 1200 disconnected 4-sets in K4□K4 and 1152 in the Shrikhande graph. The Alexander-dual face vectors are respectively (16,120,560,620,288,48) and (16,120,560,668,288), 1652 nonempty each; independent stage-toggle Morse matchings give 767 and 776 pairs and acyclic complete Hasse graphs (6128 and 6032 incidences). Rook critical cells: one 0-cell, 96 two-cells, 21 three-cells with zero Morse differentials. Shrikhande critical cells: one 0-cell, 69 two-cells, 12 three-cells, 18 four-cells; independent exact signed Morse reductions give rank4 ∂3 and rank6 ∂4, Smith nonzero factors all 1, giving free dual ranks H2=65,H3=2,H4=12. Integer Smith checks exclude torsion. Combinatorial Alexander duality on 16 vertices shifts to Htilde_i(∆4)=Htilde^{13-i}(K), yielding R degrees 10:21,11:96 and S degrees 9:12,10:2,11:65, all free. Facet complements all cardinality 12, hence pure dim11; nonzero lower homology obstructs shellability. Reduced Euler characteristic independently -75 for both.

## originality

PASS

The standard k-cut definition, duality and general topological tools belong to Bayer et al.; its published graph families and the path-grid theorems in the sequel do not contain the two strongly regular examples at k=4. Prior same-graph results concern ordinary independence or scale-two Čech complexes; a general rook k=3 formula is not a four-cut theorem. No exact equivalent table identified; unindexed results remain possible.

## value

PASS

These are the unique two nonisomorphic strongly regular graphs with parameters (16,6,2,2), making them a natural controlled comparison. Their ordinary four-cut complexes have the same purity and reduced Euler characteristic but sharply different *integral* homology, a meaningful discriminating invariant that neither adjacency spectrum nor Euler characteristic detects.

The dated certificate retains the supplied scientific assessment, sources and limitations.
