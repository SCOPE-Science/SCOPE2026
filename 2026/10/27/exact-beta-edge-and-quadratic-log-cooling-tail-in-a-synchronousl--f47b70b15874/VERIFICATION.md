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

Run `python verify.py` with NumPy and SymPy available. The standalone checker passes 66 deterministic and symbolic assertion groups: exact variance and inversion algebra, four independent parameter sets of 160,000 sampled stationary perpetuities with 130 iterations each, exact theoretical second-moment comparisons, two probability threshold checks in the full beta-edge interval for each parameter set, six successive generator-moment identities per set, and finite-size positive-variance identities. The normalized perpetuity truncated after 130 iterations differs from its stationary coupled version by at most \(c^{130}\), where \(c=q^2\). Sampling error is checked only within the program's stated tolerances.

The stationarity and uniqueness, exact beta tail, the quadratic-log lower-edge limit, and the population-limit claims are established analytically in `RESULT.md`, not by simulation. The lower-edge assertion requires asymptotic iteration of exact distributional inequalities; finite samples would not prove the infinite limit. There is no claim of independent scientific auditing.
