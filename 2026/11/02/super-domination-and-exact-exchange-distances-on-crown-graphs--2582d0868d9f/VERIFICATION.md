---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The frozen classification, enumeration and metric are correct; the repair narrows the contribution. A witness on the opposite shore sees the omissions at indices U except its own. Thus no shore can omit more than two, and omitting two on each forces disjoint index pairs, which suffice. A legal jump then exchanges only a color and a vacancy. Initially occupied positions of wrong color give a lower bound b, each having to be vacated. Index-labeled edges from initial to target colors give a balanced directed multigraph. With different support, all edges lie in the component containing 0 because a disjoint nontrivial component would need both nonzero colors. An Euler traversal based at 0 moves each wrong token once. With unchanged support and a mismatch, the first move fills an index required empty at the end, forcing one extra vacating, and an alternating circuit using that vacancy as a buffer attains the bound. This handles n=4 separately, and for n≥5 establishes connectivity and the unique antipode. To check the coefficients, the binomial moments of the match count are N_n, 2(n−1)(n−2)(n−3), 5(n−2)(n−3), 4(n−3), 1. Binomial inversion and the same-support corrections 4(t³−t²)+(t⁵−t⁴) give the shell polynomial. A slide crosses shores and changes their required counts. Independent direct witness enumeration checked all subsets for 4≤n≤8, then direct minimum-set exchange graphs were checked by BFS for 4≤n≤10. For n=4 there were six isolated states; for n=5 and n=10 the shells were (1,4,8,12,4,1) and (1,24,198,532,504,1), with every tested distance and the unique distance-five state agreeing. Replay: python3 /workspace/branches/f36ec071-0bbc-481c-a1c9-a9f737c069bc/audit_reproduction.py; see reproduction-small.log and reproduction-full.log beside it. The uploaded verifier was inspected, not executed. The finite runs corroborate, but do not prove, the infinite metric.

## originality

PASS

The frozen all-cardinality contribution is already covered, both directly for crowns and as an immediate deleted-matching specialization. The replacement treats the minimum-set classification only as a known input. What survives is the exact vacancy-restricted metric and its derived full distance distribution and antipode, with sliding isolation as a contrast. The strongest inspected near-matches change either the state space or the legal moves, and did not establish that remainder.

## value

PASS

A natural question after classifying crown minima is how many one-vertex exchanges are actually required between two of them. The result gives that exact invariant for every pair, the full distance profile, and a structural distinction from both unrestricted color swaps and token sliding. In particular, the unique farthest state and the cost of recycling an unchanged occupied support address a real reachability phenomenon, rather than just recalculating the covered counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
