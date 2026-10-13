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

Reproduce the exact rational checks with `python verify.py` in a standard Python 3 environment; no external packages are needed. The script checks 128 sampled two-site closure criteria across grid positions and contractive multipliers, 726 exact shared-uniform coupling identities, 16 balance and variance identities for the quarter-cell phase, and 3 finite-horizon distribution diagnostics: 873 assertions in total. These counts refer to exact arithmetic tests; no source papers or internet access are needed to run the script.

The infinitely many initial states and all real parameters are addressed by the analytic proof, not finite sampling. The \(W_1\) contraction uses coupled uniform variables only for comparison; it does not change the independent uniforms defining each chain. Convergence of second moments follows from the deterministic trajectory bound. The strict off-threshold inequality depends on both Bernoulli states having positive mass and on positive one-step probability of leaving that support.

The demonstration uses an ideal, once-rounded exact affine update to a uniform infinite lattice. The result is not a certificate for implementation-specific floating-point behavior. Scientific results have been checked within the same model; independent audit remains unperformed.
