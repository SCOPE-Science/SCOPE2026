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

For provided candidate order and interval approvals, an unrepresented voter approving an unselected candidate c strictly between two consecutive selected positions a<b has its entire ballot strictly inside (a,b), and conversely: this is an exact if-and-only-if, including first/last sentinel gaps and empty ballots. The good-gap predicate G(a,b) therefore characterizes all q-JR committees by increasing paths. The suffix recurrence F_0(a)=G(a,m+1) and F_t(a)=sum_{b∈E,b>a} G(a,b)F_(t-1)(b) counts each size-k eligible committee exactly once. The O(m²(n+m)+km²) cost and ≤2^m integer counts are correct; conditional path weights telescope to uniform sampling, with exact bounded random integers. DR is JR restricted to candidates whose approval count equals ceil(n/k). An independently written brute candidate-level predicate matched gap DP in 15,885 exhaustive interval/size/quota cases (m≤4,n≤3), separate from package claims of larger test sweeps.

## originality

PASS

Best-of-knowledge comparison of statements rather than titles: close primary results supply tools, partial parameter regimes or weaker scalar/qualitative conclusions but do not directly cover this particular exact claim. Inaccessible plausible broader results are named and retained as specific historical-priority risks, not treated as automatic failure.

## value

PASS

Counting justified-representation committees is a natural hard counting problem on general approval profiles, and the number and uniform distribution of feasible committees quantify representation flexibility, not merely existence. The supplied dynamic program and exact sampler close a substantial tractable candidate-interval case with arbitrary candidate eligibility and quota. The exact sampling result has independent use and is not a routine consequence of knowing a single feasible committee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
