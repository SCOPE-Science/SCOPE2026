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

# Verification of the pentagonal-wheel strong Morse classification

Run `python3 verify.py` with `collapse_pairs.json` in the same directory. Only the Python standard library is required. The code rebuilds the ten-edge unfilled wheel graph (hub 0, rim 1 through 5) rather than reading a precomputed face list.

The verifier independently derives each of the 720 strong matching generators from the vertex-order construction in two implementations, then checks 81 distinct generators, 45 maximal facets, 20 vertices, 55 edges, and 20 triangles in the derived complex. It uses the standalone certificate to check twenty sequential simplicial free-face collapses, and traverses the 20-vertex, 35-edge graph spine to confirm connectedness and cycle rank sixteen. It compares the certificate to a separately recomputed lexicographic collapse list.

For every one of the ten dihedral automorphisms it checks that the enumerated complex is invariant, computes the exact signed simplicial-chain traces, uses the Lefschetz identity to obtain the homology trace, and checks agreement with four copies of reflection sign plus three copies of the rational five-point augmentation module. The full trace vector by conjugacy type is \((16,1,-4)\). The method is finite and exhaustive, with no probabilistic steps. An independent mathematical audit has not been performed; the checker does not establish any classification for other wheel sizes or an integral lattice splitting.
