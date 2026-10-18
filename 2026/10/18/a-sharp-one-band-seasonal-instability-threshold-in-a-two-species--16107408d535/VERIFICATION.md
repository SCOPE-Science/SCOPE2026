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

# Verification of the seasonal-instability classification

The standalone Python 3 standard-library program `check.py` is supplied with this result. Run `python check.py` without supplementary files or third-party packages. The program evaluates 25 rational examples of the nilpotent matrix exponential identity and 1,600 independent high-precision eigenvalue checks across positive parameter values and duty shares. It also computes the unique universal solution of \(w\tanh w=1\), verifies two transition periods, checks the duty-boundary values, and verifies stable–unstable–stable Floquet exponents at three sample periods.

The mathematical proof is independent of these finite checks. In particular, positivity and boundedness follow from the comparison estimates in RESULT.md, the exact monodromy follows from the nilpotent structure, and the uniqueness of the instability band follows from strict monotonicity of \(w\tanh w\). The checker tests numerical formulas and does not establish any claim about nonlinear bifurcation or stability on the negative-unit-multiplier boundary.

The supporting primary literature and unresolved full-text access limitation are recorded in REVIEW.md and AUDIT.json. No independent scientific audit has been carried out.
