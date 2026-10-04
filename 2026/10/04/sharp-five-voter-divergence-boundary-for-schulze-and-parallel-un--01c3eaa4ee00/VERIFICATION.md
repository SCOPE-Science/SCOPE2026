---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
The package contains two independent exact verifiers.

`verify_schulze_rankedpairs_full.c` exhausts all labeled four-candidate profiles for one, three, and five voters.

For Schulze it computes strongest paths by Floyd–Warshall on the majority-margin graph.

For set-valued Ranked Pairs it groups victories by equal strength, enumerates every order inside tied strength groups, locks a victory exactly when it creates no directed cycle, and unions the source candidates over all tie orders.

It confirms:
- zero divergence for one voter;
- zero divergence for three voters;
- \(7962624\) five-voter profiles;
- exactly \(51840\) divergences;
- probability \(5/768\);
- equality-count histogram \(6858144,275760,591120,185760\);
- \(51840\) strict \(3\)-versus-\(2\) winner-set containments;
- exactly two canonical weighted-majority margin types, with labeled counts \(11520\) and \(40320\).

Compile and run:

`cc -O3 -std=c11 verify_schulze_rankedpairs_full.c -o verify_schulze_rankedpairs_full`

`./verify_schulze_rankedpairs_full`

The first output line must be:

`VERIFY_OK`

`verify_schulze_rankedpairs_anonymous.py` independently enumerates all \(98280\) anonymous five-voter profiles and weights them by multinomial multiplicity.

Its Schulze computation enumerates simple directed paths directly rather than using Floyd–Warshall. Its Ranked Pairs computation uses Tideman's ranking-elimination formulation rather than graph locking.

It confirms:
- \(576\) anonymous divergent profiles;
- multinomially weighted total \(51840\);
- the same full labeled histogram;
- the same two margin types;
- anonymous type counts \(168\) and \(408\);
- \(48\) exact labeled margin matrices, \(24\) for each candidate-relabeling type.

Run:

`python3 verify_schulze_rankedpairs_anonymous.py`

The first output line must be:

`VERIFY_OK`

The computation proves the stated first odd-electorate layer only.
