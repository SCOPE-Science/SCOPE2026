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

# Reproducible checks and limits

Run `python3 verify.py` with SymPy installed. It uses exact symbolic algebra to verify the Jacobian trace/determinant, the full coordinate-transformed ODE, the second-harmonic equations, the cubic resonant Fourier projections, the nondegenerate complex Hopf coefficient from an separate algebraic normalization, and the square identity showing a sharp universal minimum.

For fixed \(s\in(0,1)\), the amplitude expansion is an analytical consequence of the nondegenerate supercritical Hopf theorem, not a consequence of finite testing. The checker confirms algebraic premises only and does not formally prove the Hopf theorem or historical originality. Representative ODE shooting at \(s=0.5\), \(1/\sqrt3\) and \(0.85\) for \(\mu=0.001\) and \(0.003\) corroborates convergence of measured normalized period slopes to the derived coefficients. These finite experiments are supporting evidence, not a substitute for the local analytic proof. No global large-cycle or uniform-in-parameter theorem is claimed.
