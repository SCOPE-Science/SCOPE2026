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
The proof uses two source-backed smooth-curve formulas and standard complete-intersection adjunction. It then proves the classification by an elementary inequality valid for all allowed multidegrees.

A standalone exact checker performs a bounded regression test. It enumerates all nondecreasing multidegrees with \(4\le N\le9\) and \(2\le d_i\le12\), recomputes both degree formulas with integer arithmetic, and verifies that exactly three tuples have \(\deg\operatorname{Sec}(C)\le\deg\operatorname{Tan}(C)\), with equality only for \((2,2,4)\).

The bounded enumeration is not used to infer the infinite theorem. The infinite classification is supplied by the monotonicity proof in RESULT.md.

Scientific limits: smooth complex complete-intersection curves, ambient dimension at least four, and defining degrees at least two. Singular curves require local correction terms.
