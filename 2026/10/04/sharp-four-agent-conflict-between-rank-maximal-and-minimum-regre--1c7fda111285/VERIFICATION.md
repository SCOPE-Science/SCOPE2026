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
The embedded `verify_rankmax_minreg_stable_roommates.py` performs an exact finite replay with the Python standard library.

For every complete strict four-agent profile it enumerates all three perfect matchings.

Stability is computed independently in two ways:
1. precomputed rank maps;
2. direct preference-list position comparisons.

Rank-maximality is computed independently in two ways:
1. exact lexicographic comparison of rank profiles;
2. a steep-base integer objective with base \(5\).

Minimum regret is computed independently in two ways:
1. minimizing the maximum assigned rank;
2. increasing an admissible-rank threshold until a stable matching exists.

The verifier confirms:
- the two-agent equality base case;
- \(1296\) four-agent profiles;
- stable-matching count marginal \(1098,150,48\);
- relation histogram \(1176\) equality, \(48\) strict \(R(I)\subsetneq M(I)\), \(24\) disjoint, \(48\) unsolvable;
- no other optimum-set relation;
- exactly three disagreement orbits, each of size \(24\);
- one disjoint orbit;
- the canonical witness with stable rank vectors \((1,3,2,1)\) and \((2,2,1,2)\);
- rank profiles \((2,1,1)\) and \((1,3,0)\);
- regrets \(3\) and \(2\);
- equal total rank cost \(7\).

Run:

`python3 verify_rankmax_minreg_stable_roommates.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated two- and four-agent boundary.
