---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Strict positive definiteness K=[[a,c],[c,b]] and contracting coordinate resets give a quadratic Lyapunov drift and Wasserstein contraction, ensuring a unique stationary law with second moments. Generator on X²,Y²,XY yields a nonsingular linear system (2a+(1+θ)p)u+2cw=2D_x, 2bv+2cw=2D_y, c(u+v)+(a+b+p)w=0, p=r(1−θ), with positive determinant Δ=4(a+b)δ+2p[2ab+(1+θ)δ+(1+θ)b²]+2b(1+θ)p². Cramer algebra gives M=c(u−v)+(b−a)w=(2c/Δ)[4δ(D_x−D_y)+2p(bD_x−(a+b(1+θ))D_y)−(1+θ)D_y p²]. The numerator factors by (4δ+2bp)(D_x/D_y−q*(p))D_y and q* derivative has positive numerator 8δ[a+bθ+(1+θ)p]+2b(1+θ)p². As q*(0)=1 and q*(∞)=∞, there is one threshold only for hotter X. Independent symbolic 3×3 inversion/determinant and torque factor checks succeeded. These algebraic identities yield universal signs; no Gaussian stationary-law assumption or finite-sample extrapolation.

## originality

PASS

No-reset harmonic gyrator torque and coordinate-resetting moment methods are known. Closest inspected work on one-coordinate/velocity resetting assumes spatial translation covariance and on shear resetting uses unconfined driving; their results do not directly give the exact strictly confined OU conservative-torque phase boundary. Mechanism-specific earlier literature remains a possibility.

## value

PASS

A complete necessary-and-sufficient reversal criterion, monotone temperature-ratio boundary, and explicit unique intervention rate are natural for nonequilibrium stochastic control. It separates a nontrivial reset-driven sign transition from other magnetic/shear torque mechanisms while specifying exactly the observable (conservative torque), not claiming thermodynamic efficiency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
