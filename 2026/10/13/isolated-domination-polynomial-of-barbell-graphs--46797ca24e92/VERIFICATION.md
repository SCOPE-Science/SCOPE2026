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

Every dominating set must meet both cliques; conversely any such set dominates. An induced isolate requires a singleton side, with the unique bridge endpoint nonisolated only if the opposite bridge endpoint was also selected. Subtract sets with both sides of size>=2 and bridge-adjacent singleton cases from P_n(x)P_n(y): I=P(x)P(y)-Q(x)Q(y)-xy[(1+x)^(n-1)+(1+y)^(n-1)-1], P=(1+t)^n-1,Q=P-nt. Setting x=y and evaluating at 1 yields stated polynomial and totals. A minimal isolate dominating set cannot have >1 selected vertex on either side; exactly n^2-1 cross pairs excluding the bridge survive. Independent exhaustive subset checks for n=2..6 reproduced all bivariate coefficients and minima; this is corroboration of all-n combinatorial proof.

## originality

PASS

Best-of-knowledge PASS for all-cardinality and bivariate enumerators, not for lower isolate domination gamma0=2 already stated by Bhangale–Pawar. The earlier isolated-domination polynomial framework gives other named graphs, including a *bi-star tree*, not the two-clique bridge barbell. Resultary barbell zero-forcing polynomial is a different invariant.

## value

PASS

The barbell B_n is a natural dense-clique/one-bridge test family, and its all-set bivariate generating function distinguishes clique occupancy and yields both total counts and extremal minimal-set behavior. It goes beyond the known scalar domination number and is an exact reusable graph invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
