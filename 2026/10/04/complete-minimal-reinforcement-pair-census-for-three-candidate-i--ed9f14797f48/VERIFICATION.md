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
The embedded `verify_irv13_reinforcement_pairs.py` provides an exact finite replay.

Route A enumerates every anonymous three-candidate profile for electorate sizes \(1\) through \(13\), retains only uniquely determined IRV outcomes, and tests every unordered pair whose electorate sizes sum to a given total. It verifies that totals \(2\) through \(12\) contain no reinforcement-paradox pair and that total \(13\) contains exactly \(288\).

Route B independently enumerates every anonymous \(13\)-voter union profile and every componentwise split of that union into two nonempty subprofiles. It evaluates the two subelections and the union from scratch and is required to recover exactly the same \(288\)-pair set as Route A.

The replay also verifies the universal \(5+8\) split, \(48\) candidate-relabeling pair classes of size \(6\), \(126\) distinct unions, \(21\) candidate-relabeling union classes of size \(6\), and the union partition-multiplicity histogram \(1:36,\ 2:36,\ 3:36,\ 4:18\). The displayed witness is checked explicitly.

Run:

`python3 verify_irv13_reinforcement_pairs.py`

The first output line must be:

`VERIFY_OK`

All statements are finite. No claim about four or more candidates or larger electorate totals is inferred from this computation.
