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
The embedded `verify_maximin15_reinforcement.py` is a standard-library-only exact replay.

For three candidates, each anonymous profile is represented by the six counts of the strict rankings. Pairwise majority margins and maximin scores are computed with integer arithmetic.

Route A enumerates every unordered pair of nonempty anonymous profiles for each total electorate size through \(15\), restricted to pairs having the same unique maximin winner. It verifies zero reinforcement paradoxes for totals \(2\) through \(14\), and exactly \(18\) at total \(15\), all with electorate sizes \(5\) and \(10\).

Route B independently enumerates every anonymous \(15\)-voter union profile and every componentwise decomposition into two nonempty subprofiles. It recomputes the maximin winner of each part and the union and is required to recover exactly the same \(18\)-pair set as Route A.

The replay further verifies:
- exactly \(3\) candidate-relabeling pair classes, all of orbit size \(6\);
- exactly \(18\) distinct union profiles, each with one paradox-producing partition;
- exactly \(3\) candidate-relabeling union classes, all of orbit size \(6\);
- each ordered change from one candidate to a different candidate occurs exactly \(3\) times;
- in every minimal pair, the \(5\)-voter side has the shared winner as Condorcet winner, the \(10\)-voter side has no Condorcet winner, and the union has the new winner as Condorcet winner.

Run:

`python3 verify_maximin15_reinforcement.py`

The first line must be:

`VERIFY_OK`

The computation proves only the finite three-candidate, unique-winner statements above.
