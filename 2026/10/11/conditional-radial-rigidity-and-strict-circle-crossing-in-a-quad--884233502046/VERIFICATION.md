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

# Verification and boundaries

The exact vector field, \(\Phi=z-dx^{2}/(2a)\) and \(\Psi=xz-dx^{3}/(3a)\) are defined in RESULT.md. With SymPy installed, run `python3 verify_radial.py` from this directory. A successful run prints `VERIFY_OK`. The script expands the full Lie derivatives for symbolic \(a,b,c,d,r\), verifies their cancellations, checks the published parameter specialization, and checks both the planar Hamiltonian and its local minimum for the periodic example.

**Analytical checks.** Flow invariance of a compactly supported probability implies integration of exact derivatives against the measure is zero. Applying this to every differentiable scalar function of \(\Phi\) establishes \(\mathbb E[R^{2}\mid\Phi]=r^{2}\) almost surely; integrating the derivative of \(\Psi\) gives the covariance identity. If the invariant support has \(z=0\), the vector field forces \(R^{2}=r^{2}\) throughout that support. Combining this equality case with the fixed radial second moment proves positive measure both inside and outside the equilibrium circle for non-equilibrium stationary states. Integrating \(\dot\Phi\) gives the finite-time bounded-orbit identity without assuming ergodicity.

**Limits.** The symbolic checker is not an independent mathematical audit and does not establish any infinite-time convergence numerically. The existence of chaotic recurrence at the source's numerical coefficients is not proved. The bibliographic originality assessment retains a documented uninspected full-text risk.
