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

At integer r>=2 and any finite n>=1,k,m>=0, if two agents differ in large-good counts by >=2, transfer one heavy good and optimally redistribute their combined unit goods. The attainable pair-load differences have fixed parity and centers r Delta and r(Delta-2)>=0; lowering center cannot raise minimum achievable absolute imbalance, and therefore improves global majorization. Sum of squared heavy-good counts strictly falls, proving termination at counts q or q+1. With fixed balanced baselines, assigning each unit item to currently least-loaded agent minimizes every convex separable sum by ordered marginal increments; same vector therefore is majorized by every feasible allocation. Explicit three-case compressed formula follows by water-filling baselines with gap r. For noninteger r>1, select two agents, two large items and odd integer m with |2r-m|<1: balanced heavy items give discrepancy 1, whereas putting both heavy on one agent and units on the other gives smaller discrepancy, so the two-stage rule is not universally Lorenz optimal. Independent brute-force enumerated all labeled allocations and verified sorted partial sums for n=2–4 representative heavy/light multiplicities, including n=4,k=3,m=3,r=3 with 4096 assignments. All stated boundaries include zero items and one agent. Not an impossibility claim for any other allocation method at irrational ratios.

## originality

PASS

Common-object Lorenz domination for all symmetric Schur-concave welfare functions is stronger than maximizing a single p-mean objective, whereas the established 2026 algorithms and 2022 bivalued papers target Nash, leximin, or egalitarian objectives individually. Their algorithmic implications do not automatically prove the every-convex-sum majorization minimality or iff integrality for the named two-stage algorithm. General identical-machine two-job-length scheduling and resource-allocation literature are substantial prior-coverage risks; the present structural smoothing lemma and compressed exact profile were not located as an existing corollary in inspected material. Treat best-of-knowledge rather than absolute priority.

## value

PASS

For identical valuations this is a motivated complete characterization of a canonical allocation policy across *all* symmetric Schur-concave objectives, with a sharp arithmetic distinction integer versus noninteger ratios. The explicit three-case load multiset uses O(1) integer divisions even when multiplicities are binary-encoded, while the counterexample shows why the rule breaks outside its sharp boundary. This is an independently useful allocation and majorization theorem, beyond solving one utility objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
