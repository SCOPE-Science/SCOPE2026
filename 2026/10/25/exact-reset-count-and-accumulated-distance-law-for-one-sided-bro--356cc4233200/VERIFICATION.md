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

# Verification and reproducibility

Run `python verify.py` from the directory containing this file; NumPy is the only nonstandard dependency. The program checks (i) the two-region backward-equation solution, derivative matching and boundary normalization for several positive parameter configurations, (ii) geometric and exponential mixture probability identities and conditional Poisson normalization, and (iii) a direct trajectory Monte Carlo simulation at three monitoring rates. The direct simulation draws physical Poisson monitoring gaps, Brownian Gaussian increments and exact Brownian-bridge target-crossing probabilities; it does not sample from the geometric/exponential theorem to manufacture agreement. Assertions compare reset-free probabilities, reset counts, mean reset depths, cost moments, Laplace transforms and positive cost tails.

**Limits of finite evidence.** Statistical agreement is subject to Monte Carlo uncertainty; finite experiments cannot establish a formula for every positive parameter choice. The analytic proof in `RESULT.md` supplies the universal statements. Numerically finite trajectories do not directly verify the singular limit \(r\downarrow0\), which follows from the exact mass \(\Pr(C>0)=q\). No independent scientific audit or validation has been performed.
