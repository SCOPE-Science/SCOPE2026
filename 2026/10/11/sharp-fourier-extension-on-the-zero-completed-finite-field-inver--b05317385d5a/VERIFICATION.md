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

# Verification of sharp inverse-graph fourth moments

The self-contained checker `artifacts/verify.py` needs only Python 3's standard library. Run `python3 artifacts/verify.py` from the package root; expected actual output:

`VERIFY_OK fields=8 including F25,F49 complex_convolution_identity_tests=104 sharp_phase_extremizer_tests=24 root_residual=PASS`

The checker constructs finite fields (including the quadratic extensions of orders 25 and 49), computes full ordered-pair convolutions, and compares exact structural identity (1) against these independent numerical convolutions for 104 complex samples. It tests 24 phase-rich sharp witnesses across both arithmetic branches and computes the cubic root residual. The unrestricted mathematical proof uses the pair-sum classification and analytic inequalities in RESULT.md; finite samples alone cannot prove the infinite-field statement. The use of floating-point coefficients and tolerances in these tests is explicitly limited to computational corroboration. No independent audit has been performed.
