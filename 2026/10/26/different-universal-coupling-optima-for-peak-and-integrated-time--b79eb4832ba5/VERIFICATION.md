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

Execute `python3 verify.py` in the directory containing the supplied files, with Python 3 and SymPy installed. The expected output is included in `verification_output.txt`; 113 assertions pass.

Tests reconstruct the exact stationary Lyapunov equation, matrix exponential, antisymmetric two-time covariance, derivatives and dimensionless scaling, and 25 deterministic parameter comparisons. The analytical arguments in RESULT.md separately establish existence, strict uniqueness, and ordering of global maxima; no finite checker implies those facts. The calculation excludes equal reservoir temperatures and assumes unit mobility, stable positive coupling, equal trap stiffnesses, and stationary initialization. The optimizer is not asserted to be optimal for signal-to-noise ratio under finite-time sampling.

Primary literature for the model and generic covariance equations is cited in RESULT.md. Independent audit and independent validation have not been performed.
