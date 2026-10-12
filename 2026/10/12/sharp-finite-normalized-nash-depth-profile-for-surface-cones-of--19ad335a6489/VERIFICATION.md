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
Run `python artifacts/verify.py artifacts/index_depth_profile.csv` in a Python 3 environment. No external packages are needed. The checker reads the complete certificate from the actual packaged path, regenerates all \(1307\) rows from Hilbert bases and Nash tangent cones, and asserts exact equality, the unique maximal depth at each index, every onset threshold, and the chain at index \(65\).

The finite enumeration is exhaustive because all primitive index-\(q\) plane cones admit a standard representative \((1,0),(p,q)\) with \(0\le p<q\) and \(\gcd(p,q)=1\), and all values \(2\le q\le65\) are visited. Hilbert basis candidates cannot lie outside the stated finite rectangle by the fundamental-parallelogram subtraction lemma. Propositions 4.11–4.12 of arXiv:0910.5028 give the precise fan recursion. All calculations are over integers and rational numbers, not floating point.

The recorded result is a finite-index theorem only. Neither the checker nor the reviewed proof asserts that the logarithmic depth profile persists at larger index. Independent audit has not been performed.
