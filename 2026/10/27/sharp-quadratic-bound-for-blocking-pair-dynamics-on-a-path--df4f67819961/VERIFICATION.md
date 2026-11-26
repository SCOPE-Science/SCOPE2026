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

For fixed strict preferences, orient the line of acceptable edges toward the locally preferred edge. At j the directed ancestor sets of incoming neighbors are disjoint, so its ancestor weight is 1 plus the sum of all incoming weights. A blocking move adds j and removes only incoming occupied neighbors, increasing the sum of matching weights by at least 1. For a matching S of size k, every nontrivial directed path s to t with both ends in S yields an unoccupied predecessor u of t and a nonreachable pair (u,s); the path toward t precludes reaching s from u. The pair determines s, and the side of u relative to s determines its outward neighbor t, so this charging is injective. Consequently the potential is at most k+k(n-1-k)=k(n-k) and hence at most floor(n²/4). For the all-left preferences, sweeping a newly formed edge leftward on the free suffix and parking it consumes n-2q-1 moves in phase q without disturbing parked edges, including the endpoint/single-move phases; the total is floor(n²/4). This covers arbitrary starts and move choices and proves termination at stability. Independent bounded enumeration for n=2..8 reproduced maxima 1,2,4,6,9,12,16 for arbitrary starts and for empty starts, including the all-left witness. Replay: enumerate 2^(n-2) neighbor-order bit strings and all nonconsecutive chosen edge subsets, draw each legal edge-insertion arc by comparing current partners at both endpoints, then take the longest directed path in each acyclic graph. The source package's verify.py specifies a separate finite replay for n=2..11 and witness sizes 2..80; it was inspected, not executed. The general bound rests on the proof, not on enumeration.

## originality

PASS

The supported distinction is the exact total number of arbitrary legal moves in the worst case on a path, with an empty-start witness. The inspected comparisons do not establish this threshold. Neither the line-graph encoding nor forest convergence is claimed as new.

## value

PASS

For a natural graph restriction and a canonical local update, the total worst-case number of moves controls every implementation or adversarial schedule, unlike existence of a short path. The cubic-to-sharp-quadratic distinction and the extremizer from empty are meaningful; the charge on nonreachable pairs makes the exact path bound more than a convergence restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
