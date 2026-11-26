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

A disconnected coalition gives each member −∞ and cannot be stable or welfare-maximizing. When hubs separate, every unattached leaf is singleton and would strictly gain by joining its hub. The full separated stars are stable: a hub earns at least one, and moving to the other hub gives one. For joined hubs with p left and q right leaves, left and right leaves earn 1−q and 1−p, respectively, in the hub coalition versus zero in a singleton. Participating leaves prohibit negative utility, and absent leaves prohibit positive entry utility. Hubs already earn at least one and can gain at most one elsewhere. If q=0, entry forces p=a, and symmetrically p=0 forces q=b. If both are positive they must each be one. Counting labeled choices gives ab+3, including four distinct partitions at a=b=1. The number of internal edges in the joined coalition is 1+p+q and there are pq opposite-leaf pairs at distance three, giving W=2(1+p+q−pq)=4−2(p−1)(q−1). The joined shape with both sides nonempty has W<=4; with one side empty welfare is at most 2(1+max(a,b)). Separated welfare is at most 2(a+b), uniquely attained by two full stars in that case. These bounds give exactly the stated welfare multiset, global optimal partitions and two price ratios, with strict inequalities interpreted as mover improvements and no destination consent. Independent restricted-growth-by-block partition recursion with induced distances and exact strict deviation checks (branches/independent-replays/double_star.py) reproduced the full stable partition identities, welfare and all optima for all 21 ordered a,b with a+b<=7. The frozen checker was inspected, not executed. Its module docstring names the wrong file, but both RESULT.md and VERIFICATION.md give the correct command. Its optimum count is printed, not asserted; the independent replay and proof cover that count.

## originality

PASS

Credit the exact game model and score-vector example to Ganian et al. and the established broader phenomenon of large PoA in related models. The inspected evidence does not give the double-star equilibrium classification, labeled count and welfare multiset for these induced-distance additive scores, or the resulting family-exact price ratio.

## value

PASS

The double star is a simple natural tree with enough diameter to activate the negative score, and the two hubs are the only possible connectors. A complete labeled count with the exact welfare multiset is useful beyond a single poor equilibrium witness: all optimal outcomes and both extreme price ratios are isolated for unequal as well as equal leaf counts. It gives a sharp linear loss with a stable optimum on treewidth one at fixed diameter three, not a new claim about the analogous normalized models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
