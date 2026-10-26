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

# Reproducible checks and boundaries

Run `python VERIFY.py` with `mpmath` installed. The standalone script checks the exact first-lag constant \(1-\pi^2/24\), compares two independently implemented covariance integrals for four branch counts, verifies the derived uniform lag bound at eight powers of two, and compares covariance-summed variances with direct integration of centered Birkhoff sums for lengths one through seven. It also checks that the rigorous analytical series truncation intervals overlap the displayed approximate asymptotic variance.

Observed output in the preparation environment:

```text
VERIFY_OK direct_covariance_q=2,4,8,16 sharp_lag_bounds=8 direct_variance_N=1..7
sigma2_approx= 3.7054859213319754 rigorous_series_tail_bound= 3.9736e-8
```

The coarse printed approximation uses twelve covariance terms; increasing the cutoff improves the certified series-tail bound but still requires numerical quadrature accuracy to be assessed separately. The universal \(k\)- and \(N\)-quantifiers are justified by the algebraic proof, not the finite checks. Independent scientific validation has not been performed.
