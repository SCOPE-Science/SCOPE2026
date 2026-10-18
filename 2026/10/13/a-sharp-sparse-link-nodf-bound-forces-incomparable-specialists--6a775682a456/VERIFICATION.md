---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

With 3 rows, n positive columns and n+2 links, sum_j(deg column_j -1)=2. Hence either one degree-3 column, with P<=n-1+5/2<2n-2 for n>=4, or two degree-2 columns. If their common rows number one, column contribution <=2(n-2) and row contribution <=2, with equality iff all singleton columns hit common row; if identical degree-2 column neighbors, third-row no-isolate forces at least one disjoint singleton column, so P<=2n-5. This proves unique maximizer, labeled 3n(n-1), and Ferrers P=n+1. Independently generated all no-isolate 3xn matrices with n+2 links at n=4,5,6 and computed exact rational overlap sums: 522,2595,11673 admissible and maxima P=6,8,10 with labeled optimum counts 36,60,90. The infinite n theorem follows from the exhaustive structural degree-excess argument.

## originality

PASS

Classical NODF and its fixed-link numerical maximization are established. The primary metric analyses characterize complete/empty nestedness; Song et al. normalize using estimated fixed-connectance maxima rather than giving this closed sparse 3xn value and equality. Unrestricted-link Ferrers extremizers do not dominate the fixed-link constraint, which changes the optimizer to non-Ferrers. No matching NODF 3xn E=n+2 analytic census found in the Resultary semantic search.

## value

PASS

Exact sharp and unique optimizer of a common ecological nestedness metric under the minimally connected fixed-link regime, plus quantitative strict suboptimality of every Ferrers network. It isolates a meaningful mechanism behind non-nested optimal sparse structures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
