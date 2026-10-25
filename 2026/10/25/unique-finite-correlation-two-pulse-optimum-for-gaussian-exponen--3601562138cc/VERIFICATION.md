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

The proof uses elementary blockwise integration of the exponential covariance kernel, a derivative sign identity at fixed middle duration, and a scalar monotone-root characterization along the unique symmetric slice. The limits on pulse positions follow strictly from \(0<\log\cosh(b/2)<b/2\). The leading small-duration improvement \(L^4/256\) follows by Taylor substitution.

Run `python3 checker.py` in a directory containing the accompanying standalone file. Python 3 standard library suffices. The recorded deterministic run passed 3,509 comparisons: 800 recursions against independent exact block integrals and 2,709 fixed-scale unrestricted pulse tests/root/bounds checks. For \(L=2\), the optimal intervals were \((0.5491770806,0.9016458387,0.5491770806)\). These numerical checks do not prove global uniqueness; the analytic derivative signs do.

Only ideal Gaussian pure dephasing under exactly two instantaneous inversions is established. No finite-sample confidence, hardware robustness, additional pulse count, or non-Gaussian prediction is certified. An independent audit has not been performed.
