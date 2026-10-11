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
# Verification

The analytic proof uses the exact characteristic equation and the mixed-boundary spatial eigenproblem. At \(\alpha=0\), the first three dimensionless spatial eigenvalues are \(x\), \(9x\), and \(25x\). The branch-difference function \(G\) is positive at \(x=1/25\), tends to \(-\infty\) as \(x\uparrow1/9\), and has strictly negative derivative throughout that interval. Hence it has exactly one root there. The inequalities \(9x_*<1<25x_*\) prove that precisely two spatial modes can be imaginary at the intersection.

The characteristic derivative cannot vanish at an imaginary root because that would force \(\sin(\omega\tau)=0\), contradicting \(\sin(\omega\tau)=\omega/3>0\). Thus both conjugate pairs are simple.

For positive advection, the substitution \(\phi=e^{\alpha x/(2d)}y\) reduces the spatial problem to \(y''+k^2y=0\) with \(y'(0)=\alpha y(0)/(2d)\) and \(y(L)=0\). The zero-advection spatial roots are simple, so the spatial eigenvalues and Hopf curves vary smoothly. The zero-advection branch intersection is transverse, and the strict mode-separation inequalities persist; the implicit-function theorem therefore yields nearby positive-advection intersections with exactly two imaginary pairs.

The standalone checker `verify_double_hopf.py` uses only the Python standard library. It bisects the zero-advection scalar equation and substitutes the resulting frequencies into the characteristic equation. A successful replay prints `VERIFY_OK`. The numerical calculation is not used to prove existence, uniqueness, or continuation.

Limits: no nonlinear center-manifold coefficients are checked or claimed, and no sharp upper bound on the continued advection interval is asserted.
