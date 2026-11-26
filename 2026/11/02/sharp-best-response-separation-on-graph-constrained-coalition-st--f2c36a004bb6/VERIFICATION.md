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

A feasible partition consists of the hub coalition and singleton outsiders. A leaf cannot leave the hub strictly improving because its only other feasible destination is its singleton. Every outsider accepts a hub offer by individual rationality; the hub can only strictly improve by going to an outside leaf, since singleton hub is no better under either set of assumptions. Hub utility weakly increases on a consensual leaf join. In the monotone case, at its first move the hub chooses a highest-ranked outside pair; every previously attached leaf's pair is no better than the old coalition by monotonicity, hence is strictly worse than the chosen pair. The chosen leaf stays, and subsequent joins cannot lower the hub's ranking below that pair, so there is no second hub move. With no hub move there are at most n-1 joins; with one, its recipient has never joined and every other leaf can join at most twice, yielding 2n-3 including n=2. The prize construction works with nonnegative edge values, weak acceptance at value zero and unrestricted scheduling among movers. In the IR-only witness write k=n-2; leaf utility one in every hub coalition makes each indicated join its best response. At stage j the min-index hub payoff stays j as all free leaves with index >=j+2 join. Leaf a_(j+1) is left outside and is the available pair with largest index, so moving to it is a strict best response. Together with the initial move to the sole outside leaf a_1, this gives k hub moves and (k-1)(k-2)/2 joins, including k=1. More generally, after any hub move its utility is a fixed pair utility; successive such utilities strictly rise, so there are at most n-1 hub moves and at most n-1 joins between them. This proves the quadratic upper independently. The frozen finite checker was inspected but not executed.

## originality

PASS

The IR-only quadratic upper bound is prior (and transfers to best responses by containment). The inspected prior lower witness is for improving moves and the authors explicitly identify the failure to extend their examples to best responses. The credited contributions are the sharp 2n-3 worst case under hub monotonicity and a genuinely best-responding quadratic-length witness with IR alone. The displayed lower trajectory length is not asserted to be the exact IR maximum.

## value

PASS

The witness answers a specific open speed-up question in the IR star setting rather than duplicating the known convergence bound. The complementary sharp linear analysis identifies a structural condition on only the hub, with leaves still arbitrary IR, and gives a matching additive witness for every n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
