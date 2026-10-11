---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For \(v\) in part \(V_i\), the closed-neighborhood sum is exactly \(w-s_i+f(v)\), so the part constraints reduce to the single worst label \(\mu_i\) and are equivalent to \(w-s_i+\mu_i\ge1\). For fixed total weight \(w\), the three disjoint local cases are: a part containing \(-1\), which requires \(s_i\le w-2\); a part with no \(-1\) but at least one zero, which requires \(s_i\le w-1\); and the all-\(+1\) part, which requires \(n_i\le w\). These are exactly the three truncated generating-polynomial terms in the package, and coefficient extraction enforces the global total weight. The lower summation limit is also proved: if \(w\le0\), no part can be all \(+1\), hence \(s_i\le w-1\) for every part and summing contradicts \(r\ge2\). A fresh independent brute-force replay over all 23 nondecreasing multipartite profiles of orders two through six matched the literal definition and structural criterion; the unbounded theorem rests on the symbolic argument, not that finite replay.

## originality

PASS

Liang's full primary paper determines the signed, signed-total, and minus domination numbers of complete multipartite graphs and uses the same neighborhood identity, but it optimizes only the minimum weight. Current Resultary searches for minus domination, complete multipartite graphs, weight enumerators, polynomials, and all feasible functions returned the assigned record as the exact hit and no independent all-function census. The prior scalar minimum therefore does not imply the coefficient sequence: many distinct feasible-label distributions can share the same least weight. The audited contribution is the complete partwise feasibility classification and coefficient formula.

## value

PASS

The weight distribution of every feasible minus-dominating labeling is a natural refinement of the established minimum parameter: it simultaneously supplies all coefficient counts and specializes back to the known optimum. On complete multipartite graphs the criterion compresses each part to two local statistics, yielding a reusable exact generating-function description rather than a table of small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
