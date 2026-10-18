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

Run `python verify.py` with Python 3 and SymPy. The checker symbolically validates the generalized three-cycle characteristic polynomial and its specialization, checks invariant row and column sums, and evaluates representative positive-rate chains against the claimed activity, real-spectrum coefficients and edge-current expressions. The checker reports a count of passing assertions.

Critical identities independently proved in RESULT.md are the characteristic polynomial, the fixed pairwise-rate invariant, positivity of all directed rates, the stationary current formula and the logarithmic divergence. A finite set of tests is not an exhaustive proof. The intermediate value theorem, not the tests, supplies every target entropy-production value. The rate at the open endpoint is never claimed to be a valid strictly positive-rate chain. No independent audit has been performed.
