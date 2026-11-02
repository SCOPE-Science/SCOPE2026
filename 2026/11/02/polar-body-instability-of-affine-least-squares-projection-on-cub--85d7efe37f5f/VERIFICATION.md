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

Unpack the embedded `verification/check.py` file and run `python verification/check.py` with Python 3 and NumPy installed. The actual packaged program passed 114 assertions: 102 exact-rational beta-marginal, covariance, Irwin–Hall polynomial-integration, and special-value comparisons, followed by 12 stochastic sanity checks. Printed examples are cross-polytope \(10561/4000\) and cube \(415/162\) in dimension three.

The complete theorem is a mathematical proof, not a claim of exhaustive numerical verification. Universal maximizer rigidity uses a positive-volume opposite-sign neighborhood between any two different vertices, and the cube asymptotic uses the central limit theorem plus uniform integrability. The finite checker cannot independently establish either. The checker uses only reproducible in-package source and standard NumPy sampling; no external private files or services are required. No independent audit has been performed.
