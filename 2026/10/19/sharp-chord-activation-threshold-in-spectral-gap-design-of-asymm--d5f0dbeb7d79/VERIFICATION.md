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

# Verification instructions

Install Python 3 with SymPy and run `python verify.py` in the directory containing this file. Observed output: `VERIFY_OK 699 exact rational certificate, edge, derivative and spectral checks`.

The script tests exact rational centering, the four-level eigenvector, the saturated budget, the semidefinite dual witness's trace and threshold inequalities, transverse eigenmodes, and a strict feasible budget-preserving perturbation on both sides of the phase boundary. For eight selected graph orders it computes all distinct weighted Laplacian eigenvalues exactly and checks the spectral ordering.

These computations are finite corroboration, not an infinite-family proof. The algebraic derivation, the grounded matrix interlacing argument, and the strict-perturbation proof in RESULT.md provide the general justification. The exterior-regime optimal value is not determined. No independent audit or external certification has occurred.
