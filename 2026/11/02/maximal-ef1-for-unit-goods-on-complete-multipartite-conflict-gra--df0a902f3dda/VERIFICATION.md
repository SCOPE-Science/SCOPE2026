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

A nonempty feasible bundle occupies one part; if goods remain, maximality requires every bundle to be nonempty and every used part to be completely colored. Unit EF1 is exactly a class-size spread of at most one. If m≤n, singleton assignment is complete; if the largest part has at least n items, dividing that entire part evenly works. Otherwise choose the first prefix that reaches n, with previous sum B<n and last part size t≤a1. The sum of lower class quotas is B−Σ_{before last}⌊a_i/2⌋+⌈t/2⌉≤B+1≤n, while the upper quotas sum to at least n. Integer quotas totaling n therefore exist and each used part splits into exactly that many singletons and pairs. B+t≤2n−2; at m=n the bound also holds under a1<n (thus n≥2). The claimed time is valid by scanning explicit part lists, sorting r sizes, and writing the bundles. In K_{3,3,3}, a complete equitable split among four classes requires sizes 3,2,2,2, but each three-item part would need a class of size three. Two split parts do give a maximal partial coloring. Independent bounded replay checked 9,570 graph/agent instances via a direct search for pair quotas, including unsorted part lists and n=1.

## originality

PASS

The exact notion is prior; the evidence supports the extension to all complete multipartite graphs in the additional agent range, not priority for EF1 or equitable coloring. A distinct later-dated catalogue record materially matches existence, time and the prefix pair/singleton construction. It is equivalent coverage of those results, but no evidence places it before the frozen result. The checked earlier statements cover trees, stronger valuation assumptions at three agents, or conditions for complete allocation, not the arbitrary-part unit-good case with four or more agents.

## value

PASS

The result solves the maximal equitable partial coloring problem for a natural unrestricted family beyond trees and includes cases where complete equity is impossible. It yields an explicit efficient construction and a bound on the number of colored goods in a nontrivial regime. The motivating four-agent K_{3,3,3} case separates the task from a mere application of a complete coloring theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
