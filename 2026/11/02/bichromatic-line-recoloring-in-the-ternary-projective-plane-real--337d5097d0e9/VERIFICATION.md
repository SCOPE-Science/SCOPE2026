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

# Reproducible finite checks

Execute the two standalone programs from the same directory:

```
python3 verify_coloring_flip.py
python3 verify_quadrilateral_frames.py
```

The first enumerates all 8192 named binary point colorings of the 13-point plane using normalized ternary vectors, checks all thirteen line constraints, reconstructs all legal one-point moves and performs breadth-first searches from all 468 valid colorings and all 234 six-point classes. It separately checks the exact 13-step distance profile, girth, cubic degree, edge count, and disjointness quotient metrics.

The second uses an independent affine model with four points at infinity, verifies the projective-plane line axioms, enumerates the 234 projective line frames and all 8192 colorings, checks every point-recoloring transition, proves that the frame disjointness graph is connected and nonbipartite, and exhaustively enumerates invertible ternary 3-by-3 matrices modulo scalar to show the frame stabilizer (24 elements) is transitive on its three permitted recolorings. Its outputs include the success marker `PROJECTIVE_FRAME_STABILIZER_ARC_TRANSITIVITY_PASS`.

The theoretical identification with F234B/F468 uses the cited *complete* symmetric-cubic census, not finite statistics as an unsupported uniqueness proof. Exact checked domains are 8192 colorings, all 715 four-line choices, all 234 six-point frame classes, and the full 5616-element projective linear group. Both scripts use only Python's standard library, no downloads or randomized parameters.

Scientific limitation: no larger-order projective plane is treated. Originality limitation: the abstract graph F234B/F468 itself is long known and no external independent scholarly review of the new coloring interpretation is claimed.
