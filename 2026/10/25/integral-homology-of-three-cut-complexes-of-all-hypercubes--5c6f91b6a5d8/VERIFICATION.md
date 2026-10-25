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
# Verification details

Run `python VERIFY.py` in the extracted package with Python 3.9+ and SymPy installed. The file generates its graph and simplices from first principles rather than loading cached data. It checks the characterization of path triangles and square tetrahedra, the face counts, the signed chain identities, and the exact Smith invariant factors of the matrices in dimensions three and four. These are exact integer calculations, not numerical floating-point approximations.

For \(d=3\) the counts of vertices, edges, triangles, tetrahedra are \((8,28,24,6)\), the boundary ranks are \((7,17,6)\), and the dual homology ranks are \((4,1)\) in dimensions one and two. For \(d=4\) the counts are \((16,120,96,24)\), the boundary ranks are \((15,65,24)\), and the dual homology ranks are \((40,7)\). All nonzero Smith invariant factors of these boundaries are units. At \(d=5\), the exact counts are \((32,496,320,80)\) and the second-boundary rank modulo two is \(209\); this is a finite consistency test only.

The global claim for every \(d\ge3\) is proved without extrapolating these computations. It rests on the cubical square characterization, unique-square property of every path triangle, square-based simple connectivity, and combinatorial Alexander duality. No external validation has been performed.
