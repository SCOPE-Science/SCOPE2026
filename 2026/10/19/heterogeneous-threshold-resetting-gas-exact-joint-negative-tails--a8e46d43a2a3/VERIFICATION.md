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
# Reproducibility and mathematical limits

A direct derivation in `RESULT.md` proves the exact stationary joint left-tail scaling through an explicit killed-Brownian Gaussian integral, the finite-mean renewal formula, an integrable dominated-convergence envelope, gamma integration, and the tail integration identity. The proof's assumptions require fixed \(N\ge3\), positive diffusivities, positive upper reset thresholds and nonzero positive relative left-tail depths.

Run `python verify.py` with NumPy and SciPy to numerically integrate the independently parameterized renewal survival integrals and finite-scale event probabilities. Checks cover heterogeneous four- and five-particle settings, several tagged-index sets, two distinct choices of reset levels at fixed diffusivities, and comparison of conditional pair-coefficient ratios against their algebraic value. Computations at finite radius corroborate the asymptotic constants, but finite-radius quadrature does not prove the limit or rule out unobserved numerical errors. The rigorous limit is the dominated-convergence argument in the main proof.

The source's homogeneous stationary density and its renewal form are prior work, not new. Originality assessment considered the stated heterogeneous claim, not merely a changed notation. Possible inclusion under broader regenerative-mixture or multivariate regular-variation theorems remains a literature-completeness risk. No independent audit or external certification has been performed.
