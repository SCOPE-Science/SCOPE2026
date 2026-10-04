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
The embedded `verify_black9_reinforcement.py` provides an exact finite replay using only Python's standard library.

Route A enumerates every anonymous three-candidate profile for electorate sizes \(1\) through \(9\), computes the unique Black winner where defined, and tests every unordered pair of eligible subelectorates for totals through \(9\). It verifies zero reinforcement failures for totals \(2\) through \(8\) and exactly \(12\) at total \(9\).

Route B independently enumerates every anonymous nine-voter union profile and every componentwise split into two nonempty subprofiles. It recomputes all three Black outcomes and is required to recover exactly the same \(12\)-pair set as Route A.

The replay additionally verifies the \(6\) pairs of type \(1+8\), the \(6\) pairs of type \(4+5\), exactly two candidate-relabeling pair classes of orbit size \(6\), exactly six labeled union profiles in one candidate orbit, exactly two paradox-producing partitions per union, and the two Condorcet/Borda branch patterns.

Run:

`python3 verify_black9_reinforcement.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the finite three-candidate, tie-independent statements above. It does not claim a formula for larger electorates or more candidates.
