---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For the ordinary OPEN Lovasz neighborhood complex of T_7=L(K_7)=J(7,2), vertices are the 21 two-edges; N(e) has 10 other incident edges. I independently enumerated every nonempty subset of all 21 N(e), deduplicating 18,494 simplices, with f=(21,210,1190,3780,5187,4410,2520,945,210,21), Euler=-238. An independently written greedy discrete-Morse construction (not copied from the repository certificate) keeps active faces; while a codimension-one face has exactly one active coface it pairs the lowest-dimensional/lowest-mask such face with that coface; otherwise removes the highest-dimensional/lowest-mask active face as critical. It produced 9,120 disjoint incident pairs and exactly one critical 0-cell, 246 critical 3-cells and seven critical 4-cells. An independent topological sort of the entire directed Hasse graph (all unmatched facets downward and matched edges upward) visited all 18,494 faces, so the matching is acyclic. Recomputed the integral signed gradient-path 4-to-3 differential from this independently generated matching, with unit incidence pivots; all seven boundary vectors were identically zero over Z. Forman gives a CW complex with exactly these cells; the 3-skeleton is a wedge of 246 S^3, 2-connected, so Hurewicz identifies pi_3 with H_3=Z^246; zero signed degree for each 4-cell forces its attaching map to be nullhomotopic. Thus the entire complex is homotopy equivalent to (vee^{246} S^3) vee (vee^7 S^4), integrally torsion-free. No claims for n>=8, equivariant homotopy, closed neighborhoods or graph powers are inferred. This is a proof for the single finite complex, not extrapolation from a partial sample.

## originality

PASS

Best-of-knowledge PASS. Exact same-object published Resultary work determines only mod-two homology in degrees 3 and 4, explicitly disclaiming integral torsion, attaching maps and homotopy equivalence. The present complete acyclic matching and integral null attachments strictly strengthen that statement. Full-text graph-topology literature inspected distinguishes other complexes (clique complex of L(K_n)), other graph families (paths/stars/complete graphs), and fundamental-group constructions; no inspected theorem entails this exact integral T_7 wedge. The finite graph is canonical and the statement has genuinely higher information content. Search noncoverage is not a universal novelty guarantee.

## value

PASS

The triangular/Johnson graph J(7,2) is a natural association-scheme graph, and T7 is the first member of this family with mixed-degree known neighborhood F2 homology. That previously published exact table explicitly leaves integral torsion and nontrivial 4-cell attaching maps open. The present finite but complete integral homotopy classification resolves these specific natural questions with a constructive perfect acyclic matching and all-zero integer Morse boundary. It supplies an exact topology benchmark for graph neighborhood complexes, beyond mere field Betti computation. No unproved broad family theorem is claimed or needed for this single finite object to be mathematically useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
