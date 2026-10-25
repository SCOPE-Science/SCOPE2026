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

The Fourier restriction/dilation normalization was derived explicitly, and the exterior-power Cauchy--Binet leading term was checked algebraically. The Vandermonde Gram identity yields exactly the ratio of successive Hankel determinants, with the factor \((2\pi)^{2n}/(n!)^2\) in the squared singular-value law.

Run `python checks/low_bandwidth_check.py` in an environment with Python 3, NumPy, SciPy and SymPy. The program computes rational Hankel determinants for two disconnected non-symmetric sets and compares the first three concentration eigenvalues against the theorem at multiple bandwidths. It additionally checks the eigenfunction polynomial limit by absolute inner products. The finite tests are diagnostic only and do not establish an asymptotic theorem.

The proof requires bounded positive-measure sets, fixed mode index, and decreasing positive bandwidth. It does not cover a growing mode index, unbounded windows, or quantitative rates uniform over all window pairs. Historical-priority comparisons do not constitute independent certification.
