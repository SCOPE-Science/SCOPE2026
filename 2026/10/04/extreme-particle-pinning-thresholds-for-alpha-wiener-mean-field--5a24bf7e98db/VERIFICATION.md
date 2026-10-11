---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Subtracting the equal-weight ensemble mean from each particle removes the common mean term and yields a scalar linear residual SDE with kernel ((T-t)/(T-s))^alpha. At each fixed t the kernel integrals are iid centered Gaussians with variance v_alpha(t), so the entire residual vector is exactly sigma sqrt(v_alpha(t)) times an iid Gaussian sample centered by its empirical mean. The maximum differs from the ordinary absolute-Gaussian maximum by at most |bar Z_n|; since sqrt(log n)|bar Z_n| tends to zero, both first-order scaling and the 1/b_n Gumbel refinement transfer. Direct integration gives the three alpha regimes and hence the exact condition v_alpha(t_n) log n -> 0 for simultaneous pinning, with the stated critical windows. A fresh analytic/numeric check confirmed positivity and the closed-form regimes, while the packaged verifier separately checks quadrature and tail normalization.

## originality

PASS

The exact source model derives the residual representation and alpha-Wiener specialization but explicitly says the influence of the interaction function on convergence speed is left for future research, and separately leaves the spatial convergence rate for future work. The inspected primary article contains no growing-particle maximum theorem, no log-n terminal window, and no Gumbel profile. Single alpha-Wiener bridge endpoint theory and general mean-field concentration results do not imply the exact centered-Gaussian maximum reduction or the three joint n/t regimes. Resultary searches found no equivalent published SCOPE claim.

## value

PASS

The model source explicitly identifies convergence speed as an open issue. Uniform pinning of every particle when the ensemble size grows is a natural stronger question than pointwise finite-n pinning, and the theorem supplies sharp transition scales plus a second-order Gumbel profile. The three alpha regimes expose a genuine phase change at alpha=1/2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
