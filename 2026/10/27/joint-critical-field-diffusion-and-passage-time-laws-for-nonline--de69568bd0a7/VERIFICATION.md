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
# Verification and limits

The attached `verify_critical_qvoter.py` was executed with Python 3, NumPy, and SciPy from the packaged source. It passed 368 direct finite-state detailed-balance identities, 60 generator coefficient comparisons, 12 stationary density moment comparisons, and 18 mean passage-time comparisons in both directions (458 checks in total). For fixed \(q\) and perturbations \(\theta,\eta\), convergence of the analytical limit is established separately in the proof. The test code verifies finite examples and numerical quadratures, not infinite limit theorems.

The exact finite chain uses exclusion of the focal voter from neighbor sampling and samples the remaining voters with replacement. It checks the effect of integer rounding of zealot counts. The convergence statements assume a fixed finite \(q\) and fixed finite critical parameters. In particular, a finite state computation cannot independently certify novelty, rigorous stochastic tightness, or generality beyond these assumptions.

To reproduce, install `requirements.txt` in a suitable Python 3 environment and run `python verify_critical_qvoter.py`. No random seed is needed: the checks use deterministic calculations. Scientific publication and independent validation require separate assessment.
