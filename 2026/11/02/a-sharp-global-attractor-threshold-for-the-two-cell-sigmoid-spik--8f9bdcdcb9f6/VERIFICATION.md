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
The rigorous check consists of the explicit matrix norm identity, the scalar bound \(u(1-\tanh u)\le e^{-1}\) for \(u\ge0\), the lower bound on \(z\cdot(M\Theta_\alpha(z)+b)\), and the closed radial drift inequality at \(T=2\). For \(T>2\), verify the exterior radius and expanding factor directly from the reverse triangle inequality; for \(0<T<2\), verify the affine norm recurrence. The global-attractor construction uses nested compact images of a forward-invariant absorbing ball, not finite simulation.

Running `python3 check_bounds.py` (Python 3 standard library only) reproduces the coefficient identity checks and 1,050 seeded finite-state numerical assertions over representative values from each parameter regime. These checks passed on the accompanying source file. They cannot prove the quantification over all real states and parameter values, which rests on the written inequalities. There is no external or independent validation represented.
