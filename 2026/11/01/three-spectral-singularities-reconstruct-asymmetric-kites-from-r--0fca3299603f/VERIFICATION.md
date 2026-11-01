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

# Reproducible checks and limits

Run `python verification_code.py` after installing the dependencies listed in `requirements.txt`.

The program independently compares support-function and piecewise width values on an angular grid for five kite parameter sets, integrates the exact density across all active branch thresholds to check total probability mass, checks the three distinct inverse-square-root singularity amplitudes at successive shrinking offsets, and reconstructs \(r=17/10\), \(p=1/4\), and \(q=3/2\) from the observed critical heights.

Its successful run reports `ALL_CHECKS_PASSED`. For five test shapes, density integrals differed from unity by less than \(10^{-8}\); the finite-offset singularity checks converged to \(2/\pi,4/\pi,2/\pi\). These checks are not exhaustive and do not certify any of the infinitely many untested parameters. The full proof is analytic in `RESULT.md`. No separate independent audit has been performed.
