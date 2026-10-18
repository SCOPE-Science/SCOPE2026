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

The character sum was compared with the differentiated sine-quotient formula at multiple sample angles for cutoffs \(L=0,1,2,4,11\). Numerical quadrature of the absolute central kernel gives endpoint norms consistent with the exact integral, including \(\Lambda_0=1\). The period/root series is numerically negative and converges toward \(-0.10304\). `checker.py` reproduces these checks using NumPy and SciPy.

The proof of the all-cutoff asymptotic is analytic: it uses the exact weighted character identity, a uniform oscillatory-tail decomposition, dominated convergence on finite intervals, and a signed-period argument proving the correction strictly negative. Numerical quadrature is not used as an infinite-dimensional certificate. The integral's decimal value is not interval certified, and no finite-remainder rate is claimed.
