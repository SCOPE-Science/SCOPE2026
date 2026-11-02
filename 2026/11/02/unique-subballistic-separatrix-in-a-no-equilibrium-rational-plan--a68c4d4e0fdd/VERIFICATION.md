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

# Verification and limits

The proof in RESULT.md establishes existence, uniqueness and the infinite-time scaling analytically. Run `python3 verify.py` with standard Python 3: it checks twelve exact rational conjugacy iterates; identifies two distinct orbit classes numerically; and compares finite-horizon near-separatrix solutions with the predicted \(n^{2/3}\) and \(n^{-1/3}\) coefficients at three horizons. All these checks were executed successfully. The shooting estimates depend on the finite-horizon target \((1-u)^2y=2a/d\) and are not claimed as certified values of the infinite-horizon separatrix. No independent mathematical validation has been performed.
