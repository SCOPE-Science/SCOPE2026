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

The analytic verification reduces the one-particle Hamiltonian to a half-line Jacobi fiber. The boundary equation and bulk recurrence give the decaying root and the exact eigenvalue; the endpoint \(|k|=\pi\) is checked separately. The exact difference between the bulk-band lower edge and the edge eigenvalue is \(2(1-\lambda\cos(k/2))^2/(1+\lambda^2)\), which is positive for \(0<\lambda<1\) and all \(k\in[-\pi,\pi]\).

The accompanying script checks recurrence residuals and the separation identity at a finite grid of parameter values. It is a consistency check only, not the proof of the quantified statement. The fiber eigenvectors are normalizable in the normal direction but not along the infinite boundary. No independent audit or independent validation is claimed.
