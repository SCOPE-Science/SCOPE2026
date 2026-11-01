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

# Finite proof and checks
Run `python3 verify_dodeca_pmc.py` in a Python 3 environment. No third-party libraries are required. The verifier reconstructs the exact graph and its 36 perfect matchings; separately enumerates 111,376 ordinary matchings; verifies the 30,504 extendible matchings, including the empty matching; reproduces the 15,231 coordinate-toggle Morse pairs; and checks acyclicity on all 163,650 Hasse incidences. The exact signed Morse differential has 10 rows and 30 columns, with mod-two rank nine and a displayed maximal minor of determinant two. The integral Smith invariant factors are therefore nine copies of one and one copy of two, giving the claimed Moore summand.

The independent original-complex simplicial mod-two boundary ranks (degrees one to nine) are `(29,346,1833,3936,4416,3024,1296,324,36)`. The resulting mod-two Betti numbers are `1` in degree two and `21` in degree three, zero in every other positive degree. The original 30-vertex complex is high-dimensional, but this finite computation and the explicit acyclic matching produce a valid 3-dimensional CW model: the finite-level mod-two calculations are merely corroboration, not an infinite extrapolation. `boundary_certificate.json` contains the actual integer Morse differential in its exact row and column order. `verification_output.txt` contains the recorded stdout of the standalone checker.

The homotopy classification invokes the standard classification of three-cell attaching maps into a wedge of two-spheres by their degree vectors; the matrix's Smith form is used at the level of the simply-connected three-dimensional CW model. Limits: no general all-graph theorem, independent audit, or external certification is claimed.
