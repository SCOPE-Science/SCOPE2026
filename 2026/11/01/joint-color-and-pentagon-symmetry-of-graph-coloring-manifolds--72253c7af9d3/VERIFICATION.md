---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Schultz's Stiefel description identifies Hom(C5,Kn) with the unit tangent sphere bundle V_{n−1,2}, dimension 2n−5, so Gysin with tangent Euler class gives precisely the parity-dependent rational degrees. A D5 reflection induces (u,v)→(u,−v) in the known one-reflection model: it fixes base, has degree (−1)^(n−2) on fiber and top, while 5-fold rotations cannot act nontrivially on a one-dimensional rational line. An explicit maximal cell of color placements with colors 0,1 in pentagon positions 0 and 2 is fixed by the color transposition with two simplex reversals, so its manifold orientation sign is +1; conjugacy and generation show all S_n preserve orientation. The natural coordinate projection to the boundary of the n-color simplex is S_n-equivariant, and the Schultz regular neighborhood of the diagonal plus vanishing rational Euler class for odd n makes its pullback nonzero on H^{n−2}; the simplex boundary top class has color sign. Poincare duality transfers this sign to H_{n−3}. External tensor products and rational finite-group transfer give quotient invariants. I independently checked the explicit top cell at n=5 with two orientation reversals; inspected the source exact cell-Lefschetz algorithm testing n=4,5,6 and the cited primary Stiefel input. No full D5-equivariant homeomorphism is asserted.

## originality

PASS

Kozlov's ordinary cohomology, Schultz's full Stiefel identification and one-reflection model, and the 2014 one-reflection-equivariant refinement are prior theorems used as inputs. Their statement level does not give the combined D5×S_n color-sign characters or joint quotient parity. The 2014 article's dihedral-equivariant homeomorphism question is stronger, not resolved here; a rational representation can be computed without settling it.

## value

PASS

The pentagon coloring manifold is a classical natural Hom complex whose simultaneous position/color relabelings encode unlabelled colorings. The nontrivial target sign sectors and clean odd/even rational quotient boundary provide an exact intrinsic equivariant invariant not visible from the previously known Stiefel homotopy type or a single reflection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
