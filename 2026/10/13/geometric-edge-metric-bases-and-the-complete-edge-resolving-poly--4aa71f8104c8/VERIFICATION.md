---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Build the 18-vertex (9 point +9 nonvertical affine-line) Pappus incidence graph over F3, 27 edges; confirm BFS distance formulas (same-part coordinate distinction 2 vs 4, incident/not point-line 1 vs 3). The edge-pair discrimination family has 198 distinct nonempty masks from 351 pairs. Exhaustively assess all 2^18 landmark subsets by edge-distance signatures and masks independently: exactly 254100 resolving, coefficients 540,5976,17106,31392,43704,48620,43758,31824,18564,8568,3060,816,153,18,1 in degrees 4..18; none smaller. Four-subset finite equivalence to geometric two-column/two-slope and mixed affine incidence conditions yields 27+27+486 bases; 216 explicit affine-collineation/point-line dual automorphisms partition them into five orbits 54,54,108,108,216. This is a genuinely exhaustive FINITE proof, not extrapolation.

## originality

PASS

Kelenc-Tratnik-Yero introduces edge resolution and examples, Bailey tabulates Pappus ordinary vertex metric dimension 4, Bartoli et al treats biaffine-plane vertex metric bounds with q>=4. None has the Pappus edge-resolving polynomial or orbit decomposition; Resultary found other Pappus magnitude homology and other-graph edge bases, not this census.

## value

PASS

A complete exact all-landmark-subsets invariant of a classical 18-vertex distance-regular incidence graph, with transparent finite-geometric characterization, nontrivial automorphism orbits and quantitative vertex-vs-edge resolution gap, is a motivated useful benchmark for graph metric theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
