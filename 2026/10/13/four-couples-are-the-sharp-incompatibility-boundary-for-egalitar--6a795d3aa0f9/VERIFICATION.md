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
The embedded `verify_sm_egal_minregret_boundary.py` performs an exact finite replay using only the Python standard library.

For every complete strict profile through \(3\) couples, stability is checked independently by:
1. rank-map blocking-pair tests;
2. direct traversal of the original preference lists.

For every stable matching, total rank and maximum rank are independently computed from:
1. rank maps;
2. direct list positions.

The verifier confirms:
- \(1\), \(16\), and \(46656\) labeled profiles for one, two, and three couples;
- for three couples, \(34080\) profiles with one stable matching, \(11484\) with two, and \(1092\) with three;
- \(40056\) profiles with \(E=G\), \(5400\) with \(E\subsetneq G\), and \(1200\) with \(G\subsetneq E\);
- no disjoint or nonnested-overlap case through three couples;
- all \(24\) perfect matchings of the displayed four-couple witness;
- exactly two stable witness matchings;
- rank vectors \((2,4,3,1,1,1,2,1)\) and \((2,2,2,1,3,1,2,3)\);
- objective pairs \((15,4)\) and \((16,3)\);
- disjoint singleton egalitarian and minimum-regret optimum sets.

Run:

`python3 verify_sm_egal_minregret_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive census stops at three couples. The four-couple computation verifies only the displayed sharp witness.
