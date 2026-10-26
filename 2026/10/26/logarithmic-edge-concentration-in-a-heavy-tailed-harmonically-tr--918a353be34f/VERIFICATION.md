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

Run `python3 verify.py` with a NumPy installation. A deterministic random seed is fixed in the script. The program iterates the exact affine switching map, constructs independent stationary ages from the known equilibrium age distributions, and tests the exact finite-threshold identity against direct stationary sampling. It also evaluates the tail constants at logarithmic distances without relying on rare-event event counts. The completed run reported 24 passing numerical comparisons: four Lomax residence exponents and one half-\(t\) residence law.

The analytical proof uses stationarity and contraction, an exact age-conditioned probability identity, an entrance-gap probability inequality, tail integration, dominated convergence, and a reciprocal-moment tail integral. The finite script does **not** certify these universal steps, prove an infinite-time limit or establish originality. The stopping-time and inverse-moment statements are mathematical conclusions under the precise hypotheses, not claims of experimental observability at arbitrarily small distances.

No independent audit or external validation has been performed.
