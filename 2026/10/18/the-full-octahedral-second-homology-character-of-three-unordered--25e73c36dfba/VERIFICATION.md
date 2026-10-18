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

`verify.py` is a standalone deterministic Python program using no external packages. It creates the subdivided cube, all closed-disjoint cubical configuration cells and their oriented boundaries, then checks integrally that boundary squared is zero. It executes and certifies all 1,296 elementary top-dimensional free-face collapses, verifies connectivity and both mod-2 and mod-101 first boundary ranks, and constructs fundamental cycles for the six first-homology coordinates. The 48 cube automorphisms are enumerated as bit flips and coordinate permutations; their first-homology traces are computed via row reduction in characteristic 101 and independently compared with graph-cycle-plus-orientation traces. Signed cubical fixed-cell Lefschetz traces determine the full second-homology character and its ten character inner products.

The integral first-homology theorem for planar triconnected graphs is taken from Ko–Park (arXiv:1101.2648). It establishes torsion-freeness and rank six, and is not reproved by finite-field rank checks. Together with the complete 3/2 collapse and Euler characteristic it gives free integral second homology of rank seventeen.

The finite computation is exhaustive for this exact three-particle, once-subdivided cube model; it does not certify a general result for other graphs, larger particle counts or integral equivariant lattices. The external scientific comparison is literature-based, not an independence certificate.
