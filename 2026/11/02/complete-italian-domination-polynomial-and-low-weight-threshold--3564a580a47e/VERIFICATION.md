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

The neighborhood guard is exactly x_i=0 => Y-y_i>=2 and y_i=0 => X-x_i>=2 with X,Y side sums. Partition (X,Y) into both >=4 (H_n²), exactly one <=3 (2∑z^a T(B_a)), both <=3 (X,Y in {2,3}). In low-low, c22=n+binom(n,2), c23=n²(n−1) per orientation, c33=binom(n,3)²+n(n−1)²(n−2)+n²(n−1); disjoint supports yield displayed polynomial. All weights >=4, coefficient at z4 is c22 plus two all-one-side configurations only for n=4. I independently enumerated all 3^(2n) labeled assignments for n=4,5,6, totaling 597051 assignments, and checked every coefficient against an independently coded polynomial; this finite validation is distinct from general side-total proof.

## originality

PASS

The n=3 cycle C6 is known and excluded. Complete multipartite Roman-{2} weight enumerators do not cover crown graphs (nonadjacency between matched pair vertices is not transitive); perfect Roman crown functions obey a stronger constraint and cannot supply all Italian functions. Shao–Zhao study paths, trees and cycles, not this full crown polynomial. No dominating prior result found from real database and primary comparisons; historical priority still conditional.

## value

PASS

The deleted matching creates coupled pair-support restrictions absent in complete multipartite enumerators. The complete all-degree polynomial and exceptional n=4 minimum multiplicity form a natural exact classification of a classical regular bipartite graph family, not a routine isolated domination-number calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
