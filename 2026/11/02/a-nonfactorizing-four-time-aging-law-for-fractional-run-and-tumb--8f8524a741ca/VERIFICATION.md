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

# Reproduction and mathematical limits

The analytic steps are given in `RESULT.md`: Poisson sign parity, inverse-stable self-similarity, stable crossing-overshoot density obtained from potential and Lévy densities, and a complete strong-Markov decomposition of two disjoint observation intervals. That argument proves the universal limiting formula and strict connected-memory example. No finite experiment is used as proof.

Run `python verify.py` after installing `requirements.txt`. The script checks the arcsine pair-probability identities, independently evaluates the one-dimensional overshoot integral using incomplete-beta functions, and simulates the half-stable forward process through exact, independent subordinator increments with a shrinking operational-time mesh. The recorded sample count, mesh and seed are in the script; its tolerances reflect finite-sample and grid errors. The integer-grid numerical example is diagnostic; no exact closed form for the full four-point probability is claimed.

The construction does not furnish uniform convergence in the four time ratios, finite-sample confidence bounds, or an independent audit. A possible broader implication from stable-regenerative interval-partition theory remains an originality limitation.
