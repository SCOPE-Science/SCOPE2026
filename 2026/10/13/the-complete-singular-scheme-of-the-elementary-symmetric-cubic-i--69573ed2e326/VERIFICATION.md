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

# Reproducible checks and limits

Run `python verify.py` from the extracted package directory with ordinary Python 3. It uses only the standard library. The deterministic `verification_output.txt` records the checked finite-field census and ends with `VERIFY_OK`.

The script implements arithmetic in \(\mathbf F_4=\mathbf F_2[t]/(t^2+t+1)\), enumerates every projective vector after scaling its first nonzero coordinate to one, computes the first derivatives of \(e_3\) from \(x_i^2+s_1x_i+s_2\), and compares with the indicator-vector support prediction for \(n=5,7,8,9\). The \(n=6\) census is a deliberate excluded-congruence sanity test; it is not evidence for including that congruence class. The checker also computes exact binary ranks of the Hessian polar matrices, tests nonsingularity of the quadratic tangent cones on all \(\mathbf F_2\)-rational nonzero tangent vectors, and verifies the binomial support count and Bézout-degree balance at \(n=8,12,16,20\).

The finite-field and binary-vector tests cannot establish the theorem over every algebraically closed field, nor can they by themselves prove local Artin length or absence of positive-dimensional components. Those conclusions follow from the universal algebraic argument and complete-intersection length proof in `RESULT.md`. In characteristic two an odd-dimensional smooth quadratic form may have a polar radical, so smoothness is checked by evaluating the quadratic form on that radical, not by requiring an invertible Hessian in every case.

Self-review: passed. Independent audit: not yet performed.
