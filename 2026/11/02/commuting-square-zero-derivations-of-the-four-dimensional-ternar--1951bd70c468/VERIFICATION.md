---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Determinant differentiation gives derivations D+D^T=tr(D)I; tracing forces tr(D)=0 in odd characteristic, hence so4. The determinant-one quadratic space is split, so so4=sl2⊕sl2 via A⊗I+I⊗B. With A²=aI,B²=bI, D²=(a+b)I+2A⊗B; partial traces force a+b=0 and A⊗B=0, so nonzero square-zero D lies in one pure nilpotent sl2 ideal and has rank 2. In each ideal, nonzero commuting nilpotents share a projective conic line (q+1 choices). For support size s, counting monochromatic 2(q+1)(q-1)^s and mixed (2^s-2)(q+1)²(q-1)^s assignments gives all coefficients and total. Each fixed ideal allocation gives an irreducible product of nilpotent-line cones, dimensions m+1 (two pure) and m+2 (others), no containment. Independently enumerated all 3^6 skew 4x4 matrices: 17 square-zero and 193 commuting ordered pairs, agreeing with q=3 m=2. Characteristic 2 and nonreduced schemes are excluded.

## originality

PASS

The canonical metric 3-Lie algebra, so4 splitting and sl2 nilpotent cone are classical. Fulman–Guralnick 2018 enumerate commuting pairs for general linear, unitary and symplectic Lie algebras; their full primary text explicitly says the orthogonal case is not worked out, and it does not impose endomorphism square-zero in every coordinate. General nilpotent commuting varieties can cover parts of geometric structure, but not directly this all-arity rank-refined square-zero count in the specific ternary derivation algebra. Historical priority against an orthogonal commuting-nilpotent tuple classification remains qualified.

## value

PASS

The all-arity joint-rank polynomial and explicit non-equidimensional 2^m irreducible-component census are natural structural invariants of a classical ternary Lie algebra; they identify how the commuting and square-zero constraints interact in two simple ideals. This is more than reproducing known so4 decomposition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
