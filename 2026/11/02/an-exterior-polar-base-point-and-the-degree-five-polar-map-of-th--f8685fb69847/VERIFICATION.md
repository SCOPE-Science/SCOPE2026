---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Over algebraically closed characteristic zero or odd characteristic, take the primitive integral F=e3−s*e2 in P4. Direct differentiation gives all polar quadrics q_i=x_i²−s². At a projective base point s!=0 and normalized s=1, each xi is ±1; the normalization sum=1 forces exactly three plus signs normally (10 points), plus the all-minus class only in characteristic 3 (11 points). Hessian 2(D−J) at these projective points has rank 4, proving reducedness; the 10 3-plus nodes lie on F and are ordinary, but at the extra P=[1:1:1:1:1], F(P)=−40 ≡2 mod3, so the extra base point lies outside X. Hessian at a=[1:1:1:1:-4] has integer determinant −128, nonzero in odd characteristic and making the gradient map dominant generically separable. A general intersection of four degree-2 polars has 2^4=16 points counted with multiplicity; 10 or 11 simple base points contribute 1 each; generic fiber hence degree 6 ordinarily, degree 5 in char3. Excludes char2 and Gauss map. Independent symbolic gradient/Hessian plus finite fields p=3,5,7 independently reproduced 11/10/10 base points, not a proof over every field.

## originality

PASS

The integral normal form and ten nodes of the Segre cubic are classical; the characteristic-three exceptional exterior gradient base point of the primitive integral equation and the 6->5 generic polar-degree jump are not stated in inspected complex and nodal surveys. A 1936 article on polarities may hide analogous computation; full-text access failed so originality remains qualified.

## value

PASS

The Segre cubic is a canonical maximally nodal cubic threefold. Its specified primitive integral reduction in the characteristic dividing the degree provides a mathematically motivated sharp distinction between singular points of the hypersurface and base points of the ambient gradient map, with an exact polar-degree jump—a natural algebraic-geometric invariant, not a routine chart choice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
