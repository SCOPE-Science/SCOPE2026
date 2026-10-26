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

# Verification record
The `verify.py` script directly tests, for each selected pair, whether a shortest path of length at most two exists with no other selected internal vertex. It compares that direct predicate against the ball-or-tetrahedron classification and the coefficient formulas.

Exhaustive vertex-subset enumeration was performed for the \(3\)- and \(4\)-dimensional binary cubes. Every subset of the \(5\)-cube of cardinality at most six was also checked; the unrestricted upper-size bound is proved mathematically, not certified by this finite enumeration. In dimensions three and four, inclusion-maximal subsets were explicitly tested by single-vertex augmentation. Reproduction uses a standard Python 3 interpreter, without third-party packages: `python3 verify.py`.

Expected standard output is embedded as `verification_output.txt`. The completed checker examined 1,214,809 selected-vertex subsets. All comparisons passed. The script and log are finite sanity checks, not independent review or a machine-checked proof of all dimensions.
