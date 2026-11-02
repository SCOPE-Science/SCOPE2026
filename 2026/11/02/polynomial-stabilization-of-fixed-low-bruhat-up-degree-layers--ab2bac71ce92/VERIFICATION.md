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

# Computational verification and boundaries

Execute `python3 verify.py` with Python 3 and its standard library. The checker computes the upward-cover statistic two independent ways (literal interval-triple test and an extremal-record test), verifies that cover-graph connectivity agrees with skew indecomposability, and enumerates all permutations through order nine. It constructs coefficient counts from skew-indecomposable blocks and checks the rational-coefficient extraction through \(r=5\), including the closed formulas for \(r=2,3\). The expected terminal line is `VERIFY_OK`; intermediate checks identify 409,113 explicitly enumerated permutations.

These checks are finite and cannot independently certify the all-r theorem. The independent infinite argument in RESULT.md uses the interval-component lemma, the additive skew decomposition, the lower bound of \(s-1\) covers in an indecomposable block, and the formal generating-function extraction. No external independent audit is claimed.
