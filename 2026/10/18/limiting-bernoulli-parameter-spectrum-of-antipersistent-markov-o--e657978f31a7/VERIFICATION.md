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
Run `python3 verify.py` with Python 3 and no third-party dependencies. The program verifies stationary Markov path probabilities against the recurrence with exact rational fractions. It independently counts negative zeros via the recurrence on a dense numerical mesh for five parameter/horizon combinations, then compares the empirical spectral CDF against the angle law at five interior quantiles per combination.

Finite root finding and rational tests are limited in scope: numerical sign scans cannot exclude all potential missed roots without the separate analytical strict-interlacing proof. The complete infinite-horizon weak limit is established in `RESULT.md` by the root-counting phase argument. The spectral density integrates to one because its CDF is \(\theta(t)/\pi\) with endpoints \(0\) and \(1\). Results, including possible floating-point error, should be interpreted within the printed checks.

Independent audit remains unperformed.
