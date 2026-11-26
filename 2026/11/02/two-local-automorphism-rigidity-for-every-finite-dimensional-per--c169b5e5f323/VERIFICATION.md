---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The n natural-basis squares span E² because all cross products vanish, and perfection makes these n vectors a basis. Thus the coefficients in g(e_i)g(e_j)=0 force disjoint supports for the columns of every genuine automorphism g, which is monomial by invertibility. Interpolation at pairs of natural-basis elements shows the nonzero images T(e_i)=c_i e_{σ(i)} occupy distinct coordinates. For any x and i, the witness for (e_i,x) has exactly one entry in row σ(i), namely c_i in column i, so that row of T(x) is forced to be c_i x_i. This reconstructs the entire invertible linear map with no field-size hypothesis. The witnesses at (e_i,e_i²) give the diagonal product constraints, and disjoint image coordinates give all off-diagonal ones. Bilinearity completes multiplicativity; no polarization or division by 2 is used. The zero-dimensional case is automatic. Independent enumeration using full multiplication tables and all 256 set maps for each of the six invertible F₂ structure matrices of dimension two confirms the equality there (eight ordinary automorphisms counted across the six algebras).

## originality

PASS

The credited result is arbitrary-map two-point rigidity for all finite-dimensional perfect evolution algebras over all fields, not monomiality of ordinary automorphisms. The closest source supplying monomiality does not give the simultaneous coordinate and square interpolation argument that upgrades pointwise witnesses to one multiplicative map.

## value

PASS

Perfect evolution algebras form a natural class with constrained but potentially varied automorphism groups. It is useful to know that two simultaneous evaluations already rule out every nonlinear or nonglobal interpolant, uniformly including the smallest fields and characteristic two. This is a class-wide rigidity result, and the pair-of-squares mechanism identifies why the known monomial structure is enough in the algebraic action but not for arbitrary monomial groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
