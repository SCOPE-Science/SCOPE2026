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

# Verification of the triangular-graph zero forcing theorem

The accompanying `verify.cpp` uses C++17 standard libraries only. From the directory containing it, run `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. The program terminates with `ALL_VERIFY_OK` only if all checks pass.

At each \(n=3,4,5,6,7\), every one of the \(2^{\binom n2}\) initial white-edge sets is examined (there are \(2,097,152\) at \(n=7\)). The line-graph forcing process and the independent union-find acyclicity/isolation test agree exactly. For \(n\le6\), a different serial forcing implementation also agrees. Coefficients are compared with an independent labeled-forest recurrence, verifying in particular the polynomial for \(n=5\). For \(n\le6\), minimum-set exchange adjacency is enumerated directly, its graph is checked connected, and cross-isolated-label exchanges are counted to match the formula.

Expected minimum-set counts for \(n=3,4,5,6,7\): \(3,12,80,750,9072\). Expected cross-isolate counts for \(n=3,4,5,6\): \(3,24,270,3840\). The detailed terminal output is produced by running the standalone program; this package contains its complete code, not a claim of an independently conducted audit. The proof for all \(n\ge3\) is in `RESULT.md`; finite checks cannot establish that universal quantifier alone.
