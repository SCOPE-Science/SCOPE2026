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

# Verification record

The standalone `verify.py` was run using a standard Python interpreter with NumPy and SciPy. It completed spectral/eigenvector checks for 32 fixed parameter/dimension combinations, stationarity checks on five independently constructed count chains, and direct total-variation computations for three population sizes across centered-time values and biased/unbiased rates.

In the unbiased three-level case at \(c=0\), the observed total-variation distances were \(0.4656007\), \(0.4633971\), \(0.4617124\) for \(m=20,40,80\), compared with Gaussian limit \(0.4597086\). These checks identify finite-state consistency, not a computational certificate of an asymptotic theorem. The general conclusion is supported by the proof in `RESULT.md`, including its discrete-to-continuous spectral comparison.

No independent audit or independent validation has been performed. Nonuniform-in-\(k\) or nonhomogeneous-initial profile claims are not made.
