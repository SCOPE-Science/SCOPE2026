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
# Reproducibility and limits

Run `python3 verify_hexagon.py` in the same directory. The source uses only the Python standard library and reconstructs graphs from exact finite edge lists. For each case it checks connectivity, graph girth, enumeration and pairwise edge-disjointness of **all** simple six-cycles, all Rips simplices at graph distance at most two, and equality of the noncentered faces with exactly two alternating triangles for every six-cycle.

For the centered subcomplex it performs each proposed elementary simplicial collapse and checks that the smaller face has exactly one remaining strict coface at deletion. Its final residue must equal the original graph. A separately assembled mod-two boundary calculation then verifies complete reduced Betti numbers, including all higher dimensions present in the finite example. Each check runs afresh on the package code and prints `VERIFY_OK` on success.

The nine evaluated examples include two hexagons sharing one vertex, two bridged hexagons, hexagon–heptagon and hexagon–octagon joins, and noncactus theta graphs. Two examples with no six-cycles test only the zero-hexagon boundary of applicability. A further theta graph with three overlapping hexagons checks that noncentered tetrahedra can appear when the edge-disjointness assumption fails. These examples are finite and cannot establish a claim for arbitrarily large graphs; the proof of the universal theorem is in `RESULT.md`. Integral torsion-freeness and the exact circle-plus-sphere homotopy type rely on that all-graph CW argument, not merely on mod-two computations. The independent audit status above is intentionally unperformed.
