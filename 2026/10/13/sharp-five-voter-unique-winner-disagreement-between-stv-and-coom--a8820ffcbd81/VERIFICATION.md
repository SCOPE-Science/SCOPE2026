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
The embedded `verify_stv_coombs_first_unique_disagreement.py` performs an exact replay using only the Python standard library.

For each electorate size from one through five, it enumerates every anonymous profile as a weak composition over the six strict rankings of three candidates.

STV and Coombs are each evaluated twice:
1. by a generic recursive parallel-universes runoff engine that recomputes plurality or veto scores after every elimination;
2. by an independent closed three-candidate formula that identifies every tied first-round loser and then computes the pairwise outcome of the two survivors.

The two implementations agree on every anonymous profile.

Anonymous profiles are then weighted by exact multinomial coefficients. A separate direct loop over all labeled profiles independently confirms the resulting labeled counts.

The verifier confirms:
- zero different-singleton outcomes for electorates of size one through four;
- exactly \(6\) anonymous five-voter disagreement profiles;
- exactly \(180\) labeled five-voter disagreement profiles;
- exactly \(6516\) labeled five-voter profiles with singleton winner sets under both rules;
- exact incidences \(5/216\), \(5/181\), and \(1/42\);
- one candidate-relabeling orbit among the six anonymous conflicts;
- canonical multiplicities `(0,1,2,0,2,0)` in ranking order `ABC, ACB, BAC, BCA, CAB, CBA`;
- first-place counts \((1,2,2)\), last-place counts \((0,3,2)\), and pairwise tallies \(A\) over \(B\) by \(3\)-\(2\), \(A\) over \(C\) by \(3\)-\(2\), and \(C\) over \(B\) by \(3\)-\(2\);
- Coombs elects the Condorcet winner in every minimal disagreement.

Run:

`python3 verify_stv_coombs_first_unique_disagreement.py`

The first output line must be `VERIFY_OK`.

The computation proves only the stated finite boundary for three candidates through five voters.
