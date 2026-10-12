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
The embedded `verify_sr_egal_minregret_boundary.py` performs an exact finite replay using only the Python standard library.

For complete strict Stable Roommates profiles, it independently checks stability using:
1. precomputed one-based rank maps;
2. direct positions in the original preference lists.

For every stable matching, it independently computes:
1. total rank and maximum rank from rank maps;
2. the same two values from direct list positions.

The replay verifies:
- equality of the egalitarian and minimum-regret optimum sets for the two-agent base case;
- all \(6^4=1296\) complete strict four-agent profiles;
- \(48\) unsolvable, \(1098\) uniquely stable, and \(150\) two-stable profiles;
- among \(1248\) solvable profiles, \(1176\) with equal optimum sets, \(48\) with \(E\subsetneq G\), and \(24\) with \(G\subsetneq E\);
- no disjoint or nonnested-overlap four-agent case;
- exactly three disagreement isomorphism classes, each with orbit size \(24\);
- all \(15\) perfect matchings of the displayed six-agent witness;
- exactly two stable witness matchings;
- objective pairs \((13,3)\) and \((12,4)\);
- disjoint singleton egalitarian and minimum-regret optimum sets.

Run:

`python3 verify_sr_egal_minregret_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive lower bound stops at four agents. The six-agent computation verifies only the displayed sharp witness.
