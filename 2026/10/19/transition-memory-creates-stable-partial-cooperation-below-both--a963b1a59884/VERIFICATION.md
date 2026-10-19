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
Run `python3 verify.py` with a standard Python 3 interpreter to reproduce numerical root locations, gain-coefficient identities, stationary environmental probabilities, boundary and interior signs, the sharp-criterion inequalities and finite-size spot checks. The proof of the all-group-size monotonicity obstruction is symbolic, using strict convexity of powers and the derivative identity for Bernstein polynomials. The witness uses strict elementary logarithm bounds, so no floating-point comparison is necessary for theorem validity. The code is corroborative, not exhaustive verification over arbitrary positive real parameters.

The stochastic finite-hypergraph process described in the motivating paper is not covered by the theorem. An independent scientific audit has not been performed.
