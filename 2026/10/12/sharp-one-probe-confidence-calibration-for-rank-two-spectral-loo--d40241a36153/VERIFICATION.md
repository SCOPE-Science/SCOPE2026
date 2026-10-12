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

# Reproducibility and limits

Run `python verify.py` using Python 3 with only the standard library. The program constructs rational two-dimensional projected norm-squares directly; checks their spectral bounds and equality with the closed form; certifies the rational polynomial square identity on a finite parameter grid; checks eight numerical inversions of the exact confidence formula; and compares 510,000 seeded Gaussian samples with the analytical Cauchy probabilities. The run output is:

`VERIFY_OK exact_rational_matrix_identities= 3584 exact_rational_sharpness_identities= 171 calibration_cases=8 monte_carlo_trials= 510000 frequency_pairs= [(0.25, 0.0204, 0.02054), (0.5, 0.091318, 0.091258), (0.75, 0.255918, 0.255952)]`

The theorem for every real rank-two matrix, every threshold, and every admissible singular-value ratio depends on the analytical SVD, Gaussian/Cauchy, and square-completion proof in `RESULT.md`, **not** on the finite calculations or random trials. This verification does not claim independent audit, higher-rank results, full adaptive-algorithm guarantees, or floating-point guarantees.
