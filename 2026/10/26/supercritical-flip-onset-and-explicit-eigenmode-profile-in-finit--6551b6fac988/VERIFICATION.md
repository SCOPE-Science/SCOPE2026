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

The analytic proof covers every finite path length; no infinite certificate is claimed. The included `verify.py` uses ordinary floating-point calculations and a direct Newton solve of the exact antipodal orbit equation for \(N=1,\ldots,10\), at \(h-h_N=0.00005,0.0002,0.0008\). It checks the residual of \(G_h(\pi\mathbf1+x)=\pi\mathbf1-x\), the leading amplitude projection, and all eigenvalues of the similar symmetric local Jacobian for stability. Reproduce using `python3 verify.py`. The execution performed here produced `VERIFY_OK 30 parameter cases` without exceptions. This is finite corroboration only; the implicit-function and spectral arguments establish the infinite theorem. The numerical Jacobi diagonalization is not a rigorous interval eigenvalue certificate. No independent audit has been performed.
