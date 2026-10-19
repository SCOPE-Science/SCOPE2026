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

# Reproduction and limits

Use Python 3 and SymPy to run `python verify_landscape.py` in this directory. The script checks the explicit critical-coordinate formulas, determinant-multiplier identities, saddle height, equality-boundary fourth-order coefficient, the positive-definite operator spectrum in several exact rational dimensions, and direct rational rank-one objective values. Success terminates with a `PASS` message. The accompanying proof, not any finite computation, establishes universal parameter coverage, stationary-point exhaustion, and the minimax path barrier.

The spectral ratio \(\kappa\) and the full-rank-two forcing \(F\) are exact. No stochastic experiments, numerical root searches, or external source files are necessary. Scientific self-review is reported separately; no independent audit has been performed.
