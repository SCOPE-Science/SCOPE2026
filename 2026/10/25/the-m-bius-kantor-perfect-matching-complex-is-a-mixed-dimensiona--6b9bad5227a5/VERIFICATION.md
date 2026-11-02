---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The generalized Petersen GP(8,3) has 16 vertices and the specified 24 edges. The extendibility simplicial complex consists ONLY of subsets of its 33 perfect matchings, not all 11,067 nonempty graph matchings. An independent new implementation recursively enumerated all 33 perfect matchings and their 6051 distinct nonempty subfaces; the face vector is (24,228,984,1842,1752,924,264,33). Regenerating the exact 24-pivot face matching yields 3019 pairs; the full 27,192 oriented Hasse covers on 6051 faces topologically sort without a cycle. Remaining faces are one vertex, four 2-faces and eight 3-faces. The integral signed gradient-path elimination of the full 4-by-8 3-to-2 cellular boundary was independently recomputed as zero, not inferred from mod-2 Betti ranks. The Morse 2-skeleton is ∨⁴S² and pi2=H2=Z⁴, so the zero vectors make all eight 3-cell attaching maps null; hence ∨⁴S² ∨ ∨⁸S³. The independently authored computation and full bundled source were inspected; the finite check is exhaustive for the exact finite graph, not a claim about arbitrary GP(n,k).

## originality

PASS

Resultary primary RESULT.md for the SAME GP(8,3) computes the ordinary matching complex as ∨⁸S⁴ ∨ ∨⁴S⁵, using all 11,067 nonempty matchings. The submitted 6051-face complex retains only extendible matchings and has entirely different homotopy degrees. The 2022 honeycomb perfect-matching complex paper treats planar honeycomb patches; a 2026 Möbius LADDER paper treats a distinct graph family. The 33 perfect-matching count is previously known and explicitly excluded from novelty. No inspected theorem covers this new exact filtered complex.

## value

PASS

Extendibility to a perfect matching is a natural global matching constraint. The exact mixed-dimensional integral homotopy provides a concrete canonical counterpoint to the ordinary matching complex on the same symmetric cubic graph and exhibits structural changes not implied by the perfect-matching count. The deterministic complete Morse certificate makes a rigorous finite homotopy classification valuable independently of an all-Petersen-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
