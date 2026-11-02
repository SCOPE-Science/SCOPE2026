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

# Verification

The companion self-contained Python standard-library script is `check.py`. Run `python check.py` with a supported Python 3 interpreter. Its fixed-seed checks produced the message:

`PASS: 23700 independent numerical identities, perturbation inequalities, and Gaussian moment tests`

It exercises 90 discretized scalar plants with nonconstant affine drift and actuation profiles and three arbitrary actuator-on geometries; compares their unique shaped optimizers against the exact period contraction; checks the complete-square slack on 900 perturbed candidate holds; independently evaluates 300 constant-hold gain problems, hyperbolic identities, and competing constant gains; and checks ten Gaussian second moments directly by simulation. These computational checks only corroborate the analytic Itô-isometry, Cauchy–Schwarz, and completing-the-square proof. They are not a formal or independent proof for infinite-dimensional waveform classes, all real parameters, or all stochastic trajectories.

The documented prior-literature comparison concerns mathematical statement implication, not a guarantee that an older equivalent result does not exist. Results are self-reviewed; independent audit has not been performed.
