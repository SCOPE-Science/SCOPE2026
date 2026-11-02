---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

C: Every color-a class is a nonattacking partial matching. If it omits p−k rows and q−k columns, every missing-corner cell has no color-a neighbor and therefore must be occupied by the opposite independent color; thus (p−k)(q−k)<=1. For p<q this forces both colors to cover all rows. Ordered first injection (q)_p and inclusion-exclusion over same-row forbidden second placements gives the exact nonsquare monomial. On square n×n each color has n or n−1 cells and any n−1 missing corner must have opposite color; the (full,full),(full,partial),(partial,partial) cases produce the three derangement coefficients without overlap. Explicitly handle D0=1,D1=0, the small n2/n3 missing weights. Independent exhaustive ORIGINAL-definition enumeration of all ternary labels on 2x2,2x3,2x4,3x3,3x4 boards (up to 3^12 assignments) exactly reproduced coefficient dictionaries: (2,2){2:4,4:2}; (2,3){4:18}; (2,4){4:84}; (3,3){5:36,6:12}; (3,4){6:264}. Infinite p,q result rests on missing-corner lemma/inclusion-exclusion, not those finite checks.

## originality

PASS

O: Original 2017 2-rainbow independent domination work defines this precise coloring and its independent-set prism equivalence; later product-graph papers usually provide minimum weights for cycle products or general bounds, not a complete full-weight rook graph enumerator. Mertens 2024 calculates the ONE-COLOR ordinary domination polynomial of rook graphs, which counts different objects and does not directly imply the two-color independence/disjoint matching decomposition. Resultary search returned many rook graph invariants but not this three-term square count. A stronger maximal independent-set polynomial for K_p□K_q□K_2 could cover it; residual risk acknowledged.

## value

PASS

V: The all-weights enumerator of a standard Hamming/rook graph family is a motivated combinatorial classification beyond minimum domination, with a structural square-versus-rectangle phase boundary and exact labeled derangement counts. Such formulas can support invariant comparison and extremizer enumerations; they are not arbitrary small-instance counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
