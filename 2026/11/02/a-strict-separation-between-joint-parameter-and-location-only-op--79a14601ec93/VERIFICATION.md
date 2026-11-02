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

The accompanying standard-library `verify.py` replays the independent three-by-three Poisson Fisher matrix construction for 220 sets of exact rational parameters; this checks the determinant identity without using the simplified determinant expression to build the matrix. It tests the Fisher nuisance orthogonality for symmetric wing exposures, the location efficient-information formula, 1,000 independent central-difference derivative comparisons, 400 random positive-background root and objective comparisons, background monotonicity, the beta-one illustrative figures, and exposure arithmetic–geometric mean inequalities. The expected successful output is `VERIFY_OK assertions=16105`.

These are finite consistency checks, not a substitute for the proof of uniqueness, optimality, or limiting regimes. The proof is in `RESULT.md`, where the logarithmic derivatives are shown to be strictly decreasing for every positive parameter. The comparison with earlier literature is provisional, and external independent audit has not been performed.
