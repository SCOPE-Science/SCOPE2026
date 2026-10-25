---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The Shrikhande and 4x4 rook graphs have the same SRG parameters (16,6,2,2) but distinct neighborhoods. The vertex-subset k=2 higher-independence condition is induced maximum degree <=1. Exhaustive enumeration of all 65536 masks for each graph yields nonempty f-vectors (16,120,384,544,240,32) for Shrikhande and (16,120,384,528,144) for rook. The given pivot orders make respectively 639 and 543 disjoint matched face pairs. Independent recomputation of every Hasse incidence and Kahn acyclicity check leaves one critical vertex plus 57 or 105 critical dimension-three faces, no other cells. Discrete Morse thus gives integral homotopy wedges 57 S3 and 105 S3, not merely field homology. Boundary-rank checks separately corroborate. The finite universe is exhaustively examined, so finite proof is sufficient for these named graphs.

## originality

PASS

Best-of-knowledge PASS: published Shrikhande/rook *ordinary* independence stage differs (23 vs 15 S2), but that does not imply a second-independence wedge. Existing higher-independence theorems treat complete multipartite, trees, cycles, whiskered and chordal classes, not this nonchordal pair. A graph-edge two-matching or neighborhood complex is a different face predicate.

## value

PASS

A natural co-spectral strongly regular twin pair is separated at the second higher-independence stage by the full integral homotopy type, measuring a graph topological invariant invisible to identical SRG parameters. The precise complete finite classification and integral sphere-wedge geometry are not just a routine graph label or a single unmotivated small coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
