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

The finite checker `verify.py` separately calculates the maximum signed-antichain support by brute-force enumeration and by bottom-up dynamic programming on small complete rooted trees. It uses 158 independently drawn Gaussian direction inputs across four branching/height cases; it also tests the half-normal exponential moment constants and prints Monte Carlo diagnostics for small heights.

The infinite-height proof depends on the Gaussian support identity, the expectation recursion, leaf domination, an explicit exponential-integrability bound, Gaussian Poincare concentration, and Gaussian radial normalization. No experimental threshold or sample mean is treated as an exact asymptotic or a proof of originality.

The recursively defined constant has the analytic upper bound on its uncomputed tail stated in RESULT.md. The internal geometric statement assumes fixed branching degree. No external independent audit or formal certification was performed.
