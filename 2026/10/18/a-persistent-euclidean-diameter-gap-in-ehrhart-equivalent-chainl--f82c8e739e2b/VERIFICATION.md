---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

From the actual nine section halfspaces, independently reconstructed symbolic intersections of every nonparallel pair for both t=2m and t=4m+3. The two lists have exactly six feasible vertices for all m>=3: a violating affine residual stays strictly positive on the entire ray for every excluded candidate. All 15 vertex-pair squared distances in each section are bounded above by claimed polynomial using nonnegative coefficients after m=u+3, and witness pairs attain them. Independent SymPy symbolic check, not a bounded numerical sample, passed. The quoted Theorem 4.8 supplies Ehrhart equivalence, not the metric assertion; the positive limit follows by rationalization.

## originality

PASS

Chainlink complementary-section Ehrhart equality is explicitly prior theorem, and m=2 boundary example is in that source. The exact pair of Euclidean diameter polynomials for all m>=3 and strictly positive constant asymptotic separation are not supplied by equal Ehrhart data or the distinct Euclidean inradius of the full body. Novelty refers only to this geometric witness, not to the preexisting lattice equivalence.

## value

PASS

The construction takes a naturally motivated published family of Ehrhart-equivalent but geometrically different complementary sections and determines an exact metric invariant in every dimension parameter, including a nonzero unscaled limiting discrepancy. The strict persistent diameter gap is a concrete quantitative witness that lattice-point identity hides Euclidean shape, meaningful for comparing metric and enumerative invariants. Does not claim a general classification of all chainlink sections.

The dated certificate retains the supplied scientific assessment, sources and limitations.
