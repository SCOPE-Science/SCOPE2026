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

# Verification of the seven-cube theorem

The self-contained `verify_q7.py` requires Python 3 with only the standard library and can be run with `python3 verify_q7.py`. It constructs the 128 seven-bit vertices and both 64-vertex parity classes. Closed radius-two neighborhoods are formed directly from bit differences. Exhaustive enumeration of all independent triples confirms that none dominates a parity halfcube. Exhaustive enumeration of all independent quadruples confirms exactly 1,120 dominating quadruples, all with four distance-four and two distance-six pairs; 70 contain the zero word. Their independently selected even and odd copies yield exactly 1,254,400 minimum maximal total-visibility sets.

For actual shortest-path visibility independently of the distance-two lemma, breadth-first searches with selected internal vertices blocked verify explicit eight- and sixteen-vertex examples and reject a two-vertex non-example. The embedded `verification_output.txt` records the program's actual result. The finite exhaustive checks cover the entire stated dimension, and the mathematical proof provides an independent count and characterization. The external scientific audit is not performed; no independent verification is claimed.
