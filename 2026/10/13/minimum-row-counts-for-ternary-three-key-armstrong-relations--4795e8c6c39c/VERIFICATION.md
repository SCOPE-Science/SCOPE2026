---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

A table with all minimal keys the 3-sets has each distinct row pair agreeing on at most two coordinates, and every coordinate pair is exactly the agreement set of a row pair. Thus C(m,2)>=C(n,2), m>=n. At diagonal m=n, all row pairs have exactly two agreements and are bijective witnesses for the column pairs. Encoding each column by its canonical partition of m rows into <=3 values gives a mask on row pairs. Pairwise column-mask intersections must have size exactly one, and no row-pair edge lies in three masks. Exhaustive increasing-index DFS on all canonical ternary partitions for m=3,5,6 (respectively 4,40,121 possibilities) finds no m-column family; independently written direct DFS reproduces zero terminal solutions with nonidentical search-node counts. Explicit displayed 4x4, 6x5 and 7x7 row witnesses and the 3- and 6-column projections pass all exact agreement tests. The previously proved upper length f(3,3)=7 handles n>=8. Therefore minima n=3..7 are [4,4,6,7,7]. Unlike a partial search, the canonical partition enumeration and coverage of every diagonal candidate are mathematically justified.

## originality

PASS

Chee–Zhang–Zhang prove the maximum admissible ternary attribute length seven and exhibit a seven-row seven-column Armstrong code. Katona–Sali–Schewe give general coding/bounded domain lower bounds and m>=n, while older Beeri–Dowd–Fagin–Statman treat general Armstrong relation sizes. The candidate’s strict diagonal impossibility at n=5,6 and complete minimum-row function [4,4,6,7,7] are absent from the inspected principal papers. These finite exact naturally parameterized minima are not known-table repetition: n=5,6 require exhaustive partition obstructions. Residual priority risk from specialized unindexed conference appendices or orthogonal double cover enumerations.

## value

PASS

Minimum row count for a small-domain table realizing every 3-column minimal key is a canonical exact database-design/coding-theory invariant, not an arbitrary slice. The strict n=5 and6 gaps provide genuinely new finite feasibility boundaries beyond the m>=n general lower bound, and the full profile through maximal n=7 is complete with explicit constructions and exhaustive obstructions. This is useful independently as a benchmark for bounded-domain Armstrong code constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
