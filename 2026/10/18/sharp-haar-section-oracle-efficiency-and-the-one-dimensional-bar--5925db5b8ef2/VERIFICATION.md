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

Execute `python3 verify.py` using a standard Python 3 installation. No third-party packages or external network connection are needed. The script tests the dimensional-constant identity exactly with rational arithmetic; numerically integrates the rank-one angular formula; checks the upper and lower expected-efficiency bounds using reproducible orthonormalized Gaussian frames; and evaluates a discrete circular Dirichlet inequality for sample frames.

The script completed 433582 finite checks with seed 260524. Numerical sampling is subject to statistical tolerance, quadrature discretization, and floating-point error, and does not prove the expectation bounds or the sharp infimum. Those results follow from the norm identity, Fourier/Parseval comparison, Haar conditional rotational invariance, and dominated convergence in `RESULT.md`. The one-dimensional waiting law additionally relies on independent fresh line samples and exact minimization. Independent audit has not been performed.
