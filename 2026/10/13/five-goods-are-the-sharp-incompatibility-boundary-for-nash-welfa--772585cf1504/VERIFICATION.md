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
The embedded `verify_mnw_leximin_bivalued_boundary.py` performs an exact finite replay using only the Python standard library.

Route A enumerates every labeled valuation profile for two agents and \(1\) through \(5\) goods. Each good has one of the four valuation types \((1,1),(1,2),(2,1),(2,2)\). Every complete allocation is evaluated by the generalized MNW objective and by the sorted leximin utility profile.

Route B independently groups goods by those four types. For every composition \(a+b+c+d=m\), it enumerates how many goods of each type go to agent \(1\), computes the resulting utility pair, and restores labeled-profile counts by multinomial weights.

The replay verifies:
- disjoint-optimizer counts \(0,0,0,0,100\) for \(1\) through \(5\) goods;
- the full optimizer-set relation census through five goods;
- exactly eight bad type-count vectors at five goods;
- exactly four classes after swapping agents;
- class orbit sizes \(10,10,40,40\);
- incidence \(100/1024=25/256\);
- universal first-conflict utility profiles MNW \((3,6)\) and leximin \((4,4)\);
- MNW optimizer-count histogram \(1:80,4:20\);
- leximin optimizer-count histogram \(3:80,6:20\);
- the explicit witness and its complete optimizer sets.

Run:

`python3 verify_mnw_leximin_bivalued_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive classification stops at five goods and concerns exactly two agents with item values \(\{1,2\}\).
