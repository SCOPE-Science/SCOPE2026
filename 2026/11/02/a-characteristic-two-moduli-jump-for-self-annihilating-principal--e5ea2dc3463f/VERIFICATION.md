---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For A_d=k[x_1,...,x_d]/(x_i^2), d>=2, the squarefree basis and decomposition A_d=B⊕LB classify all linear-leading principal ideals. In char2 every f in maximal ideal squares to zero by Frobenius; after GL_d normalization, unit multiplication makes a unique generator L+g with g in m_B^2, and automorphism L↦L+g carries Ann(L)=(L) to Ann(L+g)=(L+g). Thus each initial projective line has affine fiber of dimension 2^(d-1)-d and total dimension 2^(d-1)-1. In odd char the degree-2 coefficients of f² force at most one nonzero linear coefficient, and writing f=x_i u+v gives v=0 by 2uv=0, hence exactly d coordinate ideals. For finite q counts are d (odd q) or q^(2^(d-1)-d)*(q^d-1)/(q-1) (even q). Independent complete F2,d=3 ideal enumeration from the multiplication table confirms 14 distinct self-annihilating ideals, each half-dimension. Proof handles arbitrary fields and all d>=2; these are DISTINCT ideals, not automorphism orbits.

## originality

PASS

The characteristic-two affine-fiber classification of self-paired exact-zero-divisor principal ideals and the uniform finite-field point count were not located in the searched exact-zero-divisor literature. Coordinate examples and Hilbert-function restrictions are prior results, explicitly excluded from novelty. Relevant older general exact-pair theorems may imply special cases; inaccessible full source is a residual risk rather than automatic failure.

## value

PASS

Natural Artinian monomial complete intersections show a genuine field-characteristic jump from d isolated coordinate ideals to an affine-space fibration over projective space with exponential-in-d fiber dimension. The complete all-field classification is useful to zero-divisor/ideal moduli studies rather than arbitrary finite tabulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
