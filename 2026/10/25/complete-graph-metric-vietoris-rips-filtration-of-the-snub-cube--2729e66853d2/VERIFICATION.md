---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational verification

Run `python3 snub_certificate.py` in the directory containing the extracted files; it requires only the Python standard library. Assertions verify the exact rational interval bracketing the algebraic coordinate, all pairwise adjacency inequalities, regularity and diameter, each complete Rips face set at scales one through three, every elementary free-face collapse, connectivity and vertex links of the scale-two residual closed surface, the complete scale-three matching, and global absence of a closed gradient path by topological sorting.

Observed replay output:

```
scale 1: 116 faces; 40 elementary collapses to connected graph (16 vertices, 20 edges); wedge of five circles
scale 2: 1374 faces; 662 elementary collapses to a closed connected triangulated surface, chi=2; sphere
scale 3: 36804 faces; global acyclic Morse matching 18399 pairs, 1 vertex and 5 critical dimension-5 cells; wedge of five 5-spheres
scale 0: 24 isolated points. Scale >=4: simplex on all 24 vertices.
PASS: complete homotopy filtration and exact finite Morse certificate
```

The checker is a finite exhaustive certificate, not a theorem for arbitrary graphs or an independent audit. No symmetry representation is computed.
