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

For n>=2 the two-row ladder P2 square Pn admits local column states (a,b) in {0,1,2}^2. For triples (p,s,t), each zero entry of s must have its neighboring row and horizontal weights >=2. Let delta(s)=sum(s)-1 and the finite integer potential d(p,s) as explicitly tabulated in the frozen source. Exhaustive independent enumeration of all 9^3=729 triples found 666 feasible and verified delta(s)+d(p,s)-d(s,t)>=0 in every feasible case; exactly 161 zero-cost triples. Summing telescopes to weight>=n with nonnegative endpoints. The source fully enumerates 13 trimmed zero-cost pair-states and yields two starting row choices, with alternating excursions of uniquely recoverable lengths 1,2,5 and a terminal opposite-column state. The corresponding exact generating function is 2*z^2/(1-z-z^2-z^5), with gamma_I=n and a2..a5=2,2,4,6. Independent exhaustive vertex-label checks for n=2..5 verify minima and counts; the unrestricted all-n statement depends on the complete local certificate/finite transition classification, not on extrapolation.

## originality

PASS

Gardner 2018 thesis establishes the minimum scalar Italian domination weight gamma_I(L_n)=n and is credited for it, while Shao–Zhao 2026 counts Italian dominating functions on paths, trees, cycles, not the exact ladder-optimum enumerator. The retained original contribution is the unique three-tile all-minimizer classification and all-n generating function; an unexamined full Gardner thesis (PDF access 403) might conceal that count. Inaccessibility alone is not an O fail; residual coverage risk is explicit.

## value

PASS

The all-orders classification and exact enumeration of every optimal Italian dominating labeling on the canonical two-row ladder strengthens a known optimum value by a natural nontrivial structural invariant. The finite local cost-potential lemma and three-tile bijection make the result reusable for constrained domination generating functions; it is not a tiny arbitrary n table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
