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

Run `python3 verify_grid_d4.py` in the same directory as this document. The program uses only Python 3 standard-library modules. It must finish with `VERIFY_OK`; its own assertions reconstruct and check: 24 grid edges; 276 independent triples/facets; 64,900 augmented faces; 32,432 distinct face-poset matching pairs; 36 remaining ten-faces; 516,080 codimension-one Hasse incidences; an acyclic orientation after reversing matched incidences; all eight group-element reduced signed Lefschetz traces; multiplicities of the five rational dihedral irreducible characters; and identical characters on the 36 unordered pairs of unit-square cells.

In the matching calculation the empty simplex is paired, so unpairing its incident vertex gives an ordinary acyclic matching with one critical vertex and the 36 critical ten-faces. This supplies an actual homotopy argument via the standard discrete-Morse theorem. The sign convention for fixed simplices includes the empty face, and the rational module comparison uses the ordinary characteristic-zero semisimple character theorem. Exact homotopy does **not** establish a canonical correspondence between homology generators and pairs of square cells; no integral equivariant isomorphism is claimed. All checks apply to this exact sixteen-vertex grid only. No independent audit has been performed.
