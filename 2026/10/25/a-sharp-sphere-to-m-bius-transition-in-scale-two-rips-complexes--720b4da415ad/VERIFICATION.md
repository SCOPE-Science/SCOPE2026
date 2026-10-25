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

# Reproducible checks

Run `python3 verify_mobius_rips.py` from the directory containing this file, using Python 3 with no third-party dependencies. The program independently reconstructs graph distances by breadth-first search, enumerates all simplices as cliques of the graph square, verifies facet classification, checks every proposed codimension-one free-face deletion, and checks equality with the claimed Möbius-band triangulation. It tests every integer \(6\le n\le30\), including the minimal stable case. The assertions check that the residual 1-dimensional boundary is exactly the original Hamiltonian rim.

For \(n=5\), the program deterministically generates a 36-pair collapse and independently checks the resulting 10-vertex triangulated two-sphere using connected vertex links, edge incidences, Euler characteristic and global connectedness. For \(n=3,4\), direct face enumeration checks that the Rips complex is a full simplex.

The parameter-independent proof of the stable case is the modular seven-neighbor clique classification, the four all-parameter local free-face phases, and the explicit surface and spanning-tree homology arguments in `RESULT.md`. Finite replay alone is not claimed as a proof for arbitrarily large parameters. No claims are checked about radii greater than two or continuous edge interiors. Independent scientific validation has not been performed.
