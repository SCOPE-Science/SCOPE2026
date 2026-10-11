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

Two ordinary Python 3 programs are included as standalone sources. Run `python3 verify_wagner_morse.py` and `python3 verify_wagner_homology.py` in this directory; no additional libraries or external data files are required.

The primary discrete-Morse program enumerates every legal matching simplex in five complexes and verifies the exact face vectors \((12,42,44,7)\), \((11,35,33,5)\), \((7,11,2)\), \((11,35,33,4)\), and \((7,11,3)\). It checks 49, 40, 8, 39, and 9 disjoint upper/lower face pairs respectively; it then orients *every nonempty-face Hasse cover* and requires that topological sorting reaches all 105, 84, 20, 83, and 21 faces. Directed cover counts are 244, 189, 28, 185, and 31. It verifies the critical-cell profiles, the two graph-edge orbits under translations/reflections, and ends `VERIFY_OK` only after all assertions.

The independent homology program generates the graph from cyclic vertex distance, enumerates compatible combinations of edges, computes signed simplicial boundary maps, performs exact Gaussian elimination modulo \(2\), \(3\), \(5\), and \(101\), and checks the reduced homology ranks. Both programs executed successfully. The finite-field agreement is an independent combinatorial cross-check, not a proof of torsion-freeness or of integral homotopy type. Those latter conclusions follow from the primary verifier's finite exhaustive acyclic matching, Forman's CW reduction, and the explicit null-homotopy argument. The proof makes no claim about graphs beyond those specified.
