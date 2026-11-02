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

The mathematical proof establishes the result for every finite tree and every admissible path parameter. The finite verification below checks critical boundary and compatibility behavior independently of the symbolic proof. It cannot establish the unrestricted theorem by enumeration.

The standalone file `verify.py` uses Python 3 standard library only. Run `python3 verify.py` from the extracted package directory; the expected output is in `verification_output.txt`. The checker independently enumerates edge orientations of sampled small trees, computes Boolean reachability of ordered pairs by direct traversal along their unique paths, and compares all realized label patterns with the stated structural criterion. A second check enumerates integer interval systems and verifies the exact optimum for all \(2\le d\le m\le8\).

Actual replay: `DIRECT_SHATTERING_COMPARISONS_PASS 22332`; `INTERVAL_EXTREMAL_CASES_PASS 28`; `ALL_TREE_REACHABILITY_CHECKS_PASS`. Only finite instances were executed. The shattering criterion's necessity, sufficiency, and sharp general interval upper bound have separate proofs in `RESULT.md`.
