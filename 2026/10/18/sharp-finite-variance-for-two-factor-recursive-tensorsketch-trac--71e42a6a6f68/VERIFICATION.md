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

# Reproducibility and independent audit status

Execute `python verify_recursive_tensor_variance.py` in a Python 3 environment with NumPy. The code recomputes the exact rational modular-difference collision identities for 79 widths, checks the uniform-factor variational extremum for 29 widths and 10 factor dimensions with 10 random perturbations per case, and simulates the actual three independent layers (two leaf CountSketch hashes and one internal TensorSketch) in 8 configurations.

Observed execution: PASS, 395 exact modular checks; 3190 finite extremal checks; 8 direct independent Monte Carlo settings. The deterministic tests include both odd and even widths, including one bucket. Gaussian-style finite statistical checks here are Rademacher sketches, not infinite-dimensional certificates. The complete universal claim is established by the mathematical proof in RESULT.md; the reproduction program tests finite instances only. No independent audit has been performed.
