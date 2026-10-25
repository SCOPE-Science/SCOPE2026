---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For G=K_(a,b) minus t disjoint cross-edges with a,b≥3, any >=3 initial white vertices on one side cannot ever be the first forced there because every opposite blue vertex has at least u−1>=2 white neighbors. A white pair on one side must include a matched endpoint to allow a blue opposite partner to see only the other. When both white sides have size two, initial forces exist exactly if the marked index sets I_U, I_V are unequal; equality is a complete deadlock. Checked completion cases u,v≤1, (2,0), (2,1), and symmetric, including a=3 exceptional one-blue-on-side case: a matched opposite partner always supplies a valid first move. Thus admissible whites sizes 0–4 are exactly those characterized in RESULT.md. Counting gives 1,N,ab+p+q,bp+aq,r with p=binom(a,2)−binom(a−t,2), q=binom(b,2)−binom(b−t,2), r=pq−t(a−t)(b−t)−binom(t,2). At t=0,1,>=2, r/support yield sharp Z=N−2,N−3,N−4. Independent brute-force simulation of all blue masks for selected (a,b,t): (3,3,0..3), (4,5,2),(4,5,4) matched predicted polynomial (e.g. t=2 3×3 coefficients 1,6,15,18,6); source verify.py independently read but opaque uploaded code not run. Unlimited parameter result rests on forcing-move classification, not finite sample.

## originality

PASS

Best-of-knowledge PASS for positive matching deletion. Boyer et al already give undeleted K_(a,b) polynomial and generic two top coefficients, which are acknowledged. Related Resultary exact non-CIS-pair count is the same graph family but a different property. No inspected source supplies the newly enumerated white deadlocks and low-degree polynomial coefficients.

## value

PASS

Deleting a matching from a dense bipartite graph is a natural sparse perturbation, including crown graphs. The complete zero-forcing set polynomial and exact sharp two-stage collapse at t=1 and t=2 distinguish all forcing-set sizes and minimum-set multiplicities, significantly refining the known undeleted K_{a,b} polynomial and scalar invariants. This structural family result supports further forcing polynomial comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
