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

The analytic verification follows the exact stationary path-ratio score and square-integrable renewal-reward theorem, not finite sampling. The conditional mean of each epoch reward is \((s-1)^2(1-e^{-2\kappa\tau})/(2s)\); the variance and covariance follow from Gaussian fourth moments. Integration against the exponential reset interval yields the stated \(A\) and \(C\), and conditional independence yields \(dA+d^2C\). Strict signs are rational-factor consequences. A stationary path's beginning and unfinished final excursion contribute terms bounded in \(L^2\) at each fixed dimension and hence do not affect linear-in-time cumulants.

Execute `python verify.py` with the packages in `requirements.txt`. The reference checker completed 530 numerical assertions including independent conditional-moment quadrature, regenerative fixed-time sampling and recovery of the known unconfined-Gaussian rate limit. Finite numerical checks are supportive, not proofs of statements quantified over positive real parameters, all dimensions and infinite time. The exact order of limits and the equilibrium \(s=1\) boundary are specified in RESULT.md.
