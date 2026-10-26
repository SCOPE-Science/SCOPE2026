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

# Reproducible mathematical checks

Use Python 3 with NumPy and SciPy. From the same directory, execute `python verify.py`. The script seeds its finite randomized tests for reproducibility and prints a final PASS line on success.

The code checks 256 independent positive-rate samples through even moment order 25, reconstructs six stationary generator moment grids, simulates five piecewise-deterministic physical trajectories with exponential holding times and exact flow between jumps, tests the latent two-Beta/Bernoulli phase moments and strict sampled radial ordering, and compares twenty independent Gauss–Jacobi and hypergeometric evaluations of the conditional near-wall tumble probability.

These computations check formulas and behavior at selected finite parameters and thresholds. They are not an exhaustive search over continuous rates, are not an infinite proof, and do not independently certify novelty. The universal results follow from the compact-support moment proof, strict Beta-density likelihood-ratio order, and the exact conditional product integral supplied in RESULT.md.
