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

The archived `check.py` script was executed on the packaged path with NumPy and SciPy; 204 numerical consistency checks passed. It builds the full flux-threaded diamond-chain Hamiltonian, verifies the reduced tridiagonal backbone operator, and compares mean survival integrals from two independently implemented finite Lyapunov equations. It also checks the approach to the sharp claimed coefficient for several finite lengths and sink strengths. These checks do not prove a theorem for arbitrary length or certify historical originality. The analytic argument, including the nondecaying-mode exclusion and perturbative damping coefficient, is in `RESULT.md`.
