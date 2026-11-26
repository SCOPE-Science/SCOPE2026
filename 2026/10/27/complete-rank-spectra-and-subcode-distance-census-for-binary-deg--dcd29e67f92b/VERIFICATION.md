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

For mixed nonzero coefficients the exact root set is {0,a/b}, giving rank m-1; one nonzero coefficient gives an invertible map and the zero pair gives the zero map. Since m>=2 the coefficient representation is faithful. The two axes are complementary; counting their nonzero intersections with U gives the whole enumerator, including U=0. A linear subspace consisting of full-rank nonzero maps cannot mix nonzero elements of opposite axes (their sum is mixed). Thus its maximum dimension inside U is max(r,s), and every larger linear subcode has distance m-1. For fixed intersections R,S, the quotient U/(R+S) meets neither coordinate summand; it uniquely specifies a pair of t-dimensional projections and an isomorphism between them, and every such graph lifts uniquely by full preimage. This verifies feasibility, the Gaussian product (including t=0) and the partition of the Grassmannian. The two m-dimensional maximizers are A and B. In positive codimension containment of these is disjoint and each event has [m choose c]_2 witnesses by quotienting. For c<=m the required index exists; at c=1 the counts are 2(2^m-1) and (2^m-1)^2. Independent /workspace/branches/audit_binary_rank.py constructs maps by polynomial convolution and counts their image sizes, enumerates the subspace lattice by coset unions, then checks all 67 and 2825 subcodes for m=2,3, respectively, including all best-distance profiles and the codimension probabilities. The original proof, not the finite examples, supplies the universal claim.

## originality

PASS

The supported distinct result is the exact joint rank and best-subcode-distance census at all dimensions for arbitrary binary subcodes of this particular code, including an exact quantitative dimension-removal law. The parent profile, the parent rank distribution, the example of two hyperplane behaviors and the general two-summand graph count are not new. The inspected comparators do not already encode the arbitrary-subcode census for this rank metric.

## value

PASS

The precise unresolved quantitative question behind the prior preserving/lowering hyperplane example is how often the exceptional full-rank subcode survives, not whether both outcomes are possible. The binary two-coefficient case is natural because the mixed-coefficient rank stratum and two axes exhaust all maps. Identifying these strata in every subcode supplies a simultaneous distribution of a standard distance invariant and the full rank spectrum at every dimension, with exact survival even under several removals. The all-dimension census is useful independently of the elementary counting technique; no claim extends to larger alphabets or outputs with outside spaces added.

The dated certificate retains the supplied scientific assessment, sources and limitations.
