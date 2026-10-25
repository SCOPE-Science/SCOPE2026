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

# Reproducibility and scope

The proof is analytic. `check.py` performs independent finite-dimensional optimization comparisons using both a brute-force enumeration and a linear-sum-assignment reduction. It also tests the collision-repair sandwich and runs seeded Monte Carlo diagnostics; the observations are in `CHECKS.txt`. The finite checks do not certify the Poisson point-process convergence, the moving-rank Gaussian quantile approximation, or bibliographic uniqueness.

The geometric conversion is exact: for \(G\) with iid standard normal coordinates, \(\widetilde G=G-\overline G\mathbf1\) is isotropic in the hyperplane of zero coordinate sum, so \(\widetilde G/\|\widetilde G\|_F\) is uniform on its sphere. Support *differences* between polytopes at the same fixed coordinate sum are unaffected by the centering operation. The asymptotic radial factor is separately controlled by chi-square concentration.

Critical parameters are precisely \(k_N/\sqrt N\to c\in(0,\infty)\) and \(t_N=\Phi^{-1}(1-k_N/N^2)\). The law has intensity \(2c^2\) for total width loss and intensity \(c^2\) for each support loss; the exponential **rate** is two. Both count and jump parameters matter and must not be interchanged.
