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

The king graph is the nonperiodic square-board strong product, including horizontal, vertical and diagonal attacks. Independently generated row-compatible masks for every 1<=n<=6 and exactly reproduced all complete face-cardinality vectors, including 202,841 faces for n=6. Inspected the checker’s central-first vertex-toggle acyclic matching, exhaustive directed Hasse topological sort including the augmented empty face, signed gradient-path Morse reduction, integer row/column unit elimination to zero residual, and independent original-chain F2 ranks for n<=5. Given the specified complete certificates, the boundary-unit ranks imply the six torsion-free reduced integral Betti vectors and n=5 minimal multiple-positive-degree threshold. Euler calculations independently agree for all six cases; no assertion for n>=7 or wedge homotopy follows.

## originality

PASS

Carnero Bravo 2025 treats the identical strong-product graph family but explicitly determines homotopy for widths m<=4, while the first new multi-positive-degree instances have widths 5 and 6. Earlier non-diagonal square-lattice (Cartesian) work omits king diagonal attacks. These are exact integral values not implied by the verified narrower width results.

## value

PASS

Nonattacking kings on n-by-n boards is a canonical graph-complex family with a directly adjacent published exact theory only for widths <=4. The first nonconcentrated positive homology threshold at n=5 and the complete, torsion-sensitive n=6 vector are natural, motivated finite cutoffs and exact data for extending strong-product topology, not an arbitrary parameter slice or a claimed all-n proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
