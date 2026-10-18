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

# Verification scope

The standalone `verify_hexagon_strong_morse.py` reconstructs exactly the 30 facets in two ways: all 720 orders of six vertices and the gap/root construction. It verifies their identical simplicial down-closures, checks exactly 163 augmented faces, computes mod-two simplicial boundary ranks `(11,37,30)`, and enumerates the signed oriented fixed faces for every element of the dihedral group.

The verified reduced mod-two Betti numbers are `(0,0,5,0)` in degrees zero through three. Exact ranks and Euler characteristic yield rational Betti rank five in degree two and zero elsewhere. The reduced Lefschetz numbers give the character; the finite-order property of the central half-turn gives the representation quotient.

The computational claim is finite and exhaustive. This is not a verification of arbitrary cycle lengths, integral equivariant lattices, or equivariant homotopy. It contains no external certification or independent review.
