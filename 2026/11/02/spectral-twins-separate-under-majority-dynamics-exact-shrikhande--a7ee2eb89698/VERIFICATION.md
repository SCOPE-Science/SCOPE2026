---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Both 16-vertex degree-six graphs were independently generated directly from rook coordinate agreement and Shrikhande Cayley differences ±(1,0),±(0,1),±(1,1); adjacency common neighbor count two confirms SRG parameters, while rook has eight four-cliques and Shrikhande none. For a binary state x, each site updates to one when ≥4 of six neighbors are one, zero when ≤2, and keeps x_v when exactly 3. Independent direct all-65536-state successor arrays (not read from repository verifier) were decomposed into cycles and predecessor basins; complete values: rook (fixed 302, 2-cycles 1197, periodic states 2696, max t=3, consensus basin each 20789), Shrikhande (142,685,1512,5,28221), entry histograms [2696,14136,29984,18720] and [1512,9304,26240,18496,9024,960]. Both finite-domain iterate identities F_R^5=F_R^3 and F_S^7=F_S^5 were exhaustively checked. Thus this is a complete exact finite census, not an extrapolated sample; all counts are for labeled configurations.

## originality

PASS

Best-knowledge PASS for exact majority-attractor census difference between these classical spectral twin graphs. Prior work proves eventual period one or two for undirected synchronous majority and has published different invariants of the exact graph pair, but no inspected table provides these exact majority basins or transient census. An obscure existing majority fixed-point enumeration could overlap.

## value

PASS

The complete nonlinear time-dynamics comparison gives a useful counterexample to inferring consensus behavior from a graph spectrum or strongly regular parameters, including an exact substantial disparity of unanimity probabilities; natural 16-vertex canonical graphs, no arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
