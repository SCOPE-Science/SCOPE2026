---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

Enumerated every nonempty independence face of standard Cayley Shrikhande on Z4² with ±(1,0), ±(0,1), ±(1,1) and of the 4×4 rook graph. Both have 16 degree-six vertices and 48 edges; exact face vectors (16,72,96,16) and (16,72,96,24). Independently regenerated both deterministic vertex-toggle matchings, 88 and 96 matched Hasse pairs, respectively; acyclic directed Hasse orientation verified by independent full Kahn traversal of all 200 / 208 faces and 496 / 528 Hasse covers. Unmatched cells: precisely one 0-simplex and 23 / 15 two-simplices. Forman Morse CW model then a point with only degree-two attachments, necessarily wedges of 23 and 15 copies of S². This proves integral homotopy rather than extrapolating from mod2 Betti alone. The auxiliary polynomial recursion was separately inspected.

## originality

PASS

Mathematical comparison was made at the level of Ind(S)=Cl(complement S) and Ind(R)=4×4 chessboard complex, not original-graph clique complexes. Classical chessboard topology can cover the rook half alone; Barmak star-cluster suspension and claw-free results do not give exact Shrikhande 23-sphere wedge (Shrikhande contains triangles and induced claws). A later exact Resultary work titled "The Shrikhande independence complex is a wedge of twenty-three 2-spheres" contains the same Shrikhande conclusion, independently of rook. GitHub observed assessed paired-theorem source commit at 2026-10-11 13:15:59 UTC and observed single-graph source commit at 13:16:41 UTC. Since the latter source commit is 42 seconds after this assigned source, it is not established as chronologically prior; timestamps are not evidence of independent intellectual priority, and this close overlap is high residual originality risk. No earlier public source inspected implies exact Shrikhande wedge; best-of-knowledge PASS is not priority certification.

## value

PASS

The smallest familiar nonisomorphic strongly regular parameter-twin pair has same (16,6,2,2) parameters and graph spectrum and identical f0,f1,f2 but distinct integral independence-complex wedge homotopy types (23 vs 15 two-spheres). A full acyclic discrete Morse certificate gives a stronger and reproducible topological invariant than graph spectrum or simplex face count. This is a natural finite comparison, not an arbitrary unmotivated table slice; the already-known graph nonisomorphism and known rook chessboard object are not passed off as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
