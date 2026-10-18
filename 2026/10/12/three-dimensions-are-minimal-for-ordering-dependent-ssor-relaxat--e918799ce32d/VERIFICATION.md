---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For every real non-diagonal 2x2 SPD system, positive diagonal congruence and sign conjugacy reduce to A=[[1,rho],[rho,1]]. Generalized SSOR eigenvalues have constant product 1-rho² and sum 2-rho² omega(2-omega), uniquely minimized at omega=1, giving unique smallest eigenvalue ratio. Diagonal 2x2 matrices are omega-independent. On the SPD 3-node path with 0<r<1/sqrt2 the natural order at omega=1 has one maximal generalized eigenvalue 1 and two roots in (0,1); implicit derivative gives lambda_min'(1)>0, lambda_max'(1)=0, so kappa'(1)<0. Center-first permutation has a fixed eigenvalue 1 and two roots with fixed product and sum minimized uniquely at omega=1, making omega=1 globally optimal. Independent exact SymPy rebuilt all three determinant identities and F_omega; at r=1/2 the condition derivative equals -1/8-23sqrt(17)/136.

## originality

PASS

Classical SSOR studies already show significant ordering effects and red/black omega=1 optimality for specific elliptic model problems. The new statement isolates a universal 2D no-bifurcation theorem and an explicit same-matrix minimal 3D order pair with opposite relaxation behavior. Checked Kuo–Chan primary text and Ortega bibliographic material plus Resultary/web aliases; no equivalent exact minimal-dimension boundary retrieved. Full Ortega 1991 body was inaccessible and is a material residual originality risk.

## value

PASS

The smallest dimension at which ordering affects optimal SSOR relaxation is a natural structural boundary in SPD preconditioning. Proving an unconditional n=2 impossibility and a transparent 3-node path witness explains that ordering-dependent tuning is not merely large sparse-grid behavior; the exact spectrum also supplies a reusable test case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
