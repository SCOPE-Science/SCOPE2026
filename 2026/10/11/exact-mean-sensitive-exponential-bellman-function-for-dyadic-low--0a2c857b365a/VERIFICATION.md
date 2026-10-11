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

The critical two-child Bellman inequality was checked symbolically from the proof conditions \(0\le a_0,a_1\le1\), \(0\le d\), and \(a_0+a_1+d\le2\). Its boundary step for \(1\le d\le2\) uses only \(\log q\le q-1\) and \(\log(1-u)\le-u\), with \(1<q<2\). The proof handles infinite depth by dyadic conditional-expectation convergence, not by extrapolating finite computations. The exact extremal moments follow from summing a geometric law with probabilities \(2^{-k-1}\).

Run the accompanying `verify_dyadic_blo.py` using the Python standard library. It tests the split inequality, finite dyadic functions, and geometric-staircase arithmetic (295743 supplementary comparisons in the executed test run). All mathematical conclusions beyond the finite tests depend on the proof in `RESULT.md`. No independent mathematical audit has been performed.
