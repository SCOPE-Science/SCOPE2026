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
# Verification

The bundled `verify_clebsch_independence.py` uses only the Python standard library and rebuilds all finite data from the defining graph.

It checks the following exact statements:

- the vertex model has 16 vertices, 40 edges, degree 5, and strongly regular parameters \((16,5,0,2)\);
- exhaustive enumeration of all \(2^{16}\) subsets produces 392 nonempty independent faces with face vector \((16,80,160,120,16)\);
- the stated repeated-toggle rule produces exactly 191 matched Hasse covers and leaves one critical 0-simplex and nine critical 3-simplices;
- the complete face poset has 1200 Hasse covers, and a topological sort of the full Morse-oriented Hasse graph visits all 392 faces, proving acyclicity;
- a separately constructed mod-2 simplicial chain complex has boundary ranks \((15,65,95,16)\), giving unreduced Betti vector \((1,0,0,9,0)\) and reduced Euler characteristic \(-9\).

The homotopy conclusion uses standard discrete Morse theory: an acyclic face-poset matching with exactly one critical 0-cell and nine critical 3-cells yields a CW complex with those cells. Since no positive-dimensional cells occur below dimension 3, all 3-cell attaching maps land in the single 0-cell, giving \(\bigvee^9S^3\).

The verification is exhaustive for the stated finite graph. It is not evidence for any higher folded cube, and it has not received an independent audit. A successful run ends with `ACYCLIC_MATCHING_OK` and `VERIFY_OK`.
