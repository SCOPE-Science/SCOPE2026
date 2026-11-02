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

# Reproducibility and limitations

Run `python3 verify.py` with SymPy and mpmath installed. The checker verifies exactly (symbolically) the two-monomer relative eigenmode, jump and diffusion second-moment rates, stationary fourth cumulant, and the backward differential identity for the Gaussian mean first-exit function. Its 50-digit quadrature checks the Gaussian integral and endpoint leading coefficient at four restoring rates. A seeded 10,000-path, jump-time-exact simulation at zero thermal diffusion compares samplewise rupture times at four restoring rates and checks the pathwise domination by a first jump larger than twice the threshold.

This program is a reproducibility aid and does not independently certify the scientific theorem. The all-parameter almost-sure coupling, moment convergence, and comparison limit are proved analytically in `RESULT.md`; the experiments are finite and cannot replace them. The main proof also holds at nonzero thermal diffusion, although its event-driven simulation deliberately uses the zero-diffusion subcase. Scientific priority is not independently validated.
