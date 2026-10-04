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

The packaged symbolic checker verifies the equilibrium quadratic, the general characteristic polynomial, the Routh-Hurwitz obstruction on the lower positive-root branch, and the exact invariant-measure variance factorization.

At the published parameter set it verifies \(x_+=\sqrt3-1\), \(x_-=-\sqrt3-1\), and \(y^2=2\sqrt3\). It reconstructs the positive-\(y\) spectrum as approximately \(3.97838806144\) and \(-0.127984312514\pm2.5428456801i\), matching the source values. It also evaluates the source's printed point \((0.7321,3.4641,0)\) in the displayed equation \(x^2+y^2-4=0\) and obtains residual approximately \(8.53595922\).

The checker is algebraic; it does not validate the existence, basin, entropy, or Lyapunov exponents of the numerical chaotic attractor.
