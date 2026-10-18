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

# Reproducibility and verification

Run `python verify.py` with Python 3.9 or later; only the standard library is required.

The verifier independently constructs all labelled simple graphs of orders \(3\) through \(6\), computes the isolated-two-vertex-component count and triangle-free-edge count from adjacency matrices, and evaluates their exact joint moments at five rational edge probabilities. It compares the exact covariance to the formula in `RESULT.md`; no Monte Carlo approximation enters these checks. It also verifies the stated finite-size rational peak witnesses for a range of orders and checks inequalities used in the all-order proof. The replay passed 454 deterministic assertions.

The verifier is finite: it does not establish the infinitely many orders or real parameter values. Those quantifiers are covered by the exact mixed-moment argument, the strict-log-derivative unimodality proof, and scaling bounds in `RESULT.md`. Numerical root values are not used as proof certificates. Historical priority and independent validation have not been certified.
