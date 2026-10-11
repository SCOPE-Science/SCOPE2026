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

# Reproducible verification

Run `python3 verify_cech.py` from the same directory using Python 3 with only standard-library modules. Successful execution terminates with `VERIFY_OK`.

The checker reconstructs the 12 ordered-pair vertices, all 18 edges, breadth-first-search distances, and maximal Čech facets at each integer \(r\in\{0,1,2,3,4,5,6\}\). It enumerates all faces under those facets and independently checks inclusion between consecutive scales. For each scale it builds a complete disjoint matching of face/coface pairs and tests the **entire directed Hasse graph** for acyclicity. This is a discrete-Morse certificate, not a randomized search or an assertion based only on matched-cell counts.

At scale four, signed gradient-path elimination reconstructs the integer Morse attaching matrix between 8 four-cells and 15 three-cells, checks its exact rational rank \(4\), and verifies determinant \(+1\) for rows \((0,1,2,4)\) and columns \((2,3,4,5)\), indexed from zero. A rational rank-four matrix with a unit maximal minor has four unit Smith factors and no torsion. At every scale, the checker independently computes all reduced mod-two Betti numbers from the raw simplicial boundary matrices. It also verifies that each new scale-two edge is homologous to an original two-edge path using an actual Čech triangle.

Finite checks are exhaustive for the named finite complex. The step from an acyclic matching to a CW homotopy model uses standard discrete-Morse theory; the final scale-four cell-attachment classification uses the Hurewicz isomorphism in degree three for a wedge of three-spheres. No external independent audit has been performed, and the checker does not certify novelty or mathematical results outside the stated graph and scale range.
