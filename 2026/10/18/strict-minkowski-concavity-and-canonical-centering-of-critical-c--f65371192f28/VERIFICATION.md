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

The proof is analytic. For the strictly convex perspective \(P(h,z)=h\log\cosh(z/(2h))\), differentiating twice in \(h\) gives \(z^2\operatorname{sech}^2(z/(2h))/(4h^3)\). The opposite-normal equality test requires positive width in every direction and full support of the surface-area measure. The symmetric-origin Hessian uses \(D(u)>0\) and \(N(u;c)>0\) for all \(u\) and nonzero \(c\). Parity cancels odd powers. These steps, not any finite computation, cover all admissible dimensions, bodies, translations, and levels.

The embedded `verify.py` uses Python 3 standard-library functions only. It was executed from its own file and returned:

```
CRITICAL_TRANSITION_RECENTERING_CHECKS_OK
disk_beta=1, radius_approx= 1.659084806166
quadratic_loss_coefficient_approx= 3.170423103194
finite_difference_losses= [3.1705407218, 3.1708936367, 3.1723061774]
```

The test uses 240 deterministic normal directions and 80 target directions on a unit disk. It checks radial contraction for three nonzero translations, positive perspective curvature at three independent points, strict midpoint interpolation of translated level bodies, and convergence of finite-difference area-loss coefficients toward the analytic Hessian integral. It does *not* certify every direction, every body, or infinitely many dimensions; independent audit has not been performed.
