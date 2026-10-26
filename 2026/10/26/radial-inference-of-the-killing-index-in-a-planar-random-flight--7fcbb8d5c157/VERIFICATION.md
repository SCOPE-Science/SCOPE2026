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

# Reproducibility and verification boundaries

The separately included `verify_posterior.py` uses Python 3 with NumPy and SciPy. Run `python verify_posterior.py` from the directory containing the script. The accompanying `verification_output.txt` records the actual completed run.

The program independently checks radial normalization of several Gamma–normal variance-mixture densities; agreement between a 220-term geometric count-density sum and the Bessel resolvent plus positive subordination-kernel integral on a parameter grid; strict sample likelihood-ratio inequalities for index pairs; and convergence of exact finite posterior moments toward the proved linear-plus-constant asymptotics. It executed 275 finite checks successfully.

The finite checks do not establish the universal monotonicity statement or the infinite-radius Gaussian theorem. Their verification is analytic: monotone likelihood ratios of the Gamma posterior mixing measures prove ordering, and a locally uniform complex-neighborhood Bessel/resolvent expansion proves cumulant convergence. Reproduction also depends on accurate implementations of the standard special functions in SciPy; numerical quadrature tolerances and the sum cutoff are specified in the code. No independent audit or externally certified verification is represented here.
