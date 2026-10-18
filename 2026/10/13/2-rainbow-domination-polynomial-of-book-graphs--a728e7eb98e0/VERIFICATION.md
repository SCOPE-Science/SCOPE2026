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

For every n>=1, fix the two spine labels and count the n independent pages. When a spine label is empty, its missing-colour condition is imposed by inclusion-exclusion. The five exhaustive spine-label types yield precisely A0^n - 4(1+x)A1^n + 6x^(2n) + 4x B1^n + 6x^2 B2^n + 4x^3 B3^n + x^4(1+x)^(4n). An independent literal-label enumeration confirmed all coefficients for n=1..4, with minimum pairs (2,4),(3,4),(4,5),(4,1). For n>=4, other contributions have degree >=5 and x^4 (1+x)^(4n) gives unique degree-4 term. The finite enumerations corroborate but do not establish all n; the spine-case proof does.

## originality

PASS

The existing rainbow/prism bijection transforms the claim into the ordinary domination polynomial of K_{1,n} square C_4. The full published complete-multipartite two-rainbow enumerator does not cover B_n for n>=2: nonadjacent vertices a1 and a2 on different pages have different neighborhoods {s,b1} and {s,b2}, unlike any nonadjacent pair in a complete multipartite graph. Inspected foundational sources give minima/definitions, not every coefficient on this graph family; no checked broader theorem directly implies the all-n expression. An older unindexed prism-domination enumerator remains possible.

## value

PASS

Counting all rainbow dominating functions of square book graphs by weight is a natural finer enumerative invariant than their minimum domination number. The common-spine interaction yields a seven-term exact all-order polynomial and sharp low-weight transition at four pages. Researchers can use the full polynomial or equivalent K1,n square C4 domination polynomial independently of any global classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
