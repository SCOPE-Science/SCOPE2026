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
# Reproduction of mathematical checks

Extract `median_tv_checker.py` alongside this file and run `python3 median_tv_checker.py` using Python 3. There are no third-party dependencies. The exact-integer checker passes all of the following independently executable regressions:

- \(5910\) strict orderings, exhaustive for dimensions \(3,4,5,6,7\), with every nonempty proper cyclic arc tested in each ordering. The maximal component counts are \(0,2,2,3,3\).
- \(37\) analytic strict-order witnesses for dimensions \(4\) through \(40\), including actual two-dataset perturbations remaining inside one order chamber.
- \(8184\) binary signals for dimensions \(3\) through \(12\), checking the one-input variation-decrease property.

These finite tests do not establish all-dimensional correctness. The proof in RESULT.md uses an exact arc-indicator reduction, the three-component locality bound, and explicit all-dimension attaining data. The result concerns all real inputs, including ties by continuity. No formal verification or external scientific validation is claimed.
