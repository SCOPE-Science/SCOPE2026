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

The bundled `verify.py` reconstructs the positive equilibrium from the printed nonlinear equations at the stated numerical parameters, then differentiates the same formulas to obtain the six linear coefficients. It forms \(P,Q,R\), solves the exact imaginary-frequency quadratic in \(z=\omega^2\), checks that exactly one root is positive, reconstructs the principal phase, and verifies the characteristic equation at \(\lambda=i\omega_*\).

It then evaluates the implicit derivative \(d\lambda/d\tau_1\) and checks its real part is positive. Zero-delay stability is checked from \(P>0\) and \(Q+R>0\); the absence of a zero eigenvalue follows from \(\Delta(0,\tau_1)=Q+R\). Finally, the calculation is repeated with the source's rounded equilibrium \((0.1219,0.5702)\) to show that rounding produces \(4.874589989058015\ldots\), not \(4.5923\).

The verifier is a finite high-precision reconstruction of the printed linear calculation. It does not certify nonlinear Hopf criticality or any two-delay stability boundary.
