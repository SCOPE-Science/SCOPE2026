---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=2 the process is uniform among currently feasible edges because independent random priorities are exchangeable conditional on the past. At k unmatched labels on each side and overlap r the feasible count is k^2-r, with transitions r->r-2,r-1,r in weights r(r-1),2r(k-r),(k-r)^2. At k>=2 there is always a feasible edge; failure iff final shared singleton. The conditional first-moment identity telescopes to the exact nonnegative defect 2/(n+1)-Q_n=4 sum_{k=2}^n E[(R_k)_2/(k(k-1)(k+1)(k^2-R_k))]. The second-factorial contraction gives E[(R_k)_2]<=k^4/n^2; hence the specified 16 H_n/n^2 bound and n Q_n->2 without extrapolation. Independent exact bit-mask DP agrees with overlap-chain probabilities through n=7; Q_2=0,Q_3=1/3,Q_4=4/21. The polynomial contraction inequality is positive at k=2 and increasing thereafter. I found no missing boundary assumption.

## originality

PASS

The fixed deterministic crown graph rare-event constant is distinct from generic greedy-matching approximation bounds, averaged random-graph comparisons, and unrelated crown graph invariants. The actual derivation has a nontrivial conserved-moment defect and a second-moment estimate. Historical priority remains qualified by incomplete access to the 1991 general-matching paper.

## value

PASS

A canonical dense bipartite graph minus a perfect matching has a nontrivial rare failure mechanism; a sharp coefficient 2/n, finite recurrence, and universal explicit error refine the comparison with an unrestricted random partial matching (coincidence 1/n). The result supplies exact benchmark probabilities for greedy matching rather than a routine generic approximation ratio.

The dated certificate retains the supplied scientific assessment, sources and limitations.
