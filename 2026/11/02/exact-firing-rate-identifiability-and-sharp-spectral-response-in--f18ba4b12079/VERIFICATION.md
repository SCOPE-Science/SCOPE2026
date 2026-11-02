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

# Verification record

The full analytical proof is in `RESULT.md`, with primary theorem assumptions and explicit rank/positivity, Jacobian, spectral, and scalar-optimization steps. A standalone replay command is `python CHECK.py` with NumPy and SciPy available. The saved `CHECK_OUTPUT.txt` records 1,460 deterministic passing checks from that script. Tested cases include both graph parity types, heterogeneous positive rate vectors, varying weak-reinforcement exponents, and both finite-size and continuum spectral formulas.

Numerical equilibrium solutions and small finite tests do not certify conclusions for all rates, graph sizes, or exponents. These conclusions are supported by the mathematical proof and Qin's stated positive-equilibrium uniqueness theorem. The present review is not an independent mathematical audit and does not establish definitive literature priority.
