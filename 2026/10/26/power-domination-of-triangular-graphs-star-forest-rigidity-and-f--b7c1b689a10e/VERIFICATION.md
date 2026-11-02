---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Under ordinary power domination in L(K_n), after the closed-neighborhood step precisely edges of K_U, where U is the isolated-vertex set of the selected K_n edges, remain unobserved. For |U|=2 a single forcing event completes; |U|>=3 leaves every observed edge with 0 or at least 2 unobserved neighbors, so no force. This proves iff |U|<=2. Inclusion-exclusion over exact isolated vertices proves complete polynomial; deleting a selected edge can create at most two new isolates, forcing the minimal sets to be an i=1 matching or i=2 star forest. Standard matching and exponential-formula enumerations give min/max and full minimal enumerators. Independent original graph monitoring closure, polynomial counts, minimal sets, maximal-failure counts verified for n=3..6 including 32768 selections at n=6; proof covers every n>=3.

## originality

PASS

Brimkov et al introduce general power-domination polynomials, not demonstrably the explicit Johnson J(n,2) family. The four-regular claw-free bound reaches this family only at n=4, and triangular-grid graphs are not Tri(n)=L(K_n). Published SCOPE book/spider power-domination polynomials treat different graphs. Best-of-knowledge new family structural formula and minimality classification, subject to inaccessible foundational full text.

## value

PASS

Complete placement criterion and all-size enumerators, minimal-set star-forest classification, exact extremal sizes, and maximal failures are mathematically natural parameters on the canonical highly symmetric Johnson graph J(n,2). They refine the minimum-size problem substantially.

The dated certificate retains the supplied scientific assessment, sources and limitations.
