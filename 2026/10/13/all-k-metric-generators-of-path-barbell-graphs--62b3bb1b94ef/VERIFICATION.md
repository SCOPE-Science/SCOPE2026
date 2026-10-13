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
# Verification

The standalone `verify.py` constructs each path-barbell from the definition and computes all-pairs shortest-path distances by breadth-first search. It then checks the literal definition of a \(k\)-metric generator against the claimed structural predicate for every subset.

The exhaustive grid is \(3\le p,q\le5\), \(1\le\ell\le3\), and \(k\in\{1,2,3\}\). For \(k=1,2\), the script also compares the complete cardinality histogram of valid subsets with the stated generating-polynomial coefficients and checks the predicted minimum size and number of minimum sets. For \(k=3\), it verifies that no valid subset exists.

Replay output from the packaged script:

`VERIFY_OK parameter_triples=27 k_values=3 subset_checks=65856 max_order=12`

This finite computation does not prove the infinite family. The proof in `RESULT.md` supplies the general argument from twin classes and explicit path distances. The checker is a bounded stress test of definitions, boundary parameters within the stated domain, coefficient formulas, and case handling.
