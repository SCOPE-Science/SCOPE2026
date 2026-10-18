---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For P_s strong K_(1,m), s>=2,m>=3, the strong-product distance is max(path gap,star gap). The standard auxiliary graph linking selected vertices when path gap exceeds star gap has no odd cycle by the chord/sign-alternation argument, so is bipartite; each independent part injects into a GP set of the star of size at most m. A 2m-set forces each part to project onto the unique m-leaf maximum GP set; no centers, each leaf selected exactly twice. Analyze any triple in distinct occupied path layers: two nonadjacent gaps forbid all leaf assignments; a single gap=1 forces disjoint labels in the adjacent pair; both gaps=1 prohibit only threefold repetition, impossible under twice-per-leaf. Five layers force an obstructed triple, and 4-layer sets consist of two disjoint consecutive pairs. Counting support cases gives C(s,2)+(3^m-3)(s-2)+(2^m-2)(s-2)(s-3)+(2^m-2)^2 C(s-2,2). An independent BFS/geodesic brute force for representative (s,m) and leaf-position enumeration confirmed all four cases, with all arbitrary-parameter content supplied by the analytic structural argument. The known scalar gp=2m is credited to Vesel, not newly proved.

## originality

PASS

The new all-optima distribution uses equality rigidity of the star and geodesic configurations, not simply substituting H=star in gp(P_s strong H). However the uninspected full original might analyze equality beyond the abstract. Equivalent enumerator/top-coefficient claims were sought. Neither material accessed establishes all maximizing sets or four-layer classification; no inference from a scalar gp value alone yields M(s,m). Material priority limits are recorded separately.

## value

PASS

Determines *all* maximizing vertex subsets in a natural two-parameter strong-product graph family, not only the known maximum number: identifies center exclusion and a sharp four-layer support restriction, obtains the exact labeled count/top general-position-polynomial coefficient and its quadratic path-length growth. This is a useful complete equality classification in enumerative GP theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
