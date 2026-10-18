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

The documented proof gives an exact finite-dimensional fixed-algebra calculation for all integer dimensions and all positive dephasing rates. The supplied standalone `verify.py` constructs the actual adjacency and Lindblad matrices rather than substituting the proposed fixed algebra into itself. It checks nullspace ranks, parity support, matrix stationarity, finite-time evolution, localized return probabilities, and central-binomial scaling.

Run `python verify.py` in an environment satisfying `requirements.txt`. Numerical propagation at time \(t=500\) is performed only for dimensions \(1\le d\le4\); algebraic matrix checks extend through \(d=6\). These tests are bounded checks, not a proof of convergence for every dimension, every rate, or infinite time. The analytic proof is given in `RESULT.md`, steps 1–5. External independent validation has not been performed.
