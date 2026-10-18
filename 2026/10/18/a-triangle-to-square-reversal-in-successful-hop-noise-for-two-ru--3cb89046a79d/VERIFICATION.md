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

# Reproducible verification

Run `python verify_activity.py` with a Python environment having SymPy installed (`requirements.txt`). The checker constructs the symmetry-reduced event-count matrices directly from local transition rules, verifies the asserted mean and Fano formulas symbolically, and checks the strict-sign, derivative and limiting identities. It also independently constructs the complete labeled relative-state generator (8 states for the triangle and 12 for the square), solves its stationary and Poisson equations exactly at five rational reversal rates per ring, and compares ten full-generator results against the symbolic formulas.

The full-state rational comparisons are finite tests; the symbolic finite-matrix identities, strict polynomial inequalities, and Descartes-root argument constitute the all-positive-rate proof. The tests do not establish novelty or any infinite-ring generalization. Independent scientific audit has not been performed.
