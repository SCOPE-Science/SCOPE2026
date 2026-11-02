---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For inclusive Hamming metric on 48 words [3]×[4]×[4], distances between distinct points are exactly 1,2,3. Below scale1 there are 48 points. At scale1 each clique lies in one coordinate line; 40 line simplices form a good cover, its nerve is a graph of 88 nodes and 144 incidences after triangle contractions, hence a connected wedge of 57 circles. At scale2, forbidden pairs differ in all coordinates, so the Rips complex is Ind(K3×K4×K4). Independently fully enumerated 243,270 augmented faces with exact 0..16 histogram, 432 categorical graph edges, and reconstructed 121,536 disjoint matching pairs plus exactly 198 unpaired four-vertex faces. Independently topologically sorted all 1,843,680 oriented Hasse covers, visiting every face, so acyclicity is complete, not a partial numerical sample. Empty face is matched with vertex; ordinary discrete Morse gives one point and 198 3-cells, an integral wedge of 198 S3. At scale3 the simplex is complete. Distinct homology support degrees force 47 [0,1) bars degree0, 57 [1,2) degree1, and 198 [2,3) degree3; endpoint conventions are inclusive.

## originality

PASS

Qualified best-of-knowledge: searched Resultary by semantic same-object aliases, inspected relevant primary theorem statements, distinguished direct and partial coverage, and found no proven dominating statement of the final claimed exact invariant. Residual risks and incomplete primary sections are explicitly documented.

## value

PASS

This fixed all-nonbinary triple-product complex with two four-letter coordinates is a natural step beyond the known binary-factor proof and smaller 3×3×3 example. A complete integral sphere-wedge certificate and full Hamming Vietoris–Rips barcode give a reproducible sharp finite case of a broader published conjecture without pretending to settle it. This is a natural exact invariant, not an unmotivated arbitrary tiny graph.

The dated certificate retains the supplied scientific assessment, sources and limitations.
