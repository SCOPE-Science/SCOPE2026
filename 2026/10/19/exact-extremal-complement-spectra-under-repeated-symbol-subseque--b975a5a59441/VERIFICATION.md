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

Read each output by scanning the unchanged ordered skeleton of non-a letters; the lengths in its successive slots, including the end slots, uniquely recover the deletions in every original positive a-run. This remains true even when several neighboring skeleton letters are identical or a whole run disappears. The exact polynomial is therefore the bounded-composition product. At fixed r≥1 the separator budget bounds the sum of run lengths by n-r+1; padding any run is coefficientwise monotone, and the constraints m≥r and m≥k are necessary and sufficient for the binary witness. A unit exchange x,y→x-1,y+1 for x≥y+2 increases the product of those two geometric sums by z^(y+1)+…+z^(x-1), and strictly decreases the sum of squared lengths, proving simultaneous dominance. For k=3 the types 1+1+1, 2+1 and 3 give B=C(r,3)+(r-1)min(r,d)+min(r,max(0,d-r)), d=n-2r+1. Writing r=R-h, R=floor((n+1)/2), d=2h or 2h+1, when d≤r the comparison with r=R follows from sum_{j=r}^{R-1} C(j,2)≥h C(r,2), for odd r≥4 and even r≥3 (the adjectives refer to the parity of n). For d>r and r≥5 this difference reaches at least r², the extra terms' upper bound; for r≤4 the small checks are decisive: r=4 with d>r forces R≥7 (odd n) or R≥6 (even n) and B≤20; r≤3 has B≤10, with even r=3 and d>r requiring R≥5, even r=2 giving B=1,3 at R=2,3 and B≤4 thereafter, and r=1 giving at most one. At odd n=3,5,7 direct evaluation gives 1,2,5. This verifies the global formula, achievable witnesses, coefficientwise comparison and all boundaries of the triple-deletion formula without relying on finite testing.

## originality

PASS

The supported distinct claim is the fixed-letter distinct-output extremum and triple-deletion evaluation, not the geometric-sum smoothing method in isolation. Closely related deletion-sphere extremal results concern deletions of arbitrary symbols and ordinary runs; they do not identify the collision-free fixed-letter statistic or optimize it under the budget for positive a-runs. The closest monochromatic fixed-composition catalogue comparison is later and does not state the global or k=3 optimization.

## value

PASS

This is a natural and complete special-pattern answer to a stated complement-factor question. The reduction from arbitrary words over any alphabet to balanced binary witnesses yields an exact computable maximum for every n,k, and simultaneous fixed-run domination is stronger than a bound at a selected deletion order. The explicit k=3 transition and parity laws also give sharp benchmarks for broader deletion-pattern bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
