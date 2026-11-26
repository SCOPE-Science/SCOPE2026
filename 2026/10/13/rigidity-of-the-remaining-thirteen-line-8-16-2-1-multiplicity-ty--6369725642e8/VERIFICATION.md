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

Coverage with pencil sizes 4+4+5=13 forces disjoint pencils and forbids a center-joining arrangement line. Every triple point uses one line from each pencil, so the 16 distinct intersections of the first two pencils must all be covered by the third. If the centers were collinear, put them at infinity; the third parallel pencil would cover a 4-by-4 grid with at most five values of x−λy. A real-linear projection injective on the two summand sets gives at least 4+4−1 distinct sum values (walk through the ordered first set with the least second element, then through the ordered second set with the greatest first element). This contradicts five. For triangular coordinates the quotients B/A lie in C. Each third-pencil line has one center plus eight off-center crossings counted with multiplicity, reduced by one per triple, so its singular-point count is 9−t(c). The six-point bound gives t(c)≥3 and forces quotient support exactly C of size five, with frequencies 4,3,3,3,3. The finite stabilizer of B/A has order dividing five; Kneser's theorem rules out order one since four plus four minus one is seven. Hence the stabilizer is μ₅ and both coordinate sets are four-element subsets of μ₅ cosets. Scale the missing element in each coset to one; their ratios are then μ₅. For this normal form the 16 grid points are triples; the remaining off-center incidences are 8 doubles (one on each first/second pencil line), and the pencil centers have counts 4,4,5. The linewise counts are 6 on the first eight lines, and 5,6,6,6,6 on the third pencil. Dimca–Pokora's exact propositions provide both linewise hypotheses for the lower-r member of the counterexample pair. They transfer by lattice isomorphism, so projective equivalence contradicts the required difference in r (and in ν).

## originality

PASS

The open numerical case, linewise constraints and monomial/triangular arrangement framework are prior. The distinct claim is projective uniqueness for every complex realization satisfying the two constraints, and thus exclusion of the numerical type from the cited generalized-Terao counterexample regime. The strongest checked triangular theorem gives a same-combinatorics roots-of-unity representative, not uniqueness; its noncomplete-triangle theorem concerns classical freeness, not equality of ν or r. Searches and comparisons are bounded.

## value

PASS

This is a complete projective classification on a numerical type explicitly left open by a generalized-Terao reduction, and it rules out that type regardless of which admissible lattice is considered. The connection between saturated triple grids and multiplicative small-set structure explains why the moduli collapse rather than merely supplying an example. The incidence constraints are derived in the target application, not arbitrary parameters chosen after observing uniqueness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
