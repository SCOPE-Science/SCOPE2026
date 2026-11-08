---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For constant a>0 and an even periodic uniform P1 DG mesh, the exact weak-form operators are F_A=-(a/dx)(A+B-A_- -B_-), F_B=(3a/dx)(A-B-A_- -B_-), and G_A=-2aB/dx, G_B=0. Every explicit two-stage order-two tableau reduces to I+dt F+(dt^2/2)FG. On alternating cells, M_nu=[[1-2nu,-2nu+2nu^2],[6nu,1-6nu^2]]. With W=diag(1,1/3), the energy decrement Q=W-M^TWM has determinant -4nu^4 for all nu>0; it has a negative direction, proving no positive globally nonexpansive CFL for any even mesh. Independently recomputed M,Q, det and rational vector (A,B)=(3/20,1) giving negative decrement -7/5000 at nu=1/10, plus generalized-eigenvalue amplification 1+(sqrt(T^2+48nu^4)-T)/2 with leading excess 3nu^3. This does not prove eigenvalue instability or anything about corrected schemes.

## originality

PASS

Best-of-knowledge O PASS for the exact unconditional one-step L2 energy obstruction and sharp alternating-mode amplification, not for inventing cRKDG. Chen–Sun–Xing establish the compact-stage method and Fourier/eigenvalue stability, a different property from physical W-contraction. Sun 2026 proves weak cell-average entropy inequalities and corrected strong entropy, not the uncorrected whole-P1 energy determinant. Liu–Jiang–Zhang discuss standard RKDG entropy obstructions and compact corrections under different discretization/conditions. A specialized filtered or Lax–Wendroff DG source not fully accessible could overlap.

## value

PASS

The sharp all-positive-CFL counterexample isolates a structural energy-stability limitation of a widely used compact RKDG construction. It distinguishes spectral-radius stability and weak cell-average entropy from norm monotonicity of the full polynomial, and supplies an exact obstruction with quantitative small-step growth. This is a motivated numerical-analysis boundary, not an arbitrary tiny negative test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
