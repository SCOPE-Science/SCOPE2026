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

# Verification and reproducibility

The analytic argument in `RESULT.md` establishes the monomial diagonalization, strict eigenvalue ordering, uniformly Gaussian-concentrated radial moments, the quantitative saddle tracking bound, mesh density of the saddle radii, and the iff relation between spectral and geometric limits. The weight hypotheses imply \(m\leq\Phi'(r)/r,\Phi''(r)\leq M\), and every assertion is for fixed \(\beta>0\).

Run `python verify_radial_weyl.py` in an environment with Python 3, SciPy and NumPy-compatible numerical primitives (SciPy suffices for the script). Expected terminal marker: `RADIAL_FOCK_WEYL_MOMENT_CHECKS_OK checks=20`. The computation uses centered quadrature for \(n=40,100,400,1600\) on three explicit weights and checks the saddle relation against moments. No external data or other files are required.

The numerical checks do not prove the infinite-dimensional assertions, the sharp cluster interval, or global originality. Those conclusions rely on the stated analytic argument and literature comparison. Independent review has not been performed.
