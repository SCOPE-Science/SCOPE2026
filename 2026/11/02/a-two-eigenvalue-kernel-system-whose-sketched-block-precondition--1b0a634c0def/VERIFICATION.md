---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For ||u||=1, K²=I+3uu^T and H=2I+4uu^T. Each 2x2 block K_j=diag(1+s_j,1), B_j=diag(q(1+s_j)(q(1+s_j)+1),q(q+1)); q different positive s_j=j²/S give q different poles d_j=2/beta_j in active diagonal-plus-positive-rank-one C_a. Secular interlacing yields q simple roots, and Jensen gives F(eta0)=1-2(q+1)Σ[2q+1+q*s_j]^-1 <=1-q<0 so no collision with inactive eta0. Every active eigenvector has nonzero first coordinate; symmetrically transformed b also has inactive e2 projection, giving exact Krylov grade q+1. For homogeneous sj=1/q active sector has only two levels, inactive one more. Independent symbolic rational F(eta0) and qxq Krylov rank checks q=2..8; exact arithmetic proof covers all q.

## originality

PASS

Qualified PASS for model-specific exact CG *minimal polynomial* growth and its homogeneous isospectral control, not generic secular equations, CG grades, or BLOKS itself. Vitale et al §3 eq (12), Algo 1, Appendix B state the preconditioner and practical conditioning/performance comparisons; the source does not assert this every-q right-hand-side exact termination anomaly. General block-Jacobi conditioning bounds of Demmel and Kolotilina do not imply its block-orientation specificity.

## value

PASS

Exact Krylov grade is a natural, exact-arithmetic diagnostic of an actual published block preconditioner. A bounded original condition number does not prevent q+1 preconditioned spectral levels, while a same-spectrum equal-orientation example has only three, isolating a testable mechanism. This says nothing unproved about finite-tolerance or wall-clock performance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
