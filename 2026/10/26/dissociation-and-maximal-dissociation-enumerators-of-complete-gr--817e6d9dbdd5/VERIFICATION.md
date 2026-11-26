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

Fix the selected old set A, leaving b omitted old vertices C. Subdivision vertices internal to A are forbidden. Each of the b-choose-2 subdivision vertices internal to C can independently be selected and each old vertex in A has a disjoint b-way pool from which to select at most one neighbor. This proves the weighted D summand including b=0. For b>0, maximality forces all internal C subdivisions and exactly one crossing neighbor per selected old vertex, giving a function f:A→C and size 2(n−b)+binom(b,2). No new subdivision can then be added; an omitted old vertex has b−1 selected neighbors from internal C edges, and any selected crossing subdivision to it would become degree two on its addition. Hence it is blocked iff b≥3 or it lies in the image of f. For b=1 the image is the only element since n≥3; for b=2, both omitted vertices must be hit, giving 2^(n−2)−2 mappings (zero at n=3); for b≥3 all functions work, including the empty function at b=n. At b=0 the all-old set is maximal. These are exactly the four summands. The strict discrete convexity of the size for b≥1 gives minimum 2n−3 at b=2,3 and possible maximum only at 1,n. Comparing with size n and using binom(n,2)>2n−2 for n≥5 proves both asserted uniqueness ranges and the gap. Direct substitution verifies M_3 and M_4.

## originality

PASS

Best-of-knowledge pass for the uniform labeled cardinality polynomials and maximality/extremal classification across complete subdivisions beyond the already covered cycle boundary. Same-host indexed results count different objects. The known complement equivalence with three-vertex-path covers is credited; the inspected published extremal results do not provide this family distribution.

## value

PASS

The full subdivision of a complete graph is the natural incidence graph of the complete two-uniform set system. The b-dependent extension test identifies precisely when local maximality forces an onto assignment and when the incidence structure alone blocks all omitted vertices. The exact size distribution and sharp unique extremal sets expose a quadratic disparity between locally maximal solutions; by complement they also quantify sizes of minimal three-vertex-path covers in this family. These are not implied by an optimum value or an order-based bound alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
