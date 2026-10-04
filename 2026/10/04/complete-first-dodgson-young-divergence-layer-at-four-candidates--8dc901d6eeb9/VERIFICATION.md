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
The embedded `verify_dodgson_young_first_layer.py` performs an exact finite replay using only the Python standard library.

For every one-voter and three-voter profile over four candidates, Dodgson uses the strong Condorcet target and Young uses the weak Condorcet target.

Dodgson scores are computed independently by:
1. a dynamic program over pairwise-margin gains from upward adjacent swaps;
2. direct enumeration of every possible upward final position of the candidate in all three ballots.

Young scores are computed independently by:
1. enumeration of every nonempty voter subset;
2. a specialized three-voter formula checking the full electorate, every two-voter subprofile, and every one-voter subprofile.

The verifier confirms:
- all \(24\) one-voter profiles give the same unique winner under both rules;
- all \(13824\) three-voter profiles are exhausted;
- \(12288\) equal singleton-winner profiles;
- \(528\) equal three-winner profiles;
- \(144\) divergent profiles with winner-set sizes \((2,3)\);
- \(576\) divergent profiles with winner-set sizes \((2,4)\);
- \(288\) divergent profiles with winner-set sizes \((3,4)\);
- total divergence \(1008\), exactly \(7/96\) of the domain;
- strict containment \(D(P)\subsetneq Y(P)\) on every divergent profile;
- exactly seven divergent isomorphism classes under candidate and voter relabeling;
- orbit size \(144\) for every class.

Run:

`python3 verify_dodgson_young_first_layer.py`

The first output line must be:

`VERIFY_OK`

The computation establishes only the stated four-candidate first odd-electorate layer.
