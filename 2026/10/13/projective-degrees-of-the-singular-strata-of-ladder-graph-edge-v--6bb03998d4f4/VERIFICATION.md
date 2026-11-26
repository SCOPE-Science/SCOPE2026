---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The m square binomials give the ladder edge ideal. Independently, reduce monomials by u_i w_i=v_{i-1}v_i so that no monomial uses both rails of one square. Substituting w_i=v_{i-1}v_i/u_i sends distinct reduced monomials to distinct Laurent monomials: each u_i exponent recovers the rail pair and then the v exponents recover the remaining rung factors. The rung and top-rail edge monomials are algebraically independent by leaf elimination on their spanning tree. This verifies the prime complete intersection and projective dimension 2m. In a Jacobian dependence each participating nonzero row has both rails zero by its private rail columns; its equation and nonzero row force exactly one nonzero rung and a single supported column. Cancellation then requires an adjacent pair supported in the same rung column. The remaining case is a zero row, where each neighbor has one vanishing rail. Thus the maximal pieces are precisely the row-zero loci after the neighbor rail choices and the adjacent-row loci. Their residual square equations lie in disjoint smaller ladder blocks with independent free variables; each list member is irreducible and has its full complementary coordinate support (all ones there is a point). The ambient codimension is always m+3; there are four end-row pieces and m-1 adjacent-row pieces of degree 2^(m-2), and 4(m-2) interior-row pieces of degree 2^(m-3), by complete-intersection degrees. Independent analytic elimination solves the other equations using unit rails, or in the adjacent-row case first eliminates the shared rung using a unit rung. The only transverse equation is a rank-four quadric, up to a unit rescaling. A separate finite-field support and Jacobian replay for m=3,4,5 corroborated component counts 10,15,20 and degree totals 16,44,112; it is not used as the proof over C.

## originality

PASS

Credit the established ladder edge-ring complete intersection and the applicable general Hibi singularity theory. Indeed the same projective embedding is Hibi: use the lattice of ideals of the ordinal sum of m two-element antichains, with the rung coordinates the ends of successive diamonds and the two rails their incomparable elements. The Hibi straightening relations are exactly the square quadrics. Thus general Hibi criteria already cover qualitative singular support. The supported distinct contribution is the explicit degree profile for this family, requiring the exhaustive component calculation and the residual-chain degree count, not a first criterion for where toric singularities occur.

## value

PASS

The graph-edge embedding is canonical, so projective degree of its reduced singular support and the degree of each orbit-closure component are natural embedding-sensitive invariants. The calculation exhibits two different degree levels despite equal codimension and generic transverse type, and provides an exact whole-family answer rather than a single instance or an evaluation of smoothness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
