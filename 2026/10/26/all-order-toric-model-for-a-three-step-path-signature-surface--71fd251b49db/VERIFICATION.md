---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For j>0 the words 1^i 2^j 1^ell give all monomials b^j a^i c^ell with i+ell=k-j, up to nonzero constants; the only surviving pure first-axis coordinate is (a+c)^k up to normalization. In u=a+c,v=a,w=b the j-block is exactly w^j times the full degree-(k-j) binary-form space. Dehomogenizing by u^k on the parameter torus gives the characters (v/u)^q(w/u)^j and the full lattice-point set of P_k. The characters generate the full lattice (use (0,1),(1,1)), and the lattice polygon integer-decomposition property gives a normal homogeneous semigroup ring. Twice the area is k(k-1). In the character lattice the tangent cones at the origin and slanted vertex are unimodularly equivalent respectively to cones with rays (1,0),(1,k-1) and (1,0),(k-1,k). For a character cone with rays (1,0),(a,d), the exponent map (x,y) -> (dx-ay,y) identifies the chart with the invariant monomials of weights (1,a) mod d. This fixes the tangent-versus-normal sign convention and yields the two claimed quotient types; at (0,k) the primitive directions (0,-1),(1,-1) give determinant 1. Open positive-dimensional torus orbits are smooth. This is an all-k check, not a finite extrapolation; the bound VERIFICATION.md does not record prior independent or formal verification.

## originality

PASS

The supported distinct statement is the explicit all-k polygon and its invariants for this fixed shape at k>=4. The closest primary treatment gives the general coordinate parametrization and this shape's order-three toric surface, not the all-order linear conversion or its polygonal invariants. The frozen prior-work sentence overstates Proposition 3.9: its order-three case is restricted to at most two axes and its general order-two case to at most three axes, with an additional stated order-two family. This does not affect the present theorem or its distinction from prior work.

## value

PASS

The fixed natural repeated-axis shape is an established test case in the question about toricness of axis-path varieties. Rather than a new individual level, the complete lattice polygon supplies the projective normal model, the exact degree at every order and two uniform local singularity types. These are useful concrete invariants even without resolving the general axis-path question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
