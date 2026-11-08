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

Assume every vertex has degree 1 or 2, and utility same-coalition neighbors divided by total coalition size. A stable partition cannot give any vertex zero internal neighbors (move to a neighbor gives positive utility). On a crossing edge vw, each endpoint has exactly one internal friend and one external friend, so nonimprovement in both directions forces ||A|−|B||≤1. Conversely each vertex with two internal friends has no profitable outside move, and each vertex with one has at most one external friend, to whose coalition payoff 1/(|B|+1)≤1/|A| under size balance. Thus criterion works even if coalitions disconnected; singleton creation never improves. For C_n, a coalition of t≥2 runs needs each run and each gap length≥2, hence n≥4t. Alternating two coalitions in runs length≥2 with size difference≤1 attains t=floor(n/4). At n=8 exactly two distinct stable labeled partitions have disconnected coalition. Exact small-n independent exhaustive partition calculations confirmed counts 1,3,6,6,15,17 through n=8 and 2 disconnected n=8; infinite proof is structural.

## originality

PASS

2018 Bilò et al. address Nash existence, efficiency, and welfare optimization on various graph types; the full OA paper was consulted at relevant model definitions and main topology cases. They do not directly state the all-partition degree-two iff local certificate or exact fragmentation threshold in inspected material. Related Hanaka et al. bounded-treewidth welfare results and the modified denominator model are distinct. Qualified PASS, possibility of equivalent special graph-local characterization in unindexed game literature.

## value

PASS

Local O(n+m) complete Nash decision for arbitrary disconnected coalitions on paths/cycles and exact sharp first fragmentation threshold is a motivated structural graph-game theorem; it distinguishes stable clustering from connected clustering and supplies both obstruction and attaining constructions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
