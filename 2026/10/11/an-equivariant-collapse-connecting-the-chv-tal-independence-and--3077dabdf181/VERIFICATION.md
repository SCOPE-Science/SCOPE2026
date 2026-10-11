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

# Reproducibility and verification

Run `python verify_morse.py`, `python verify_independent.py` and `python verify_equivariant.py` in a directory containing all three programs and `MORSE_CERTIFICATE.json`. All use only the Python standard library.

A third checker, `verify_equivariant.py`, enumerates all 126 faces of the independence complex and the 110 faces of the neighborhood complex, certifies that precisely eight free triangles each have a unique tetrahedral coface, verifies all sixteen deleted simplices, and checks that the eight dihedral automorphisms act transitively with equal trivial stabilizers on both simplices of each pair. Thus the inclusion is an equivariant simplicial collapse, not merely a homology isomorphism.

The first checker independently reconstructs all nonempty faces and confirms the exact stored face masks and 54 matched cover pairs, with two critical masks `1` and `672`. Directed Hasse edges number 264 and a topological sort exhausts all 110 faces. Forman's acyclic-matching theorem then provides the claimed integral sphere homotopy type.

The second checker reconstructs the complex from a separate neighbor list and verifies all four face counts and the modular simplicial boundary ranks `11,31,12` for primes `2,3,5,101`. It uses an exhaustive graph-coloring search, not a numerical estimate, to certify non-three-colorability and the explicit four-coloring. It independently enumerates all adjacency-preserving graph permutations, finds exactly eight, and calculates signed traces for every automorphism; the generating degrees are `-1,-1`.

The finite calculations exhaust this particular twelve-vertex graph. The modular homology ranks alone would not prove its integral homotopy type or the equivariant character; the separate acyclic Morse certificate and the integer signed fixed-simplex calculation establish those stronger claims. No independent external audit is asserted.
