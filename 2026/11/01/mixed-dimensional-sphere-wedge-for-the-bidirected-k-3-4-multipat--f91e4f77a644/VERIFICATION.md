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

The bidirected K_{3,4} has exactly 24 ordered arcs and its multipath faces are arc subsets with indegree/outdegree <=1 and no directed cycles (including 2-cycles), equivalent to disjoint simple directed paths. An independently written recursive all-arc enumerator found 3301 augmented faces and exactly 144 six-arc facets; an independent explicit subset-size<=6 bounded check in the source code corroborates completeness since 7 vertices prohibit >6 arcs. Reconstructed 1608 augmented toggle matches, all 13104 Hasse covers and full 3301-vertex acyclic ordering, leaving 37 critical 3-cells, 48 4-cells and one 0-cell. Independent *signed integer* Morse projection computed the entire 37x48 matrix and found every entry zero; the Hurewicz isomorphism pi3(vee^37 S3)=Z37 gives 37 S3 +48 S4. Pure dimension-five with H3 and H4 nonzero is not shellable. The finite proof applies precisely to this digraph, not every bidirected K_{m,n}.

## originality

PASS

Best-of-knowledge PASS after direct full primary reading: Caputi–Collari–Di Trani–Smith Theorem 3.7 of 2024 applies a one-way bipartite orientation with 12 arcs and yields only Euler characteristic, while current bidirected K3,4 has 24 arcs, directed two-cycles and a complete integral wedge classification. The full 2026 Caputi–Collari–Smith primary text studies bidirected polygons/paths and restricts its acyclic blow-up comparison to no directed cycles, inapplicable here. Full Resultary bidirected double-star theorem treats trees, not complete bipartite K3,4, and Morse K3,4 or 2-matching K3,4 are different complexes.

## value

PASS

The smallest nontrivial complete bipartite bidirected case K3,4 beyond one-way chessboard matchings supplies a natural missing arc-cycle-containing multipath invariant. Its two adjacent nonzero homotopy degrees, exact primitive integral attachments and purity/non-shellability tension are meaningful relative to published acyclic bipartite Euler-count formulas and bidirected path/polygon or double-star families; future comparisons of more general bidirected multipartite complexes can use this precise benchmark without a general-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
